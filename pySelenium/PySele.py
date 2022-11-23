

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from datetime import datetime
import os 
import sys

app_path = os.path.dirname(sys.executable)

now = datetime.now()

month_day_yearr = now.strftime("%m%d%Y")
path = "C:/Users/dsalazar/Downloads/chromedriver_win32/chromedriver.exe"
website = "https://www.the-sun.com/sport/soccer/"

options = Options()
options.headless = True

chrome = Service(executable_path= path)
browser = webdriver.Chrome(service=chrome, options= options)
browser.get(website)

containers = browser.find_elements(by = "xpath", value = '//div[@class = "teaser__copy-container"]' )

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(by = "xpath", value = './a/h2').text
    subtitle = container.find_element(by = "xpath", value = './a/p').text
    link = container.find_element(by = "xpath", value = './a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

dictionary = {'Titles': titles, 'Subtitles': subtitles, 'Link': links}

headline_df = pd.DataFrame(dictionary)
file_name = 'headlines-headless-{month_day_year}.csv'
final_path = os.path.join(app_path,file_name)
headline_df.to_csv(final_path)

browser.quit()
