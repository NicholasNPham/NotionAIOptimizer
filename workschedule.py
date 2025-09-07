from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

from key import *
from function import newDate, timeBlock

import time
import platform

# Check to see which OS coding is running from.
if platform.system() == 'Windows':
    service = Service(executable_path="./chromedriver.exe")
elif platform.system() == 'Darwin':
    service = Service(executable_path="./chromedriver")
else:
    raise OSError("Unsupported Platform or ChromeDriver not Found")

driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

print("Running Selenium Driver...")

# Website link to Employee Portal (ALDI)
driver.get("https://myaldius.staffbase.com/content/page/609ea1450e49ad1c940fd1ab")

# Login Sequence
initialSignInButton = wait.until(EC.element_to_be_clickable((By.ID, "public-login-hint"))).click()
credentialSignInButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "type-uncollapse"))).click()

#Input Username and Password
inputUsername = driver.find_element(By.ID, "identifier").send_keys(username)
inputPassword = driver.find_element(By.ID, "secret").send_keys(password)
submitLoginButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "type-submit"))).click()

# Navigation to MySchedule Button
myScheduleButton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "quick-links-widget"))).click()

# Must be Kept to Allow Click to "quick-links-widget"
time.sleep(2)

# Clicking Schedules in MySchedule
iframes = driver.find_elements(By.TAG_NAME, "iframe")
if len(iframes) > 0:
    driver.switch_to.frame(iframes[0])  # adjust index if necessary

currentWeekSchedule = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='Schedules']")))
scheduleLink = currentWeekSchedule.find_element(By.XPATH, "./ancestor::a")
driver.execute_script("arguments[0].scrollIntoView(true);", scheduleLink)
scheduleLink.click()

# Iterating Through Current Week to Scrape Data Needed
def scrapeWeek():
    daysInWeek = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cmp-schedule-item")))
    dictSchedule = {}
    for days in daysInWeek:
        date = days.find_element(By.CSS_SELECTOR, ".cmp-schedule-item__schedule-date__date").text
        date = newDate(date)

        try:
            shift = days.find_element(By.CSS_SELECTOR,".cmp-schedule-item__schedule-content__hours-range.shift .range-hours").text
        except NoSuchElementException:
            shift = "No Shift Scheduled"

        dictSchedule[date] = timeBlock(shift, date)

    return dictSchedule

# Calling Function first Time
dictSchedule = scrapeWeek()

nextWeekSchedule = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "cmp-date-navigation__icon-arrow-next"))).click()

# Must be keep to allow display text of next week shifts after "cmp-date-navigation__icon-arrow-next" has been clicked.
time.sleep(2)

# Calling Function Second Time (Updating DictSchedule)
dictSchedule.update(scrapeWeek())

# Reversing dictSchedule
reversedDictSchedule = {}
for key in reversed(dictSchedule):
    reversedDictSchedule[key] = dictSchedule[key]

# print(reversedDictSchedule)

# Listing Dictionary to show date and information
# Uncomment to check dictSchedule
# for date, information in dictSchedule.items():
#     print(date, information)


time.sleep(1)

driver.quit()

print("Finished Running Selenium Driver")