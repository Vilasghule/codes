from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
from datetime import date, datetime, timedelta

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options)
page = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.diariomunicipal.sc.gov.br/?r=site/index&q=abertura+categoria%3ALicita%C3%A7%C3%B5es&AtoASolrDocument_page=1'
driver.get(url)
time.sleep(10)

tender_title = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,'h4'))).text    
print("tender_title :",tender_title)

pub_date = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.quiet'))).text
published_date = re.findall("\d+/\d+/\d{4}",pub_date)[0]
print("published_date :",published_date)

resource_url = " "
resource_url += "\n"
resource_url += WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,'h4 a'))).get_attribute('href')
resource_url += "\n"
resource_url += WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div.row.no-print.resultado-pesquisa > a:nth-child(3)'))).get_attribute('href')
resource_url += "\n"
resource_url += WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div.row.no-print.resultado-pesquisa > a:nth-child(4)'))).get_attribute('href')
resource_url += "\n"
resource_url += WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#content > div.row.no-print.resultado-pesquisa > a:nth-child(5)'))).get_attribute('href')
print("resource_url :",resource_url)
