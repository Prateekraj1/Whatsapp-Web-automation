from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("/Users/RAJ/Downloads/chromedriver_win32(1)/chromedriver.exe")
driver.get("https://web.whatsapp.com/")

wait = WebDriverWait(driver, 600)

groupname = input("Enter the Group/person Name")

mesage=input("Enter the desired message")

target = "'"+groupname+"'"

string = mesage

xarg = '//span[contains(@title ,'+target+')]'

target = wait.until(EC.presence_of_element_located((By.XPATH, xarg)))

target.click()

count = 0
input_box1 = driver.find_element_by_class_name('p3_M1')

input_box = input_box1.find_element_by_class_name('_13NKt')
for i in range(3):
    input_box.send_keys(string+Keys.ENTER)
    count = count+1
    print("total message=" + str(count))