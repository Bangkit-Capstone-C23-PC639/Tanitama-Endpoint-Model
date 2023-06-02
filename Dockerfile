# Menggunakan image python sebagai base image
FROM python

# Mengatur working directory di dalam container
WORKDIR /app

# Menyalin requirements.txt ke dalam container
COPY requirements.txt .

# Menginstall dependencies yang diperlukan
RUN pip install -r requirements.txt

# Menyalin seluruh file aplikasi ke dalam container
COPY . ./

# Menjalankan perintah untuk memulai aplikasi Flask
CMD ["python", "app.py"]
