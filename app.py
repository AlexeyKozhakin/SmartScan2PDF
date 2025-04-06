import streamlit as st
from PIL import Image
import os
import tempfile

def resize_image(files, alpha):
    resized = []
    for file in files:
        img = Image.open(file)
        new_size = (int(img.width * alpha), int(img.height * alpha))
        img = img.resize(new_size, Image.LANCZOS)
        resized.append(img)
    return resized

def compress_images(images, quality):
    compressed = []
    for img in images:
        img_rgb = img.convert("RGB")
        temp_img = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        img_rgb.save(temp_img.name, format="JPEG", quality=quality)
        compressed.append(Image.open(temp_img.name))
    return compressed

def convert_to_pdf(images):
    pdf_temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    images[0].save(pdf_temp.name, save_all=True, append_images=images[1:])
    return pdf_temp.name

st.set_page_config(page_title="Image to PDF Converter", layout="centered")
st.title("📄 Преобразование изображений в PDF")

uploaded_files = st.file_uploader("Загрузите изображения", type=["png", "jpg", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    mode = st.radio("Режим", ["Ручной", "Автоматический подбор размера PDF (пока отключено)"])

    if mode == "Ручной":
        alpha = st.slider("Коэффициент сжатия (alpha)", 0.1, 1.0, 0.75, 0.01)
        quality = st.slider("Качество изображения (quality)", 10, 100, 75)

    if st.button("🚀 Создать PDF"):
        with st.spinner("Обработка изображений..."):
            resized_images = resize_image(uploaded_files, alpha)
            compressed_images = compress_images(resized_images, quality)
            pdf_path = convert_to_pdf(compressed_images)

        st.success("✅ PDF успешно создан!")

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Скачать PDF",
                data=f,
                file_name="result.pdf",
                mime="application/pdf"
            )