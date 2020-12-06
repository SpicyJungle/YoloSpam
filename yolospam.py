from selenium import webdriver
import time
import random
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, StaleElementReferenceException

driver = webdriver.Chrome(executable_path=r'') #Put path to webdriver. (You will need to change webdriver.Chrome to webdriver.{yourdriver} if you don't use the chrome driver.
driver.get('')#Yolo link goes here
ans = []#Write responses here for random responses
while 1:
    try:
        sendButtone = driver.find_element_by_id('send-button')
        textBox = driver.find_element_by_id('text')
        time.sleep(0.1)
        textBox.send_keys()#Text here, or random.choice(ans)
        sendButtone.click()
        driver.refresh()#Refresh to enable text box again
    except StaleElementReferenceException: #Incase page doesnt load fast enough
        print("stale")
        continue
