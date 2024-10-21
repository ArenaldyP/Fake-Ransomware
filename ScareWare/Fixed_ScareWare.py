import os
import psutil, ctypes

# Fungsi untuk menghapus ekstensi .SEIZE dan mengembalikan nama file tanpa ekstensi tersebut
def restore_extensions_in_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.SEIZE'):
                try:
                    file_path = os.path.join(root, file)

                    # Menghapus ekstensi .SEIZE
                    original_file_path = file_path[:-len('.SEIZE')]
                    os.rename(file_path, original_file_path)

                    print(f"{file_path} berhasil dipulihkan menjadi {original_file_path}")
                except Exception as e:
                    print(f"Gagal memulihkan {file}: {e}")

def change_desktop_background_color(color):
    color_ref = (color[2] << 16) | (color[1] << 8) | color[0]
    # Menggunakan SystemParametersInfo untuk mengubah wallpaper
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, color_ref, 3)

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
    change_desktop_background_color((255, 255, 255))
