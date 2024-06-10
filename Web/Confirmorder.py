from selenium.webdriver.support.wait import WebDriverWait
import time
from Log.Log import Log
from Web.WebWait import WebWait

class ConfirmOrder(WebWait,Log):

    def __init__(self,applesht, row, ponum,driver,qtynum,loadinglocation):
        self.log = self.getLogger()
        self.driver = driver
        self.qtynum = qtynum
        self.loadinglocation = loadinglocation
        self.ponum = ponum
        self.applesht = applesht
        self.row = row
        self.wait = WebDriverWait(self.driver, 40)
        WebWait.__init__(self, self.wait)

    def confirmorder(self):
        self.wait_for_element_byxpath("//*[contains(text(),'Subtotal')]")
        self.wait_for_element_byid("qty0")
        qty = self.driver.find_element_by_id("qty0")
        qty.clear()
        qty.send_keys(self.qtynum)
        time.sleep(1)
        self.wait_for_element_byxpath("//*[contains(text(),'Checkout')]")
        checkout = self.driver.find_element_by_xpath("//*[contains(text(),'Checkout')]")
        checkout.click()
        self.log.info("Quantity Entered")

        self.wait_for_element_byid("selectedAddress")
        self.wait_for_element_byid("termsponumber")
        self.wait_for_element_byid("placeOrder")

        address = self.driver.find_element_by_id("selectedAddress")
        address.click()

        time.sleep(0.5)
        location = str(self.loadinglocation).upper()
        self.wait_for_element_byxpath("//li/span[contains(text(),'" + location + "')][2]")
        locationelem = self.driver.find_element_by_xpath("//li/span[contains(text(),'" + location + "')][2]")
        locationelem.click()
        time.sleep(0.5)
        self.selectedaddress = self.driver.find_element_by_id("selectedAddress").text
        self.log.info("Address Selected")
        self.applesht.cell(row=self.row, column=46).value = self.selectedaddress

        ponumber = self.driver.find_element_by_id("termsponumber")
        ponumber.send_keys(self.ponum)
        time.sleep(0.5)

        placeorder = self.driver.find_element_by_id("placeOrder")
        placeorder.click()







