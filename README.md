# Project UMA

## 📅 Project Roadmap (KDD Lifecycle)

### 1️⃣ Selection (Seleksi Data) - Hari 1
*Target: Memilih subset data yang relevan dari sekumpulan data mentah.*

- [x] **Setup Environment**
    - [x] Install libraries & setup struktur folder (`raw`, `processed`, `src`).
- [x] **Data Ingestion**
    - [x] Load dataset utama `race_result.csv`.
    - [x] **Feature Selection Awal:** Memilih kolom-kolom krusial (seperti `rank`, `time`, `horse_name`) dan membuang kolom administrasi yang tidak relevan/kosong.

### 2️⃣ Preprocessing (Pembersihan Data) - Hari 2-3
*Target: Membersihkan noise dan menangani inkonsistensi untuk meningkatkan kualitas data.*

- [x] **Data Mapping**
    - [x] Rename header kolom dari Bahasa Jepang ke Bahasa Inggris.
- [x] **Data Cleaning**
    - [x] **Noise Removal:** Hapus baris dengan `rank` non-integer (misal: "Batal/Gagal Finish").
    - [x] **Type Conversion:** Perbaiki format data (misal: `date` menjadi datetime).
    - [x] **Handling Missing Values:** Strategi imputasi atau penghapusan data kosong (NaN).

### 3️⃣ Transformation (Transformasi Data) - Hari 4-6
*Target: Mengubah data menjadi format yang siap dimodelkan (Feature Engineering).*

- [ ] **Feature Construction**
    - [x] Konversi `race_time` (string "1:34.3") menjadi numerik detik (float 94.3).
    - [ ] Hitung fitur baru: `days_since_last_race` (selisih hari antar balapan).
- [x] **Encoding**
    - [x] Ubah data kategorikal (`venue`, `weather`, `surface`) menjadi format numerik (Label/One-Hot Encoding).
- [x] **Aggregasi & Derivasi (Advanced Features)**
    - [x] **History Profiling:** Buat fitur rata-rata performa 3 balapan terakhir (`last_3_avg_rank`).
    - [x] **Clustering (sebagai Fitur):** Kelompokkan gaya lari kuda (Nige/Senkou) menggunakan K-Means dan simpan sebagai kolom fitur baru.

### 4️⃣ Data Mining (Penambangan Data) - Hari 7-10
*Target: Menerapkan algoritma cerdas untuk mengekstrak pola tersembunyi.*

- [x] **Data Splitting**
    - [x] Pisahkan data Training dan Validation menggunakan metode **Time-Series Split** (bukan acak) untuk mencegah kebocoran data masa depan.
- [x] **Modeling**
    - [ ] **Baseline:** Latih model sederhana (Logistic Regression) sebagai tolak ukur.
    - [x] **Core Algorithm:** Implementasi algoritma Gradient Boosting (**CatBoost** atau **LightGBM**) untuk klasifikasi kemenangan (Win/Lose).
- [x] **Pattern Extraction**
    - [x] Latih model untuk mengenali pola kombinasi fitur (misal: Kuda tipe X + Joki Y di Lintasan Z).

### 5️⃣ Interpretation/Evaluation (Evaluasi & Interpretasi) - Hari 11-14
*Target: Menerjemahkan pola yang ditemukan menjadi pengetahuan dan keputusan bisnis.*

- [x] **Model Evaluation**
    - [x] Evaluasi teknis menggunakan metrik **AUC-ROC** dan **Confusion Matrix**.
- [x] **Knowledge Interpretation (Business Logic)**
    - [x] **Betting Simulation:** Menerapkan hasil prediksi pada data validasi untuk menghitung potensi ROI (Return on Investment).
    - [x] Analisis **Value Bet** (Membandingkan probabilitas model vs odds pasar).
- [ ] **Knowledge Representation (Deployment)**
    - [ ] Membangun Dashboard **Streamlit** untuk memvisualisasikan hasil prediksi agar mudah dipahami pengguna.

---

## 📝 Catatan Harian
- **Hari 1:** ...
- **Hari 2:** ...
