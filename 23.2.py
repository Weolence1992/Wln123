import requests
from bs4 import BeautifulSoup
import openpyxl

page_num = 1

while True:
  url = f'https://parfums.ru/fragrance?sort=discount&page={page_num}'
  r = requests.get(url)
  soup = BeautifulSoup(r.content, 'html.parser')
  products = soup.find_all('div', class_='col-6 col-sm-4 prod_item js-ajax-item')

  items = []
  for n in products:
    Brand = n.find('span', class_='unit-brand').text.strip()
    Name = n.find('h3', class_='unit-name').text.strip()
    Price_old = n.find('span', class_='unit-price price-old').text.strip()
    Price_new = n.find('span', class_='unit-price price-new').text.strip()
    items.append({'Brand': Brand, 'Name': Name, 'Price_old': Price_old, 'Price_new': Price_new})
    page_num += 1
  
  for i in items:
      print(i)

  def save_data_to_excel(data, filename):
      wb = openpyxl.Workbook()
      ws = wb.active
      ws.append({'Бренд', 'Название', 'Старая цена(без скидки)', 'Новая цена(со скидкой)'})
      for items in data:
          ws.append({'Brand': Brand, 'Name': Name, 'Price_old': Price_old, 'Price_new': Price_new})
      wb.save(filename)
