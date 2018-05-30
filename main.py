from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.implicitly_wait(1)


def wait_by_id(el_id, seconds=10):
    element = WebDriverWait(driver, seconds).until(
        EC.presence_of_element_located((By.ID, el_id))
    )
    return element


def wait_by_classname(el_class, seconds=10):
    element = WebDriverWait(driver, seconds).until(
        EC.presence_of_element_located((By.CLASS_NAME, el_class))
    )
    return element


def wait_by_css(selector, seconds=10):
    elements = WebDriverWait(driver, seconds).until(
        EC.presence_of_element_located((By.CLASS_NAME, selector))
    )
    return elements

def wait_by_name(selector, seconds=10):
    elements = WebDriverWait(driver, seconds).until(
        EC.presence_of_element_located((By.NAME, selector))
    )
    return elements


driver.get("https://uni.urfu.ru/fx/")
wait_by_id('login',10).send_keys('n.v.ignatchenko@urfu.ru')
wait_by_id('password',10).send_keys('')
wait_by_name('LogonFormSubmit',10).click()
driver.execute_script('document.querySelector(".menuitem_submain_ul").style.display = "block"')
