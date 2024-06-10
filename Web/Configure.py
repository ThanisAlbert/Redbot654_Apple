import time
from selenium.webdriver.support.wait import WebDriverWait
from Log.Log import Log
from Web.Confirmorder import ConfirmOrder
from Web.WebWait import WebWait

class Configure(WebWait,Log):

    def __init__(self, applesht, row, ponum,  driver ,vendorcode, description, location, quantity):
        self.log = self.getLogger()
        self.vendorcode = vendorcode
        self.description = description
        self.location = location
        self.quantity = quantity
        self.driver = driver
        self.ponum = ponum
        self.applesht = applesht
        self.row = row
        self.wait = WebDriverWait(self.driver, 40)
        WebWait.__init__(self,self.wait)

    def configure_product(self):

        self.log.info(self.description)
        self.applesht.cell(row=self.row, column=44).value = self.description
        self.log.info("Configure page entered")

        if "Z15S" in self.vendorcode:

            time.sleep(2)
            self.wait_for_element_byxpath("//*[contains(text(),'Your Configurations')]")
            self.wait_for_element_byxpath("//*[contains(text(),'Keyboard Language')]")
            self.wait_for_element_byid("cpqAddToCartBtn")

            if "10-CORE" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'10‑core')]")
                processor = self.driver.find_element_by_xpath("//label[contains(text(),'10‑core')]")
                processor.click()
                time.sleep(3)

            if "8GB" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'8GB')]")
                memory = self.driver.find_element_by_xpath("//label[contains(text(),'8GB')]")
                memory.click()
                time.sleep(3)

            if "16GB" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'16GB')]")
                memory = self.driver.find_element_by_xpath("//label[contains(text(),'16GB')]")
                memory.click()
                time.sleep(3)

            if "24GB" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'24GB')]")
                memory = self.driver.find_element_by_xpath("//label[contains(text(),'24GB')]")
                memory.click()
                time.sleep(3)

            if "256GB" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'256GB')]")
                storage = self.driver.find_element_by_xpath("//label[contains(text(),'256GB')]")
                storage.click()
                time.sleep(3)

            if "512GB" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'512GB')]")
                storage = self.driver.find_element_by_xpath("//label[contains(text(),'512GB')]")
                storage.click()
                time.sleep(3)

            if "1TB" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'1TB')]")
                storage = self.driver.find_element_by_xpath("//label[contains(text(),'1TB')]")
                storage.click()
                time.sleep(3)

            if "2TB" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'2TB')]")
                storage = self.driver.find_element_by_xpath("//label[contains(text(),'2TB')]")
                storage.click()
                time.sleep(3)

            if "30W" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'30W')]")
                power = self.driver.find_element_by_xpath("//label[contains(text(),'30W')]")
                power.click()
                time.sleep(3)

            if "67W" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'67W')]")
                power = self.driver.find_element_by_xpath("//label[contains(text(),'67W')]")
                power.click()
                time.sleep(3)

            if "35W" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'35W')]")
                power = self.driver.find_element_by_xpath("//label[contains(text(),'35W')]")
                power.click()
                time.sleep(3)

            if "FINAL CUT PRO" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'Final Cut')]")
                finalcut = self.driver.find_element_by_xpath("//label[contains(text(),'Final Cut')]")
                finalcut.click()
                time.sleep(3)

            if "LOGIC PRO" in str(self.description).upper():
                self.wait_for_element_byxpath("//label[contains(text(),'Logic Pro')]")
                logic = self.driver.find_element_by_xpath("//label[contains(text(),'Logic Pro')]")
                logic.click()
                time.sleep(3)

            self.log.info("Configured Successfully")
            self.wait_for_element_byid("cpqAddToCartBtn")
            basket = self.driver.find_element_by_id("cpqAddToCartBtn")
            basket.click()

            confirm = ConfirmOrder(applesht = self.applesht, row= self.row, ponum=self.ponum, driver=self.driver, qtynum=self.quantity,loadinglocation=self.location)
            confirm.confirmorder()
























