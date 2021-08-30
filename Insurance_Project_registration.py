from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from skuska_def import login, tearDown_insurance


driver = webdriver.Chrome(executable_path="C:\Python\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/")
driver.implicitly_wait(10)



print("Prihlasovanie")
login(driver)


#Insurance Project -> link
driver.find_element(By.PARTIAL_LINK_TEXT, "Insurance Project").click()


#Insurance Porject -> Register
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='btn btn-default']").click()

#-------- Sign_Up --------#


#Title
time.sleep(0.5)
driver.find_element(By.ID, "user_title").click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[text()='Major']").click()

#First_name
driver.find_element(By.ID, "user_firstname").send_keys("Erik")

time.sleep(0.5)
#Sur_name
driver.find_element(By.ID, "user_surname").send_keys("Mäsiar")

time.sleep(0.5)
#Phone
driver.find_element(By.ID, "user_phone").send_keys("07548263545")

#--Date_of_Birth--#
#Day
driver.find_element(By.ID, "user_dateofbirth_1i").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//option[@value='1995']").click()

#Month
driver.find_element(By.ID, "user_dateofbirth_2i").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//option[text()='October']").click()

#Year
driver.find_element(By.ID, "user_dateofbirth_3i").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//select[@id='user_dateofbirth_3i']/option[24]").click()

#--Date_of_Birth_END--#

#Provisional
driver.find_element(By.ID, "licencetype_f").click()
time.sleep(0.5)
driver.find_element(By.ID, "licencetype_t").click()

#Licence_period
driver.find_element(By.ID, "user_licenceperiod").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//select[@id='user_licenceperiod']/option[11]").click()
time.sleep(0.5)

#Occupation
driver.find_element(By.XPATH, "//select[@id='user_occupation_id']/option[6]").click()
time.sleep(0.5)

#Address_Street
driver.find_element(By.XPATH, "//input[@name='street']").send_keys("Malá Čalomija")
time.sleep(0.5)

#City
driver.find_element(By.XPATH, "//input[@name='city']").send_keys("Malá Čalomija")
time.sleep(0.5)

#Country
driver.find_element(By.XPATH, "//input[@name='county']").send_keys("Slovakia")
time.sleep(0.5)

#Post_Code
driver.find_element(By.XPATH, "//input[@placeholder='sy24 5be']").send_keys("99109")
time.sleep(0.5)

#E_mail
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("masiar.erik@giuelk.com")
time.sleep(0.5)

#Password
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("YgupEze")
time.sleep(0.5)

#Cofirm_password
driver.find_element(By.XPATH, "//input[@name='c_password']").send_keys("YgupEze")

#Create_submit
driver.find_element(By.XPATH, "//input[@type='submit']").click()
#-------- Sign_Up_END --------#


#--Login_after_signUp--#
#Email
time.sleep(1)
driver.find_element(By.ID, "email").send_keys("masiar.erik@giuelk.com")
#Cofirm_password
time.sleep(1)
driver.find_element(By.ID, "password" ).send_keys("YgupEze")
#Create_submit
time.sleep(1)
driver.find_element(By.XPATH, "//input[@value='Log in']").click()
time.sleep(2)

#print
print("Odhlasovanie")
time.sleep(2)
tearDown_insurance(driver)
print("Odhlásenie - úspešné")
time.sleep(2)


driver.quit()