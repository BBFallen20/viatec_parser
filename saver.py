import csv

def save(items, path):
    with open(path, 'w', newline='', errors='ignore', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Модель", "Артикул", "Ссылка", "Изображение", "Цена", "Наличие", "Производитель", 'Категория', 'Тип камеры', 'Разрешение'])
        for item in items:
            writer.writerow([item['title'], 
                             item['articul'],
                             item['link'], "https://viatec.ua"+item['image'],
                             item['price'],
                             item['available'], 
                             item['manufacturer'],
                             item['category'],
                             item['type'],
                             item['resolution'],
                             ])
