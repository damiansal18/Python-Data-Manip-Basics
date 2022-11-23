from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import time

path = "C:/Users/dsalazar/Downloads/chromedriver_win32/chromedriver.exe"
chrome = Service(executable_path= path)
website = 'https://docs.google.com/forms/d/e/1FAIpQLSfER5NMO3sDwxlHKBRZfRoxZTrIzp60FgjPKqV3Sbu8EDbECw/viewform'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches',['enable-logging'])
browser = webdriver.Chrome(service=chrome,options= options)

fields = ['Name','Email','Address','Phone number', 'Comments']
data = ['Dee', 'dee@example', '123 Addy St', '6191236459','no comment']
myform = dict(zip(fields,data))

browser.get(website)
time.sleep(3)

for field, data in myform.items():
    textInput = browser.find_element(by= 'xpath', 
    value= f'//div[contains(@data-params, "{field}")]//textarea |' 
    f'//div[contains(@data-params, "{field}")]//input')

    textInput.send_keys(data)

submitButton = browser.find_element(by= 'xpath', value = f'//div[@role="button"]//span[text()="Submit"]')
submitButton.click()

time.sleep(3)
browser.quit()