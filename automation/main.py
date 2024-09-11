import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True) # type: ignore
browser = webdriver.Chrome(options=options)

browser.get('http://www.google.com')
browser.maximize_window()

assert 'Google' in browser.title

elem = browser.find_element(by=By.ID, value='APjFqb')  # Find the search box
elem.send_keys('seleniumhq')

time.sleep(5)

browser.quit()
