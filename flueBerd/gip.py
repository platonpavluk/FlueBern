import os
import shutil

def copy_template_files(source_dir, destination_dir):
    # Перевірка наявності каталогу-шаблону
    if not os.path.exists(source_dir):
        print(f"Помилка: Джерело {source_dir} не знайдено.")
        return False

    # Створення нової папки
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"Створено нову папку: {destination_dir}")
    
    # Копіювання всіх файлів і папок з templ
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        destination_path = os.path.join(destination_dir, item)
        
        if os.path.isdir(source_path):
            # Якщо це каталог, рекурсивно копіюємо вміст
            shutil.copytree(source_path, destination_path)
            print(f"Каталог {item} скопійовано.")
        else:
            # Якщо це файл, просто копіюємо його
            shutil.copy2(source_path, destination_path)
            print(f"Файл {item} скопійовано.")
    
    return True

def main():
    # Запит у користувача на ім'я нового проєкту
    print("Вітаємо в програмі для створення нового проєкту!")
    project_name = input("Введіть ім'я нового проєкту: ").strip()

    # Запит у користувача на місце для створення нового проєкту
    project_location = input("Введіть шлях, де створити новий проєкт: ").strip()
    
    # Формуємо повний шлях до нової папки
    destination_dir = os.path.join(project_location, project_name)

    # Каталог шаблону
    source_dir = "templ"  # Це каталог шаблону, який ми будемо копіювати

    # Виконання копіювання
    if copy_template_files(source_dir, destination_dir):
        print(f"Проєкт успішно створено в папці: {destination_dir}")
    else:
        print("Не вдалося створити проєкт.")

if __name__ == "__main__":
    main()
