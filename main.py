from resize_img import compress_image, resize_image
import os

tp = 'new'
directory_path = f"C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\passport_ibelong\\pasport_{tp}\\"
files = os.listdir(directory_path)
directory_save = f"C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\passport_ibelong\\pasport_{tp}_resized\\"




# Создаем директорию
os.makedirs(directory_save, exist_ok=True)
#save_as_jpeg(files, 50, directory_path, directory_save)
#resize_images(files, 0.5, directory_path, directory_save)
alpha=0.45
resize_image(files, directory_path, directory_save, alpha)

directory_path1 = f"C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\passport_ibelong\\pasport_{tp}_resized\\"
files = os.listdir(directory_path1)
directory_save1 = f"C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\passport_ibelong\\pasport_{tp}_resized2\\"
os.makedirs(directory_save1, exist_ok=True)

compress_image(files, directory_path1, directory_save1, quality=50)

#print(files)  # Выведет список имен файлов в каталоге