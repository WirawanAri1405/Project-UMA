# Project UMA

# 📅 Roadmap & Progress Tracking

### ✅ Fase 1: Data Preparation & Cleaning (Hari 1-3)
*Fokus: Mengubah raw data berbahasa Jepang menjadi format tabular yang bersih dan siap olah.*

- [x] **Setup Project**
    - [x] Buat virtual environment & install libraries (`pandas`, `scikit-learn`, `catboost`, `streamlit`).
    - [x] Struktur folder: `data/raw`, `data/processed`, `notebooks`, `src`.
- [x] **Data Ingestion (race_result.csv)**
    - [x] Load CSV ke Pandas DataFrame.
    - [x] Rename kolom Jepang ke Inggris (Mapping: `着順`->`rank`, `タイム`->`time`, dll).
    - [x] Filter kolom penting saja, buang kolom administrasi yang kosong.
- [ ] **Data Cleaning**
    - [ ] Bersihkan kolom `rank`: Hapus data non-integer (seperti "Batal/Gagal").
    - [ ] Konversi kolom `date` ke format datetime.
    - [ ] Handling Missing Values (Imputasi atau Drop).
- [ ] **Feature Engineering Dasar**
    - [ ] Konversi `time` (1:34.3) menjadi detik (94.3 detik).
    - [ ] Encoding Label untuk data kategorikal (`venue`, `weather`, `surface`).
- [ ] **Finalisasi Data**
    - [ ] Sort data berdasarkan tanggal.
    - [ ] Simpan sebagai `data/processed/master_data_v1.csv`.

### ⛏️ Fase 2: Mining & Feature Enrichment (Hari 4-6)
*Fokus: Membuat fitur tambahan cerdas untuk meningkatkan akurasi model.*

- [ ] **Running Style Clustering**
    - [ ] Load `corner_passing_order.csv` (jika ada) atau gunakan data passing dari `race_result`.
    - [ ] Lakukan K-Means Clustering untuk mengelompokkan gaya lari (Nige, Senkou, Sashi, Oikomi).
    - [ ] Gabungkan (Merge) hasil cluster ke `master_data_v1.csv`.
- [ ] **History Features (Time Series)**
    - [ ] Buat fitur `last_5_race_avg_rank`: Rata-rata peringkat di 5 balapan terakhir.
    - [ ] Buat fitur `days_since_last_race`: Selisih hari dari balapan sebelumnya.
- [ ] **Jockey/Trainer Synergy**
    - [ ] (Opsional) Hitung Win Rate historis untuk setiap Joki dan Trainer sebelum tanggal balapan.

### 🧠 Fase 3: Predictive Modeling (Hari 7-10)
*Fokus: Melatih dan validasi model Machine Learning.*

- [ ] **Data Splitting**
    - [ ] Time-Series Split: Train (Data lama) vs Validation (Data tahun terakhir). *Jangan di-shuffle!*
- [ ] **Model Training (Baseline)**
    - [ ] Latih model sederhana (Logistic Regression) sebagai benchmark.
- [ ] **Model Training (Advanced)**
    - [ ] Implementasi **CatBoost** atau **LightGBM**.
    - [ ] Tuning Hyperparameter dasar (Learning rate, depth).
- [ ] **Evaluation**
    - [ ] Cek metrik AUC-ROC (kemampuan membedakan menang/kalah).
    - [ ] Cek Confusion Matrix.
    - [ ] Simpan model terbaik (`model.cbm` atau `.pkl`).

### 💰 Fase 4: Betting Strategy Simulation (Hari 11)
*Fokus: Menguji apakah model bisa menghasilkan profit secara teoritis.*

- [ ] **Simulasi Backtesting**
    - [ ] Gunakan data Validation (Data yang belum dilihat model).
    - [ ] Bandingkan Prediksi Model vs Odds Pasar.
    - [ ] Hitung EV (Expected Value).
- [ ] **Analisis ROI**
    - [ ] Hitung total profit/loss jika bertaruh flat (misal 100 yen) pada setiap rekomendasi model.

### 🚀 Fase 5: Dashboard & Deployment (Hari 12-14)
*Fokus: Membuat antarmuka pengguna sederhana untuk demo.*

- [ ] **Backend Script**
    - [ ] Buat fungsi `predict_race(race_data)` yang memuat model tersimpan.
- [ ] **Frontend (Streamlit)**
    - [ ] Buat UI untuk upload data race baru (CSV) atau input manual.
    - [ ] Tampilkan tabel hasil prediksi (Nama Kuda | Probabilitas Menang | Rekomendasi).
    - [ ] Visualisasi grafik sederhana (Scatter plot performa).
- [ ] **Final Review**
    - [ ] Dokumentasi singkat cara menjalankan aplikasi.
    - [ ] Rekap hasil proyek.

---

## 📝 Catatan Harian
*(Gunakan bagian ini untuk mencatat kendala atau ide baru)*

- **Hari 1:** ...
- **Hari 2:** ...
