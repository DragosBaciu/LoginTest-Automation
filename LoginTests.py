from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.chrome.service import Service
import time

s=Service("//Users/dragosbaciu/Desktop/test python/chromedriver")
driver = webdriver.Chrome(service=s)

class LoginTests():
    
    
    def login_with_params(self, usernameLogin, passwordLogin):
        driver.get("https://www.demo.guru99.com/V4/")
        
        time.sleep(5)
        
        try:
            driver.switch_to.frame("gdpr-consent-notice");
            save = driver.find_element(By.ID, "save")
            save.click()
        except NoSuchFrameException:
            pass    
        
        username = driver.find_element(By.NAME, "uid")
        username.send_keys(usernameLogin)
        
        password = driver.find_element(By.NAME, "password")
        password.send_keys(passwordLogin)
        
        btnLogin = driver.find_element(By.NAME, "btnLogin")
        btnLogin.click()

    def resetButton(self, usernameLogin, passwordLogin):
        driver.get("https://www.demo.guru99.com/V4/")
        
        time.sleep(5)
        
        try:
            driver.switch_to.frame("gdpr-consent-notice");
            save = driver.find_element(By.ID, "save")
            save.click()
        except NoSuchFrameException:
            pass    
        
        username = driver.find_element(By.NAME, "uid")
        username.send_keys(usernameLogin)
        
        password = driver.find_element(By.NAME, "password")
        password.send_keys(passwordLogin)
        
        btnReset = driver.find_element(By.NAME, "btnReset")
        btnReset.click()    
    
    def login_OK(self):
        self.login_with_params("mngr451732", "EmyjYqU" )        
        time.sleep(5)
       
        actualTitle = driver.title
        
        assert actualTitle == "Guru99 Bank Manager HomePage", "We are not able to login"
        
        print("Test cases Login OK Passed")
        
    
    def login_with_wrong_password(self):
        self.login_with_params("mngr451732", "wrongPassword")
       
        
        try:
            actualTitle = driver.title
            print("Test Case login_with_wrong_password Failed")
        except UnexpectedAlertPresentException:
            print("Test Case login_with_wrong_password Passed")
            
    def login_with_wrong_username(self):
        self.login_with_params("wrongUsername", "EmyjYqU")
       
        
        try:
            actualTitle = driver.title
            print("Test Case login_with_wrong_username Failed")
        except UnexpectedAlertPresentException:
            print("Test Case login_with_wrong_username Passed")
    
    def login_with_wrong_username_and_wrongpassword(self):
        self.login_with_params("wrongUsername", "wrongPassword")
       
        
        try:
            actualTitle = driver.title
            print("Test Case login_with_wrong_username_and_wrongpassword Failed")
        except UnexpectedAlertPresentException:
            print("Test Case login_with_wrong_username_and_wrongpassword Passed")
            
    def login_with_empty_password(self):
        self.login_with_params("mngr451732", "")
        time.sleep(3)
        
        message_to_check = driver.find_element(By.ID, "message18")
        
        assert message_to_check.text == "Password must not be blank", "We should receive an error message that pass must ot be blank"
        print("Test Case login_with_empty_password Passed")
    
                        
    def login_with_empty_username(self):
        self.login_with_params("", "EmyjYqU")
        
        
        try:
            actualTitle = driver.title
            print("Test Case login_with_empty_username Failed")
        except UnexpectedAlertPresentException:
            print("Test Case login_with_empty_username Passed")
            
    def login_with_empty_username_and_password(self):
        self.login_with_params("", "")
        time.sleep(3)
        
        message1 = driver.find_element(By.ID, "message18")
        message2 = driver.find_element(By.ID, "message23")
        
        assert message1.text == "Password must not be blank" and message2.text == "User-ID must not be blank", "User or Password is not valid"
        
        print("Test Case login_with_empty_username_and_password Passed") 
                
    def login_with_username_and_password_with_special_characters(self):
        self.login_with_params("wrong@!?_Username", "!@#$432432~")
       
        
        try:
            actualTitle = driver.title
            print("Test Case login_with_username_and_password_with_special_characters Failed")
        except UnexpectedAlertPresentException:
            print("Test Case login_with_username_and_password_with_special_characters Passed")
            
    def reset_username_and_password(self):
        self.resetButton("mngr451732","EmyjYqU")
        
        btnLogin = driver.find_element(By.NAME, "btnLogin")
        btnLogin.click()
        
        
        try:
            actualTitle = driver.title
            print("Test Case reset_username_and_password Failed")
        except UnexpectedAlertPresentException:
            print("Test Case reset_username_and_password Passed")
    


print("***********************Start TESTING********************************")                
loginTesting = LoginTests()
loginTesting.login_OK()
loginTesting.login_with_wrong_password()
loginTesting.login_with_wrong_username()
loginTesting.login_with_wrong_username_and_wrongpassword()
loginTesting.login_with_empty_password()
loginTesting.login_with_empty_username()
loginTesting.login_with_empty_username_and_password()
loginTesting.login_with_username_and_password_with_special_characters()
loginTesting.reset_username_and_password()

driver.close() 

print("***********************Stop TESTING********************************")     
        