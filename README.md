# mini_project_1_ddp
NABILA VIVIANA ASRI |2509116098 |SITEM INFORMASI C 2025

TEMA : SISTEM PEMESANAN TIKET BUS

# FLOWCHART


<img width="370" height="1091" alt="FLOWCHART SISTEM PEMESANAN TIKET BUS" src="https://github.com/user-attachments/assets/4266ed74-219e-4ba9-a2e3-a77ad94ccd21" />

# Mulai

Proses dimulai ketika pengguna membuka aplikasi atau sistem pemesanan tiket bus.

# Pilih Menu

Pengguna diberikan dua pilihan utama:

Lihat rute = menampilkan daftar rute bus yang tersedia.

Pesan tiket = langsung menuju ke proses pemesanan tiket.

# Jika Pilih "Lihat Rute"

Sistem akan menampilkan daftar rute bus yang tersedia.

Setelah melihat rute, pengguna diberikan pertanyaan:
“Lanjut pesan tiket?”

Jika Ya = masuk ke menu pemesanan tiket.

Jika Tidak = proses langsung selesai.

# Jika Pilih "Pesan Tiket"

Pengguna diminta memilih tujuan perjalanan, misalnya:

- Jakarta
- Surabaya
- Bandung
- Jogja

Sistem meminta nama pengguna untuk dicatat pada tiket.

Sistem meminta jumlah tiket yang ingin dibeli.

Sistem menghitung total biaya pembelian tiket

Total Pembayaran
= Harga Tiket × Jumlah Tiket

# Apakah Ingin Melihat Detail Tiket?

Sistem memberikan opsi:

Ya = menampilkan detail tiket:

- Nama pemesan

- Tujuan perjalanan

- Jumlah tiket

- Harga per tiket

- Total pembayaran

Tidak = langsung menuju tahap selesai.

# Selesai

# CODINGAN

<img width="1920" height="1080" alt="CODINGAN 1 (2)" src="https://github.com/user-attachments/assets/eca86f39-fb52-4ba1-82be-896f1d7f5c8e" />


<img width="1920" height="1080" alt="CODINGAN 2 (2)" src="https://github.com/user-attachments/assets/04be8b58-045a-4819-ad58-d24cc6f0dd5b" />


<img width="1920" height="1080" alt="CODINGAN 3" src="https://github.com/user-attachments/assets/b1dac5e2-f520-4655-b96f-d4c1059c2125" />





# RUTE = berisi daftar kota tujuan bus

# harga_tiket = berisi harga tiket sesuai urutan kota di [list] rute

"masukkan" = input yang berarti masukkan. (user diminta untuk memilih "lihat rute" atau "pesan tiket")

# jika user memilih "lihat rute" maka akan ditampilkan list rute bus

lanjut = "input"yang berarti masukkan. user akan ditanya apakah ingin melanjutkan ke menu pesan tiket? user diminta untuk memilih ya atau tidak

jika ya = maka user akan langsung masuk ke menu pesan tiket

jika tidak = maka selesai dan otomatis keluar karna exit(yang berarti keluar )

# jika user memilih "pesan tiket" maka user akan diminta untuk memilih tujuan yang ingin di datangi :jakarta/surabaya/bandung/jogja
program akan mencocokkan input dengan rute yang ada misal: user memilih jakarta maka program akan menyimpan :nama, harga tiket ke tujuan anda, dan tujuan perjalanan anda

program akan menanyakan nama pemesan tiket

lalu program akan menampilkan harga tiket untuk tujuan yang anda pilih

lalu program menanyakan berapa tiket yang anda ingin beli

lalu program menghitung harga tiket yang di pilih dikali jumlah tiket yang dibeli

lalu program akan menampilkan total tiket yang di pesan

input untuk menanyakan apakah user ingin memlihat detail tiket? ya/ tidak

jika ya maka program akan menampilkan :
- NAMA
- TUJUAN
- JUMLAH TIKET YANG USER BELI
- HARGA TIKET UNTUK TUJUAN YANG DIPILIH USER
- TOTAL PEMBAYARAN USER

jika user memilih tidak maka program akan menampilkan tulisan "transaksi selesai hati hati dijalan"

jika user tidak memilih ya atau tidak maka program akan menulis "TERIMAKASIH SELAMAT MENIKMATI PERJALANAN"












