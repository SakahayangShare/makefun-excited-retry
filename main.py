import os
import shutil
import sys

def main():
    # Nama file sumber dan tujuan (Jalur Absolut WAJIB)
    source_file = 'entry.png'
    output_dir = '/output'
    dest_file = os.path.join(output_dir, source_file)

    # 1. Pastikan file sumber ada
    if not os.path.exists(source_file):
        print(f"Error: {source_file} tidak ditemukan di direktori saat ini.")
        sys.exit(1)

    # 2. Buat folder /output bila belum ada
    try:
        os.makedirs(output_dir, exist_ok=True)
        print(f"Direktori '{output_dir}' siap.")
    except OSError as e:
        print(f"Error: Tidak dapat membuat direktori '{output_dir}': {e}")
        # Jika gagal karena masalah izin (biasa di lingkungan non-root), 
        # kita tetap keluar dengan error sesuai mandat "WAJIB".
        sys.exit(1)

    # 3. Salin file secara byte-identik
    # shutil.copy2 menyalin konten dan juga mencoba mempertahankan metadata file
    try:
        shutil.copy2(source_file, dest_file)
        print(f"Berhasil menyalin '{source_file}' ke '{dest_file}'.")
    except Exception as e:
        print(f"Error saat menyalin file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
