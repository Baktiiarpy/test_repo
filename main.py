# some_variable - camel case
# someVariable - camel case

# типы двнных
# изменяемые
# list [] лист или список
# set {} сеть либо множ
# dict {} словар либо обьект

# неизменяемые

# int числа 
# str строки
# bool - Tru или Fals
# NonType - None - ничего
# tuple() кортеж

# age = 25 
# type() #помогает узнать тип данных
# # print((type650))
# print(10+15)
# print(12+12)
# print(2*2)
# print(5 / 2) > 2.5
# print(5 // 2) -> 2

# print(5 % 2)
# result = (5+10)-(8-3)
# print(result)


# users_age = input('34')
# print (users_age)

# name = 'john'

# print(type(name)

# users_name = input('enter your name')
# users_age = input('enter your age')
# print('hello' + users_name + ', you are ' + users_age) 

# a = int(input(1))
# b = int(input(2))
# c = int(input(3))
# res = (a*b)%c
# print(res)

# data = 2
# res = (2 ** 3)
# print(res)

import requests
from bs4 import BeautifulSoup as BS
import csv
def get_html(url):
    response = requests.get(url)
    return response.text
def get_data(html):
    soul = BS(html, 'lxml')
    catalog = soul.find('div', class_ = 'list-view')
    # name = catalog.find('div', 'product_text pull-left').find('a').text
    
    for item in catalog:
        try:
            description = item.find('div', class_ = 'product_text pull-left').text
        except:
            description = ''
        try:
            price = item.find('div', class_ = 'listbox_price text-center').find('strong').text
        except:
            price = ''
        try:
            image = 'https://www.kivano.kg' + item.find('div', class_= 'listbox_img pull-left').find('img').get('src')
        except:
            image = ''
        data = {
            'description': description,
            'price': price,
            'image':image
        }
        write_csv(data)
def write_csv(data):
    with open('mobiles.csv', 'a') as file1:
        writer = csv.writer(file1, delimiter = '$')
        writer.writerow(
            (
                data['description'],
                data['price'],
                data['image']
            )
        )
def main():
    for page in range(2,33):
        print(f'Парсим {page} страницу...')
        url = f'https://www.kivano.kg/mobilnye-telefony?page={page}'
        html = get_html(url)
        get_data(html)
main()
