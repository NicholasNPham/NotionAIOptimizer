from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://myaldius.staffbase.com/content/page/609ea1450e49ad1c940fd1ab")

time.sleep(10)

driver.quit()
