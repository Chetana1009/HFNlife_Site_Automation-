from telnetlib import EC

from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome("C:\\Users\\Dell\\PycharmProjects\\WebsiteAutomation\\chromedriver.exe")
browser.maximize_window()
browser.get("https://hfnlife.com/")

browser.find_element_by_xpath('//*[@id="shopify-section-header"]/section/header/div/div/div[2]/div[2]/div/a[2]').click()
time.sleep(3)
browser.find_element_by_id("login-customer[email]").send_keys("xxxxxxxxxxxxx@gmail.com")
browser.find_element_by_id("login-customer[password]").send_keys("yyyyyyyyyy")
time.sleep(3)
browser.find_element_by_xpath('//*[@id="header_customer_login"]/button').click()
browser.find_element_by_link_text("Books").click()
browser.find_element_by_id('filter-0-tag-author_james-allen').click()
time.sleep(3)
browser.find_element_by_xpath("//a[contains(text(),'As a Man Thinketh')]").click()
browser.find_element_by_xpath('//*[@id="product_form_6789376737429"]/div[3]/button').click()
browser.find_element_by_xpath("//a[contains(text(),'View cart')]").click()
browser.find_element_by_name('checkout').click()
