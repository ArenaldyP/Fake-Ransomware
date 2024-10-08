import os


# Fungsi untuk menghapus ekstensi .K1NGP1NG dari semua file yang ada dalam folder
def restore_extensions(folder_path):
    # Iterasi semua file dalam folder dan subfolder
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.K1NGP1NG'):
                try:
                    # Path file saat ini
                    encrypted_file_path = os.path.join(root, file)

                    # Hapus ekstensi .K1NGP1NG (mengembalikan nama asli tanpa ekstensi .K1NGP1NG)
                    original_file_path = encrypted_file_path[:-len('.K1NGP1NG')]
                    os.rename(encrypted_file_path, original_file_path)

                    print(f"{encrypted_file_path} berhasil dipulihkan menjadi {original_file_path}")
                except Exception as e:
                    print(f"Gagal memulihkan {encrypted_file_path}: {e}")


if __name__ == "__main__":
    # Folder yang ingin diproses, ganti dengan path folder yang diinginkan
    folder_to_process = "J:\Buku 2023\Cybrary\Victim"

    # Panggil fungsi untuk memulihkan ekstensi file
    restore_extensions(folder_to_process)
