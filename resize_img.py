from PIL import Image, ImageFilter
import os

import cv2

def resize_image(list_img, input_path, output_path, alpha):
    i=0
    for img in list_img:
        i+=1
        print(i)
        full_path_source = os.path.join(input_path, img)
        # Загружаем изображение
        image = cv2.imread(full_path_source)
        
        # Получаем новые размеры изображения
        new_width = int(image.shape[1] * alpha)
        new_height = int(image.shape[0] * alpha)
        
        # Уменьшаем размер изображения
        resized_image = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_AREA)
        
        # Создаем путь для сохранения уменьшенного изображения
        full_path_save = os.path.join(output_path, img)
        
        # Сохраняем уменьшенное изображение
        cv2.imwrite(full_path_save, resized_image)

def compress_image(list_img, input_path, output_path, quality=85):
    i=0
    for img in list_img:
        i+=1
        print(i)
        full_path_source = os.path.join(input_path, img)
        image = Image.open(full_path_source)
        # Удаление альфа-канала (если он есть)
        image = image.convert('RGB')       
        # Создаем путь для сохранения изображения стем же именем, но в формате JPEG
        output_img_name = os.path.splitext(img)[0] + ".jpg"
        full_path_save = os.path.join(output_path, output_img_name)
        
        # Сохраняем изображение в формате JPEG с указанным уровнем качества
        image.save(full_path_save, "JPEG", quality=quality)
        
def compress_image_jpg(list_img, input_path, output_path, quality=85):
    i=0
    for img in list_img:
        i+=1
        print(i)
        full_path_source = os.path.join(input_path, img)
        image = Image.open(full_path_source)
        # Удаление альфа-канала (если он есть)
        # Создаем путь для сохранения изображения стем же именем, но в формате JPEG
        output_img_name = os.path.splitext(img)[0] + ".jpg"
        full_path_save = os.path.join(output_path, output_img_name)
        
        # Сохраняем изображение в формате JPEG с указанным уровнем качества
        image.save(full_path_save, "JPEG", quality=quality)        