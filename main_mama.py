from resize_img import compress_image, resize_image
import os

tp = 'new'
directory_path = r"C:\Users\alexe\Documents\Mama_ID_documents_2024_september\svidetelstvo_o_brake"
files = os.listdir(directory_path)
directory_save = r"C:\Users\alexe\Documents\Mama_ID_documents_2024_september\svidetelstvo_o_brake\spravka_resized/"




# Создаем директорию
os.makedirs(directory_save, exist_ok=True)
#save_as_jpeg(files, 50, directory_path, directory_save)
#resize_images(files, 0.5, directory_path, directory_save)
alpha=0.7
resize_image(files, directory_path, directory_save, alpha)

directory_path1 = directory_save
files = os.listdir(directory_path1)
directory_save1 = directory_save
os.makedirs(directory_save1, exist_ok=True)

compress_image(files, directory_path1, directory_save1, quality=70)

#print(files)  # Выведет список имен файлов в каталоге