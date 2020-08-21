from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv
with open('keywords.txt') as my_file:
    for line in my_file:
        search_string = line
        search_string = search_string.replace(' ', '+')
        browser = webdriver.Chrome('chromedriver')
        for i in range(1):
            matched_elements = browser.get('https://www.google.com/search?q="' +
                                           search_string + '"&start=' + str(i))
            login = browser.find_element_by_xpath('//div[@id= "result-stats"]')
            print(login.text)
            with open('result.csv', 'a', newline='', encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow([line,login.text])
                time.sleep(7.4)
                browser.quit()