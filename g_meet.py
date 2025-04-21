import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver_path = "C:/Users/psbd1/OneDrive/Documents/python/codes/Web-automation/env/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") OPTIONAL

def wait(css_selector):
    try:
        WebDriverWait(browser,20).until(EC.visibility_of_element_located((By.CSS_SELECTOR,css_selector)))
    
    except TimeoutException:
        print('time out in wait of {}'.format(css_selector))
        exit()

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
browser.maximize_window()

browser.get("https://classroom.google.com/u/1/h")
browser.implicitly_wait(1)
search_box = browser.find_element_by_css_selector('.whsOnd.zHQkBf')
# print(search_box)
search_box.click()
search_box.send_keys(Keys.MAIL)
search_box.send_keys(Keys.ENTER)

time.sleep(5)
search_box = browser.find_element_by_css_selector('.whsOnd.zHQkBf')
search_box.click()
search_box.send_keys(Keys.PASSWORD)
search_box.send_keys(Keys.ENTER)
# time.sleep(15)
wait('.YVvGBb.csjh4b')
# try:
#     element = WebDriverWait(browser, 20).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, ".YVvGBb.csjh4b"))
#     )
# finally:
#     ()
search_box = browser.find_element_by_css_selector('.YVvGBb.csjh4b')
search_box.click()
time.sleep(15)
# wait('.l4V7wb.Fxmcue')
search_box = browser.find_elements_by_css_selector('.l4V7wb.Fxmcue')
search_box[5].click()
# time.sleep(5)
# search_box = browser.find_elements_by_css_selector('.RveJvd.snByac')
# search_box[4].click()
# time.sleep(5)
# wait('.l4V7wb.Fxmcue')
time.sleep(20)
search_box = browser.find_element_by_css_selector('.l4V7wb.Fxmcue')
search_box.click()
