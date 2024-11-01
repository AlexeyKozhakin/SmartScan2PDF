from resize_img import compress_image, resize_image
import os
from PIL import Image

def rotate_images_in_directory(input_dir, output_dir):
    # Проверяем, существует ли директория для вывода. Если нет, создаем ее.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Получаем список файлов в директории ввода
    image_files = os.listdir(input_dir)

    for image_file in image_files:
        # Полный путь к входному файлу
        input_path = os.path.join(input_dir, image_file)
        
        # Проверяем, является ли файл изображением
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
            # Открываем изображение
            with Image.open(input_path) as img:
                # Поворачиваем изображение на 180 градусов
                rotated_img = img.rotate(180)
                # Получаем путь к выходному файлу
                output_path = os.path.join(output_dir, image_file)
                # Сохраняем повернутое изображение
                rotated_img.save(output_path)

input_dir = "C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\Contract_flat\\"
output_dir = "C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\Contract_flat_rotated\\"
os.makedirs(output_dir, exist_ok=True)
#rotate_images_in_directory(input_dir, output_dir)

def rename_images_to_sequential_numbers(directory):
    # Получаем список файлов в директории
    image_files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # Сортируем список файлов
    image_files.sort()
    
    # Счетчик для порядкового номера
    count = 1
    for image_file in image_files:
        # Получаем полный путь к файлу
        old_path = os.path.join(directory, image_file)
        # Формируем новое имя файла
        new_name = str(count) + ".png"  # Можете изменить расширение на нужное
        new_path = os.path.join(directory, new_name)
        
        # Переименовываем файл
        os.rename(old_path, new_path)
        # Увеличиваем счетчик
        count += 1

directory = "C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\Contract_flat_rotated\\"
rename_images_to_sequential_numbers(directory)
