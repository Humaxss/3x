from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from skuska_def import login, invalid_login, tearDown, alert_text
from skuska_def import webdriver


driver = webdriver.Chrome(executable_path="C:\Python\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/")
driver.implicitly_wait(10)

login(driver)
tearDown(driver)
alert_text(driver)
invalid_login(driver)
alert_text(driver)
login(driver)
time.sleep(2)
print("Test ukončený!")
driver.quit()




