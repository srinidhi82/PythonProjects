from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome('/Users/srinidhik/SeleniumWebdriver/chromedriver')
browser.get('https://www.seleniumhq.org')

browser.find_element_by_link_text('Download')

element1 = browser.find_element_by_link_text('Download')
element1.text
element1.click()

elem = browser.find_element_by_link_text('Projects')
elem.click()
searchBar = browser.find_element_by_id('q')
searchBar.send_keys('java')

searchBar.send_keys(Keys.ENTER)
