# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time

# # ✅ Updated path
# service = Service(
#     executable_path="C:/Users/USER/Downloads/chromedriver-win64/chromedriver.exe"
# )
# driver = webdriver.Chrome(service=service)

# driver.get("https://www.google.com")
# print("Page title is:", driver.title)

# time.sleep(3)
# driver.quit()

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://localhost:8000")

assert "Congratulations" in browser.title
print("ok")
