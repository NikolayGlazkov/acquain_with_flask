import os
import asyncio
import time
import aiohttp
from bs4 import BeautifulSoup

PATH_NAME = "image"

if not os.path.exists(PATH_NAME):
    os.makedirs(PATH_NAME)

link = 'https://zastavok.net/'

async def download_and_save(session, image_num, image):
    image_link = image.find('a').get('href')
    async with session.get(f"{link}{image_link}", ssl=False) as download_response:
        if download_response.status == 200:
            download_soup = BeautifulSoup(await download_response.text(), 'lxml')
            download_block = download_soup.find('div', class_="image_data").find('div', class_='block_down')
            result_link = download_block.find('a').get('href')
            
            async with session.get(f"{link}{result_link}", ssl=False) as image_response:
                if image_response.status == 200:
                    image_bytes = await image_response.read()
                    filename = f'image/image{image_num}.jpg'
                    with open(filename, 'wb') as file:
                        file.write(image_bytes)
                    print(f'Изображение {image_num}.jpg успешно скачано!')
                else:
                    print(f"Ошибка при загрузке изображения. Код ошибки: {image_response.status}")

async def download_images(session, all_image):
    tasks = []
    image_num = 1
    for image in all_image:
        tasks.append(download_and_save(session, image_num, image))
        image_num += 1
    await asyncio.gather(*tasks)

async def main():
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"{link}/1", ssl=False)
        if response.status == 200:
            soup = BeautifulSoup(await response.text(), 'lxml')
            block = soup.find('div', class_='block-photo')
            if block:
                all_image = block.find_all('div', class_='short_full')
                await download_images(session, all_image)
            else:
                print("Блок 'block-photo' не найден.")
        else:
            print(f"Ошибка при загрузке страницы. Код ошибки: {response.status}")

if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(f"Общее время выполнения программы: {end_time - start_time} секунд")
