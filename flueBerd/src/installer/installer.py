import os
import subprocess
import requests
from tqdm import tqdm

# URL до Python і двигуна
python_url = "https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe"  # Замініть на актуальний
engine_url = "https://drive.google.com/uc?id=1fNST5lznyZtwF-nUNY05zlp4yd71-SdF&export=download"

# Функція для перевірки, чи встановлений Python
def check_python_installed():
    try:
        # Перевірка, чи є Python в PATH
        subprocess.run(['python', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Python вже встановлений!")
        return True
    except FileNotFoundError:
        print("Python не знайдено. Завантаження Python...")
        return False

# Функція для завантаження файлів з прогрес-баром
def download_file(url, filename):
    # Відправка запиту на отримання файлу
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('Content-Length', 0))  # Отримуємо розмір файлу
    
    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='B', unit_scale=True
    ) as bar:
        # Завантаження файлу по частинах
        for data in response.iter_content(chunk_size=1024):
            bar.update(len(data))  # Оновлення прогрес-бару
            file.write(data)  # Запис частини файлу

    print(f"{filename} завантажено успішно!")

# Якщо Python не встановлений, завантажуємо Python
if not check_python_installed():
    download_file(python_url, "python_installer.exe")
else:
    print("Пропускаємо завантаження Python.")

# Завантажуємо двигун
print("Завантаження двигуна...")
download_file(engine_url, "game_engine.zip")
