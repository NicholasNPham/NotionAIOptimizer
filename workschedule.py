from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from key import *

import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Website link to Employee Portal (ALDI)
driver.get("https://myaldius.staffbase.com/content/page/609ea1450e49ad1c940fd1ab")

wait = WebDriverWait(driver, 10)

# First Step
initialSignInButton = wait.until(EC.element_to_be_clickable((By.ID, "public-login-hint")))
initialSignInButton.click()

# Second Step, Gain Access to Login Input
credentialSignInButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "type-uncollapse")))
credentialSignInButton.click()

#Input Username and Password
inputUsername = driver.find_element(By.ID, "identifier")
inputUsername.clear()
inputUsername.send_keys(username)
inputPassword = driver.find_element(By.ID, "secret")
inputPassword.clear()
inputPassword.send_keys(password)

# Final Boss, Sign in after text field input
submitLoginButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "type-submit")))
submitLoginButton.click()

# Clicking MySchedule Button
myScheduleButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "quick-links-widget")))
myScheduleButton.click()

time.sleep(2)  # give some buffer for redirects

# Clicking Schedules in MySchedule
iframes = driver.find_elements(By.TAG_NAME, "iframe")

if len(iframes) > 0:
    driver.switch_to.frame(iframes[0])  # adjust index if necessary

currentWeekSchedule = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Schedules']")))
scheduleLink = currentWeekSchedule.find_element(By.XPATH, "./ancestor::a")
driver.execute_script("arguments[0].scrollIntoView(true);", scheduleLink)
scheduleLink.click()

scheduleDays = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cmp-schedule-item")))
for days in scheduleDays:
    day = days.find_element(By.CSS_SELECTOR, ".cmp-schedule-item__schedule-date__day").text
    date = days.find_element(By.CSS_SELECTOR, ".cmp-schedule-item__schedule-date__date").text

    try:
        shift = days.find_element(By.CSS_SELECTOR, ".cmp-schedule-item__schedule-content__hours-range.shift .range-hours").text
    except NoSuchElementException:
        shift = "No Shift Scheduled"

    try:
        hour = days.find_element(By.CSS_SELECTOR, ".total-hour").text
    except NoSuchElementException:
        hour = 0

    print(date)
    print(shift)
    print(hour)
    print("-------")

# time.sleep(2)  # give some buffer for redirects
#
# nextWeekSchedule = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cmp-date-navigation__icon-arrow-next")))
# nextWeekSchedule.click()

time.sleep(10)

# driver.quit()