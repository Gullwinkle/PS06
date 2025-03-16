import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
url = "https://www.divan.ru/category/svet"
driver.get(url)
time.sleep(3)

lamps = driver.find_elements(By.CSS_SELECTOR, 'div[data-testid="product-card"]')

parsed_data = []

for lamp in lamps:
    try:
        name = lamp.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        link = lamp.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
        price = lamp.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').get_attribute('content')

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("lamps.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)