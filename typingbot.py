import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome("C:/Users/student/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://10fastfingers.com/advanced-typing-test/english")
time.sleep(5)
word_list = driver.execute_script("return document.getElementById('wordlist').innerHTML")
words = word_list.split("|")
for i in range(len(words)):
    driver.find_element_by_id("inputfield").send_keys(words[i] + " ")
    time.sleep(0.05)
