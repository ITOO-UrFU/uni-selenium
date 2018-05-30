from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from tkinter import *

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


def button_clicked():
    driver = webdriver.Firefox()
    driver.implicitly_wait(1)

    driver.get("https://www.lostfilm.tv")
    driver.find_element_by_xpath('//a[@href="/login"]').click()
    driver.find_element_by_xpath('//input[@name="mail"]').send_keys("lea_alex@mail.ru")
    driver.find_element_by_xpath('//input[@name="pass"]').send_keys("fktrctq")
    driver.find_element_by_xpath('//input[@value="Войти"]').click()
    wait_by_id('main-left-side', 25).find_element_by_class_name('text-block').click()
    wait_by_classname('movie-parts-list',10).find_elements_by_tag_name('tr')[1].find_elements_by_tag_name('td')[2].click()
    wait_by_classname('external-btn', 10).click()
    print(driver.title)
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 10).until(lambda d: d.title != "")
    print(driver.title)
    wait_by_classname('inner-box--link', 10).find_elements_by_tag_name('a')[0].click()
    driver.close()

root=Tk()
# кнопка по умолчанию
button1 = Button()
button1.pack()
# кнопка с указанием родительского виджета и несколькими аргументами.
button2 = Button(root, bg="red", text=u"Кликни меня!", command=button_clicked)
button2.pack()
root.mainloop()