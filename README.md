# Project UMA

Proyek ini adalah proyek Machine Learning end-to-end yang mencakup pengambilan data, eksplorasi, pemrosesan data, hingga pemodelan menggunakan LightGBM.

## 🗂 Struktur Proyek

Berikut adalah tata letak direktori proyek:

- **models/**: Menyimpan model yang telah dilatih (misalnya `lgbm_model.pkl`).
- **notebooks/**: Berisi Jupyter Notebook untuk setiap tahapan analisis:
  - `EDA.ipynb`: Exploratory Data Analysis (Analisis Data Eksploratif).
  - `01_JRA_Preprocessing.ipynb`: Pembersihan dan pra-pemrosesan data mentah.
  - `02_Feature_Engineering.ipynb`: Pembuatan dan seleksi fitur.
  - `03_Modeling.ipynb`: Pelatihan model, validasi, dan evaluasi.
- **src/**: Berisi skrip Python pendukung (misalnya `download_data.py`).
- **requirements.txt**: Daftar pustaka (library) Python yang diperlukan.

## 🚀 Memulai (Getting Started)

### Prasyarat

Pastikan Anda telah menginstal **Python 3.x**.

### Proses Instalasi

**Clone repositori ini** 
(atau unduh file proyek):
   ```bash
   git clone [https://github.com/wirawanari1405/project-uma.git](https://github.com/wirawanari1405/project-uma.git)
   cd project-uma
```
  
### Buat Virtual Environment
Disarankan menggunakan virtual environment agar library tidak bentrok dengan environment lokal.

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Untuk macOS/Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```
### Install Dependensi
Jalankan perintah berikut untuk menginstal semua library yang dibutuhkan (seperti pandas, numpy, lightgbm, dll):
```bash
pip install -r requirements.txt
```
### Download Data
Jalankan skrip yang ada di folder src untuk mengunduh dataset yang diperlukan:
```bash
python src/download_data.py
```
