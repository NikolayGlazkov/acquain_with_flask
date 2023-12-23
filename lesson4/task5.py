import os
from task1 import timecolc

# Указываем путь к директории
@timecolc
def chat_sync():
    directory = "/Users/nikolay/Documents/acquain_with_flask/data"

    # Получаем список файлов
    files = os.listdir(directory)
    for file_name in files:
        # Создаем полный путь к файлу
        file_path = os.path.join(directory, file_name)

        # Открываем файл HTML в режиме чтения
        with open(file_path, 'r', encoding='utf-8') as file:
            # Читаем содержимое файла
            html_content = file.read()

        # Выводим содержимое файла HTML
        return (len(html_content))

if __name__ == "__main__":
    chat_sync()