#Код, написанный с использованием новых селекторов.
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
url = "https://tomsk.hh.ru/vacancies/programmist"
driver.get(url)
time.sleep(3)

vacancies = driver.find_elements(By.CSS_SELECTOR, 'div[class^="vacancy-info"]')

parsed_data = []

for vacancy in vacancies:
    try:
        title_element = vacancy.find_element(By.CSS_SELECTOR, 'a[class^="magritte-link"]')
        title = title_element.text
        link = title_element.get_attribute('href')
        company = vacancy.find_element(By.CSS_SELECTOR, 'span[data-qa="vacancy-serp__vacancy-employer-text"]').text

        try:
            salary = vacancy.find_element(By.CSS_SELECTOR, 'div[class^="compensation"]  span[class^="magritte-text"]').text
        except:
            salary = "Не указана"

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)

print("Данные успешно сохранены в файл hh.csv")