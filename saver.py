import csv

def save(items, path):
    with open(path, 'w', newline='', errors='ignore') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Модель", "Артикул", "Ссылка", "Изображение", "Цена", "Наличие"])
        for item in items:
            writer.writerow([item['title'], item['articul'], item['link'], "https://viatec.ua"+item['image'], item['price'], item['available']])
