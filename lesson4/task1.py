"""Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные
файлы.
� Используйте потоки."""


import requests
import os
import time
PATH_NAME = "data"


# если нет существующих папки, создайте его
if not os.path.exists(PATH_NAME):
    os.mkdir(PATH_NAME)

urls = [
    "https://www.google.ru/",
    "https://gb.ru/",
    "https://ya.ru/",
    "https://www.python.org/",
    "https://habr.com/ru/all/",
    "https://chat.openai.com/",
    "https://www.youtube.com/",
    "https://www.facebook.com/",

]
# загрузка данных из URL-адресов
def timecolc(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Время выполнения: {end_time - start_time} секунд")
    return wrapper

@timecolc
def main():
    for url in urls:
        download_and_save(url)

def download_and_save(url):
    response = requests.get(url)
    filename = (
            "sync_"
            + url.replace("https://", "").replace(".", "_").replace("/", "")
            + ".html"
        )
    filename = os.path.join(PATH_NAME, filename)
    with open(filename, "w",encoding='utf-8') as file:
        file.write(response.text)



if __name__ == "__main__":
    main()