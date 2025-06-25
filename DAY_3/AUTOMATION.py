import pyautogui as p
print(p.position())

# p.moveTo(750,1052,duration=0.2)
# p.click()
# p.write("https://www.instagram.com/accounts/login/?source=auth_switcher")
# p.press('enter')
# p.moveTo(830,301,duration=0.2)
# p.click()
# p.write("ak9843688@gmail.com")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = "its_pulkitbarola"
PASSWORD = "PulkitJain@2005"

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)  

username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(50)

# (Optional) Close the browser
# driver.quit()
