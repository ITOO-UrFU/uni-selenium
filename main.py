from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\\Users\\User\\Desktop\\WORKING\\chromedriver_new.exe")

driver.get("https://openprofession.ru/")