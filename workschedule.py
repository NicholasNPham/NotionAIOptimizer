from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from key import *

import time
import platform


if platform.system() == 'Windows':
    service = Service(executable_path="./chromedriver.exe")
elif platform.system() == 'Darwin':
    service = Service(executable_path="./chromedriver")
else:
    raise OSError("Unsupported Platform or ChromeDriver not Found")

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

dictSchedule = {}

# Iterating Through Current Week to Scrape Data Needed
currentWeekScheduleDays = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cmp-schedule-item")))

for days in currentWeekScheduleDays:
    date = days.find_element(By.CSS_SELECTOR, ".cmp-schedule-item__schedule-date__date").text

    shiftHourList = []

    try:
        shift = days.find_element(By.CSS_SELECTOR, ".cmp-schedule-item__schedule-content__hours-range.shift .range-hours").text
        shiftHourList.append(shift)
    except NoSuchElementException:
        shift = "No Shift Scheduled"
        shiftHourList.append(shift)

    try:
        hour = days.find_element(By.CSS_SELECTOR, ".total-hour").text

        shiftHourList.append(hour)
    except NoSuchElementException:
        hour = 0
        shiftHourList.append(hour)

    dictSchedule[date] = shiftHourList

time.sleep(2)  # give some buffer for redirects

nextWeekSchedule = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cmp-date-navigation__icon-arrow-next")))
nextWeekSchedule.click()

time.sleep(2)  # give some buffer for redirects

# Iterating Through Next Week to Scrape Data Needed
nextWeekScheduleDays = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cmp-schedule-item")))
for days in nextWeekScheduleDays:
    date = days.find_element(By.CSS_SELECTOR, ".cmp-schedule-item__schedule-date__date").text

    shiftHourList = []

    try:
        shift = days.find_element(By.CSS_SELECTOR,".cmp-schedule-item__schedule-content__hours-range.shift .range-hours").text
        shiftHourList.append(shift)
    except NoSuchElementException:
        shift = "No Shift Scheduled"
        shiftHourList.append(shift)

    try:
        hour = days.find_element(By.CSS_SELECTOR, ".total-hour").text

        shiftHourList.append(hour)
    except NoSuchElementException:
        hour = 0
        shiftHourList.append(hour)

    dictSchedule[date] = shiftHourList

for key,value in dictSchedule.items():
    print(key, value)

# Function to convert MM-DD date to ISO Date YYYY-MM-DD
# def dateConversion(date):

# Function to Turn String Shift into two Strings and into 24 Hours
# Function to Remove HR from Hour string


time.sleep(10)

driver.quit()