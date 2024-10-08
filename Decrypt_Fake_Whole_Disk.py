import os
import psutil

# Fungsi untuk menghapus ekstensi .K1NGP1NG dan mengembalikan nama file tanpa ekstensi tersebut
def restore_extensions_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.K1NGP1NG'):
                try:
                    file_path = os.path.join(root, file)

                    # Menghapus ekstensi .K1NGP1NG
                    original_file_path = file_path[:-len('.K1NGP1NG')]
                    os.rename(file_path, original_file_path)

                    print(f"{file_path} berhasil dipulihkan menjadi {original_file_path}")
                except Exception as e:
                    print(f"Gagal memulihkan {file}: {e}")

# Fungsi untuk memproses semua partisi
def process_all_partitions(action):
    partitions = psutil.disk_partitions()
    for partition in partitions:
        if 'system' in partition.opts or partition.fstype == '':
            continue  # Abaikan partisi sistem atau yang tidak valid

        print(f"Memproses partisi: {partition.mountpoint}")
        action(partition.mountpoint)

if __name__ == "__main__":
    # Pulihkan ekstensi file di semua partisi
    process_all_partitions(restore_extensions_in_folder)
