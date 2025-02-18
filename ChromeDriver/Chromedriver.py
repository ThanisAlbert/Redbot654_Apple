from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Chromedriver:

    def __init__(self,headless,downloadpath):
        '''
        :param downloadpath: download folder
        :param headless: True or False
        '''
        self.downloadpath=downloadpath
        self.headless=headless

    def chromedriver(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('prefs', {
            #"download.default_directory": self.downloadpath,
            "download.prompt_for_download": False,  # To auto download the file
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True  # It will not show PDF directly in chrome
        })

        if self.headless==True:
            chrome_options.add_argument("--headless=new")
            chrome_options.headless = True
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            ua = UserAgent(verify_ssl=False)
            userAgent = ua.chrome
            chrome_options.add_argument(f'user-agent={userAgent}')

        #driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", options=chrome_options)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
        params = {'cmd': 'Page.setDownloadBehavior',
                  'params': {'behavior': 'allow', 'downloadPath': self.downloadpath}}
        command_result = driver.execute("send_command", params)

        driver.set_window_position(-10000, 0)

        return driver

