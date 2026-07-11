from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage

class InputFormPage(BasePage):

    NAME = (By.ID,"name")
    EMAIL = (By.ID,"inputEmail4")
    PASSWORD = (By.ID,"inputPassword4")
    COMPANY = (By.ID,"company")
    WEBSITE = (By.ID,"websitename")
    COUNTRY = (By.XPATH,"//*[@id='seleniumform']/div[3]/div[1]/select")
    CITY = (By.ID,"inputCity")
    ADDRESS1 = (By.ID,"inputAddress1")
    ADDRESS2 = (By.ID,"inputAddress2")
    STATE = (By.ID,"inputState")
    ZIPCODE = (By.ID,"inputZip")




    SUBMIT = (
        By.XPATH,
        "//button[contains(text(),'Submit')]"
    )

    SUCCESS = (
        By.CSS_SELECTOR,
        ".success-msg"
    )

    def fill_form(self,name,email,password,company,website,country,city,address1,address2,state,zipcode):
        self.type(self.NAME,name)
        self.type(self.EMAIL,email)
        self.type(self.PASSWORD,password)
        self.type(self.COMPANY,company)
        self.type(self.WEBSITE,website)
        self.select_dropdown_value(self.COUNTRY,'value',country)
        self.type(self.CITY, city)
        self.type(self.ADDRESS1,address1)
        self.type(self.ADDRESS2,address2)
        self.type(self.STATE,state)
        self.type(self.ZIPCODE,zipcode)





    def submit(self):
        self.click(self.SUBMIT)

    def success_message(self):
        return self.get_text(self.SUCCESS)


