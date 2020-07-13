from bs4 import BeautifulSoup
from request import get_html
from saver import save
import os
import time
# Адресс страницы 'https://hard.rozetka.com.ua/videocards/c80087/' https://hard.rozetka.com.ua/motherboards/c80082/


# Главная функция
def parse(url):
    # Получаем html
    page = get_html(url)
    if page.status_code == 200:
        print('='*50)
        print('[+]Connected.')
        print('=' * 50)
        hardware = []
        manufacturer, resolution = None, None
        cameratype = input("Cameratype:\n")
        resolution = input('Resolution:\n')
        question = input("Add manufacturer?1-Yes|2-No\n")
        if question == '1':
            manufacturer = input('Enter manufacturer:\n')
        pages = get_pages(page.text)
        for page in range(1, pages+1):
            print(f'Info checking {page} from {pages}')
            page = get_html(url, params={'page': page})
            hardware.extend(content(page.text, cameratype, resolution, manufacturer if manufacturer else ''))
        print(f'''{'='*50}
\t\t\t\tReady!
Finded: {len(hardware)} products.
{'='*50}''')
        path = 'C:/Users/Public/Desktop'
        filename = "/" + input('Enter filename:\n')+'.csv'
        path += filename
        try:
            save(hardware, path)
            print('='*50)
            print('Saved.(hardware.csv)')
            print('='*50)
            time.sleep(1.5)
            os.startfile(path)
        except:
            print("Failed to save to the path.")
    else:
        print('='*50)
        print('[!]Connection error.')
        print('=' * 50)


def get_pages(page):
    soup = BeautifulSoup(page, 'html.parser')
    pag = soup.find('ul', class_='pagination')
    if pag:
        pagination_item = pag.find_all('a')
        if pagination_item:
            return int(pagination_item[-2].get_text())
        else:
            return 1
    else:
        return 1


def content(page, cameratype, resolution,  manufacturer='', category='Видеонаблюдение, Камеры'):

    soup = BeautifulSoup(page, 'html.parser')
    # Парсим все карточки из каталога
    cards = soup.find_all('a', class_='product-item')[:-10]
    # Словарь для итоговых значений
    videocards = []
    # Циклом проходимся по всем карточкам,собирая инфу
    for card in cards:
        videocards.append({ # Добавляем в словарь
            'title': card.find('p', class_='product-title').get_text(strip=True), # Название товара
            'articul': card.find('div', class_='product-item__description').find('span').get_text(strip=True), # Арикул
            'link': card.get('href'), # СсылОЧКА
            'image': card.find('img').get('src'), # Ссылка на картинку
            'price': card.find('div', class_='product-item__price').get_text(strip=True).replace('грн', ""), # Цена
            'available': card.find('p').get_text(strip=True), # Наличие
            'manufacturer': manufacturer, # Производитель
            'resolution': resolution, # Качество
            'category': category,
            'type': cameratype,

        })
    return videocards


url = input("Enter url:\n")
parse(url)
time.sleep(1.5)
