import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver


def login(driver):
    # User_id
    driver.find_element(By.NAME, "uid").send_keys("mngr350387")
    time.sleep(1)

    # password
    driver.find_element(By.NAME, "password").send_keys("yqUhytY")
    time.sleep(1)

    # login
    driver.find_element(By.NAME, "btnLogin").click()
    time.sleep(1)

def tearDown(driver):
    driver.find_element(By.PARTIAL_LINK_TEXT, "Log out").click()

def alert_text(driver):
    alert = driver.switch_to.alert
    alert.dismiss()

def invalid_login(driver):
    # User_id
    driver.find_element(By.NAME, "uid").send_keys("Zlé meno mhr4145")
    time.sleep(1)

    # password
    driver.find_element(By.NAME, "password").send_keys("fdspEze")
    time.sleep(1)

    # login
    driver.find_element(By.NAME, "btnLogin").click()
    time.sleep(1)

def tearDown_insurance_project(driver):
    driver.find_element(By.XPATH, "//input[@value='Log out']").click()