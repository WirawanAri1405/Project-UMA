import kagglehub
import shutil
import os

# 1. Konfigurasi Folder Tujuan (Sesuai struktur proyek kita)
project_root = os.getcwd() # Mengambil lokasi folder saat ini
destination_folder = os.path.join(project_root, 'data', 'raw')

# Pastikan folder tujuan ada
os.makedirs(destination_folder, exist_ok=True)

print("--- Memulai Download ---")

# 2. Download Dataset menggunakan kagglehub
# Dataset ini akan masuk ke folder cache sistem
path = kagglehub.dataset_download("takamotoki/jra-horse-racing-dataset")

print(f"\nDataset berhasil didownload ke cache sementara: {path}")
print(f"Sedang memindahkan file ke: {destination_folder} ...\n")

# 3. Pindahkan file CSV dari Cache ke Folder Proyek
files_found = os.listdir(path)
moved_count = 0

for filename in files_found:
    # Kita hanya ambil file CSV (biasanya ada file lain yg tidak perlu)
    if filename.endswith(".csv"):
        source = os.path.join(path, filename)
        destination = os.path.join(destination_folder, filename)
        
        # Copy file (gunakan copy agar cache tetap ada jika butuh lagi, atau move untuk memindah)
        shutil.copy(source, destination)
        print(f"[OK] File disalin: {filename}")
        moved_count += 1

if moved_count == 0:
    print("\n[WARNING] Tidak ada file CSV ditemukan di hasil download!")
else:
    print(f"\n--- Selesai! {moved_count} file telah siap di folder data/raw ---")
    print("Silakan cek folder data/raw Anda.")