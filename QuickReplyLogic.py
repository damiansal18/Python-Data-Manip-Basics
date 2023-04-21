from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 
from time import sleep

browser = uc.Chrome()
browser.delete_all_cookies()

#path = "C:/Users/dsalazar/Downloads/newChromeDriver/chromedriver_win32/chromedriver.exe"
#options = Options()
#chrome = Service(executable_path= path)
#browser = webdriver.Chrome(service=chrome, options= options)

browser.get('https://gmail.com')
sleep(10)

#browser.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form[2]/button')
#sleep(5)

#Set the name of the expected sender
#expectedContact = " "

#Set the timeframe to search
#timeframeStart = ''
#timeframeEnd = ''
#wait.until(presence_of_element('locator')) or timeframe has expired

email = ""
password = " "
#Get user login and password


LoginBox = browser.find_element(By.XPATH, ' //*[@id="identifierId"]')
LoginBox.send_keys(email)

nextButton = browser.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span')
nextButton.click() #next button on login page
sleep(5)

PasswordBox = browser.find_element(By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input') #password input
PasswordBox.send_keys(password)


PasswordNextButton = browser.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[3]') #next button password page
PasswordNextButton.click()
sleep(5)

#browser.get('https://gmail.com')
#sleep(5)

print("login succesful")

    