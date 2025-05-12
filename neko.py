import urllib.request
from typing import final

import requests
import random
import os

def main():
    print('+==============================+')
    print('|    Cофт был создан сырком!   |')
    print('|       GitHub RZT | Team      |')
    print('+==============================+')
    print('')
    print('1. Досс ')
    print('2. Поиск информации')
    print('3. Анали сайта')
    print('4. БД')
    input('>>> ')
    asd()


def asd():
    print('Подключение и установка....')
    try:
        for i in range(100):
            idr = random.randint(1, 1355)
            url1 = f"https://res.cloudinary.com/f1sk/yiff/yiff_{idr}.jpg"

            img_data = requests.get(url1).content

            # Путь к директории загрузок
            download_path = os.path.join(os.environ['HOME'], 'storage', 'Pictures', f'{idr}.jpg')

            with open(download_path, 'wb') as handler:
                handler.write(img_data)
            print(f'Установлено {i}%')

    except:
        for i in range(100):
            idr = random.randint(1, 1355)
            url1 = f"https://res.cloudinary.com/f1sk/yiff/yiff_{idr}.jpg"

            img_data = requests.get(url1).content
            with open(f'{idr}.jpg', 'wb') as handler:
                handler.write(img_data)
            print(f'Установлено {i}%')
    finally:
        print('Все 100 Порно картинок с фурри установлено!')
main()