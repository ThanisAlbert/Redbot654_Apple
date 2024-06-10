import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from ChromeDriver.Chromedriver import Chromedriver
from Log.Log import Log
from Web.Configure import Configure
from Web.WebWait import WebWait

class WebNavigate(WebWait,Log):

    def __init__(self,applesht,row, driver,ponum,vendorcode,description,location,qty):
        self.log = self.getLogger()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 40)
        self.vendorcode = vendorcode
        self.description = description
        self.location = location
        self.qty = qty
        self.ponumber = ponum
        self.applesht = applesht
        self.row = row
        #super(WebNavigate,self).__init__(self.wait)
        WebWait.__init__(self,self.wait)

    def web_navigate(self):

        self.driver.get("https://idmsa.apple.com/IDMSWebAuth/signin?appIdKey=070c5f58894e389c757e88ac40b772b15bac8e980770c156c73e8d374a6afa70&baseURL=https%3A%2F%2Fecommerce.apple.com%3A443%2Fopsb2b%2F&language=US-EN&view=1&path=%2Flogin")
        self.log.info("Apple page logged in")
        # self.driver.maximize_window()
        self.wait_for_element_byxpath("//*[@id=\"aid-auth-widget-iFrame\"]")
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//*[@id=\"aid-auth-widget-iFrame\"]"))
        self.wait_for_element_byid("account_name_text_field")
        element = self.driver.find_element_by_id("account_name_text_field")
        element.send_keys("bhuvanasundar.rn@redington.co.in")
        self.driver.find_element_by_id("account_name_text_field").send_keys(Keys.ENTER)
        self.log.info("username entered")
        self.wait_for_element_byid("password_text_field")
        self.driver.find_element_by_id("password_text_field").send_keys("Redington@2022")
        self.driver.find_element_by_id("password_text_field").send_keys(Keys.ENTER)
        self.log.info("password entered")
        self.driver.switch_to.default_content()

        self.wait_for_element_byxpath("//div[@id='shimpmentplantable']")
        self.wait_for_element_byxpath("//h1[contains(text(), 'My Shipment Plans')]")
        self.wait_for_element_byxpath("//span[@class='i-extlink iconsmall']")

        self.driver.find_element_by_xpath("//span[@class='i-extlink iconsmall']").click()
        self.wait_for_element_byxpath("//a[contains(text(),'Apple Store for REDINGTON LIMITED')]")
        self.wait_for_element_byid("topsearch")
        self.driver.find_element_by_id("topsearch").click()
        time.sleep(5)

        self.wait_for_element_byid("js-site-search-input")
        self.driver.find_element_by_id("js-site-search-input").send_keys(self.vendorcode)
        self.driver.find_element_by_id("js-site-search-input").send_keys(Keys.ENTER)

        #self.driver.get("https://ecommerce.apple.com/asb2bstorefront/asb2b/en_GB/INR/search/?text=z15s")
        #self.driver.get("https://ecommerce.apple.com/asb2bstorefront/asb2b/en_GB/INR/search/?text="+ self.vendorcode)

        self.wait_for_element_byxpath("//div[@class='list-item']/a")
        config = self.driver.find_element_by_xpath("//div[@class='list-item']/a")
        config.click()

        conf = Configure(applesht = self.applesht, row= self.row ,ponum=self.ponumber, driver=self.driver, vendorcode=self.vendorcode, description=self.description, location=self.location, quantity=self.qty)
        conf.configure_product()
