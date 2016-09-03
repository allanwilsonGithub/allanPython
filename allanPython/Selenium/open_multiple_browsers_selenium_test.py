from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

urls = ('http://www.google.com',
        'http://www.iwoot.com',
        'http://www.yahoo.com',
        'http://www.bbc.com')

for url in urls:
    cmd = "\"window.open('"+ url +"','_blank')\""
    print cmd
    driver.get(url)
    driver.execute_script("window.open('http://www.google.com','_blank')")