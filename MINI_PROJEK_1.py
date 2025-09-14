# MINI PROJEK SISTEM PEMESANAN TIKET BUS 
# NABILA VIVIANA ASRI
# NIM: 2509116098

rute =["jakarta", "surabaya", "bandung", "yogyakarta"]
harga_tiket = [100000, 150000, 200000, 1250000]
masukkan =input("pilih menu: (lihat rute/pesan tiket): ")
if masukkan =="lihat rute":
    print("========= LIST RUTE ===========")
    print("JAKARTA")
    print("SURABAYA")
    print("BANDUNG")
    print("YOGYAKARTA")
    print("===============================")
lanjut =input("apakah anda ingin melanjutkan untuk pemesanan tiket (ya/tidak)?:")
if lanjut=="ya":
    masukkan = "pesan tiket"   
else:
    print("TERIMA KASIH")
    exit()
if masukkan =="pesan tiket":
    a = (input("pilih tujuan anda (jakarta/surabaya/bandung/jogja)?:"))
    if a == "jakarta":
        nama =input("masukkan nama anda:")
        print(rute[0], "=Rp",harga_tiket[0])
        harga_pilihan = harga_tiket[0]
        tujuan = rute[0]
    elif a == "surabaya":
        nama =input("masukkan nama anda:")
        print(rute[1], "=Rp", harga_tiket[1])
        harga_pilihan = harga_tiket[1]
        tujuan = rute[1]
    elif a == "bandung":
        nama =input("masukkan nama anda:")
        print(rute[2], "=Rp", harga_tiket[2])
        harga_pilihan = harga_tiket[2]
        tujuan =rute[2]
    elif a == "jogja":
        nama =input("masukkan nama anda:")
        print(rute[3], "=Rp", harga_tiket[3])
        harga_pilihan = harga_tiket[3]
        tujuan =rute[3]
    else:
        print("rute tidak tersedia")
        exit()
    berapa_tiket = int(input("berapa tiket?: "))
    total = harga_pilihan * berapa_tiket
    print("TOTAL TIKET YANG ANDA PESAN:","Rp",total)
    detail=input("apakah anda ingin melihat detail tiket anda? (ya/tidak):")
    if detail == "ya":
         print("======= DETAIL TIKET =======")
         print("NAMA:",nama)
         print("TUJUAN :",tujuan)
         print("JUMLAH TIKET:",berapa_tiket)
         print("HARGA TIKET:Rp.",harga_pilihan)
         print("TOTAL PEMBAYARAN:Rp.",total)
         print("===========================")
         print("TERIMAKASIH SELAMAT MENIKMATI PERJALANAN")
    if detail == "tidak":
        print("TRANSAKSI SELESAI HATI HATI DI JALAN")
    else :
        print()
        exit()

    print("TERIMAKASIH SELAMAT MENIKMATI PERJALANAN")