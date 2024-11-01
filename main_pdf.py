from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Image
import os

tp = 'new'

def create_pdf(images, path, output_pdf):
    doc_path = os.path.join(path, output_pdf)
    doc = SimpleDocTemplate(doc_path, pagesize=letter)
    story = []
    for image in images:
        image_path = os.path.join(path, image)
        img = Image(image_path)
        img.drawHeight = 500  # Вы можете настроить высоту и ширину изображения по вашему выбору
        img.drawWidth = 500        
        story.append(img)

    doc.build(story)


import img2pdf

def convert_images_to_pdf(image_paths, output_pdf):
    with open(output_pdf, "wb") as f:
        f.write(img2pdf.convert(image_paths))



#path = f"C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\passport_ibelong\\pasport_{tp}_resized2\\"
#path = f"C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\Contract_flat_resized2\\"
#path = f"C:\\Users\\alexe\\Downloads\\ready_docs\\LTR_resized\\application2_resized2\\"
#path = f"C:\\Users\\alexe\\Downloads\\ready_docs\\ready_docs\\5_work_FS3\\pics\\"
path = r"C:\Users\alexe\Documents\Mama_ID_documents_2024_september\svidetelstvo_o_brake\spravka_resized"
#images = os.listdir(path)
output_pdf = "application.pdf"  # Имя PDF-файла, который вы хотите создать
output_pdf = os.path.join(path, output_pdf)
#create_pdf(images, path, output_pdf)



images = os.listdir(path)
image_paths = [os.path.join(path, image) for image in images] 
convert_images_to_pdf(image_paths, output_pdf)