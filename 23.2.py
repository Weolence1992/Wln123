import requests

from bs4 import BeautifulSoup

import openpyxl

from openpyxl import Workbook

# while True: перебор до последней страницы продукции (996 страниц)

url = f'https://parfums.ru/fragrance?sort=discount'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
products = soup.find_all('div', class_='col-6 col-sm-4 prod_item js-ajax-item')

Parfums = []

for n in products:
    Brand = n.find('span', class_='unit-brand').text.strip()
    Name = n.find('h3', class_='unit-name').text.strip()
    Price_old = n.find('span', class_='unit-price price-old').text.strip()
    Price_new = n.find('span', class_='unit-price price-new').text.strip()

    Parfums.append({'Brand': Brand, 'Name': Name, 'Price_old': Price_old, 'Price_new': Price_new})
    Parfums.append([Brand, Name, Price_old, Price_new])

for i in Parfums:
    print(i)




print(f'Name parfume: {Brand} {Name}, Price: {Price_old}, Discount price: {Price_new}')


wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Parfume prices"
sheet.append(['Бренд', 'Наименование', 'Цена без скидки', 'Цена со скидкой'])
for parf in i:
    sheet.append(Brand, Name, Price_old, Price_new)
wb.save('Parfume prices')
