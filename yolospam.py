from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException

driver = webdriver.Chrome(executable_path=r'C:\Users\eiken\Downloads\chromedriver_win32\chromedriver.exe')
driver.get('')
ans = ['Heil stalin', 'Stalin <3', 'Long Live Stalin', 'StalinLivesMatter', 'Long live stalin!', "stalin e babe",
       'Stalin er mitt forbilde.'
       ]
while 1:
    try:
        sendButtone = driver.find_element_by_id('send-button')
        textBox = driver.find_element_by_id('text')
        time.sleep(0.5)
        textBox.send_keys(random.choice(ans))
        sendButtone.click()
        driver.refresh()
    except StaleElementReferenceException:
        print("stale")
        continue
