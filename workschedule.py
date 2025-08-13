from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# Website link to Employee Portal (ALDI)
driver.get("https://myaldius.staffbase.com/content/page/609ea1450e49ad1c940fd1ab")

# First Step
wait = WebDriverWait(driver, 10)
buttonOne = wait.until(EC.element_to_be_clickable((By.ID, "public-login-hint")))
buttonOne.click()

# Second Step, Gain Access to Login Input
wait = WebDriverWait(driver, 10)
buttonTwo = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "type-uncollapse")))
buttonTwo.click()

time.sleep(10)

driver.quit()


