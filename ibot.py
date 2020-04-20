from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from pw import pw

# driver = webdriver.Chrome(ChromeDriverManager().install())
class Instabot:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")
        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
        sleep(2)
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        sleep(10)
Instabot("manulangat",pw)
print(pw)