from prettytable import PrettyTable

# data untuk login admin
nama_admin = "admin"
password_admin = "admin123"

# databases sederhana untuk properti yang sudah disediakan (biar ada aja)
properti = {
    "P01": {
        "Jenis": "Bangunan",
        "Nama": "Rumah James Bond 007",
        "Harga Sewa per Hari": "190.000.000",
        "Status": "Disewa"
    },
    "P02": {
        "Jenis": "Bangunan",
        "Nama": "Rumah Diddy 69",
        "Harga Sewa per Hari": "250.000.000",
        "Status": "Tersedia"
    },
    "P03": {
        "Jenis": "Kendaraan",
        "Nama": "Porsche 918 Spyder",
        "Harga Sewa per Hari": "90.000.000",
        "Status": "Disewa"
    },
    "P05": {
        "Jenis": "Bangunan",
        "Nama": "Wite House",
        "Harga Sewa per Hari": "500.000.000",
        "Status": "Tersedia"
    },
    "P06": {
        "Jenis": "Kendaraan",
        "Nama": "Koenigsegg Jesko",
        "Harga Sewa per Hari": "105.000.000",
        "Status": "Tersedia"
    },
    "P07": {
        "Jenis": "Bangunan",
        "Nama": "Astroworld Studio",
        "Harga Sewa per Hari": "390.000.000",
        "Status": "Disewa"
    }
}

# fungsi buat admin biar bisa nambahin properti
def admin_tambah():
    admin_penyewa_liat()
    while True:
        nomor_properti = input("Masukkan Nomor Properti : ") # nasukin nomor properti
        jenis = input("Masukkan Jenis Properti (Kendaraan/Bangunan) : ") # masukin jenis properti
        nama = input("Masukkan Nama Properti : ") # masukin harga properti
        harga = input("Masukkan Harga Sewa per Hari : ") # masukin harga properti
        status = "Tersedia" # ntar abis ditambahin langsung tersedia
        
        properti[nomor_properti] = {
            "Jenis": jenis,
            "Nama": nama,
            "Harga Sewa per Hari": harga,
            "Status": status
        }
        print("Properti berhasil ditambahkan!")
        
        pilihan = input("Apakah Ingin Menambahkan Properti Lagi? (Y/N) : ")
        if pilihan == "Y":
            continue
        else:
            break
            
# fungsi buat admin mau hapus properti apa ndak
def admin_hapus():
    admin_penyewa_liat()
    nomor_properti = input("Masukkan Nomor Properti Yang Ingin Dihapus : ") 
    if nomor_properti in properti:
        del properti[nomor_properti]
        print("Properti Berhasil Dihapus!") # otomatis properti tehapus
    else:
        print("Properti Gak Ada") 

# fungsi buat admin sama penyewa biar sama" bisa liat propertinya
def admin_penyewa_liat():
    if properti:
        table = PrettyTable() # masukin fungsi tabelnya
        table.field_names = ["Nomor", "Jenis", "Nama", "Harga Sewa per Hari", "Status"]
        
        for nomor_properti, data in properti.items():
            table.add_row([nomor_properti, data["Jenis"], data["Nama"], data["Harga Sewa per Hari"], data["Status"]])
        
        print(table) # buat munculin tabelnya
    else:
        print("Belum Ada Data Properti")

# fungsi buat ngedit/memperbarui propertinya
def admin_perbarui():
    admin_penyewa_liat()
    nomor_properti = input("Masukkan Nomor Properti yang ingin diperbarui: ")
    if nomor_properti in properti:
        jenis = input("Masukkan Jenis Properti (Kendaraan/Bangunan) : ")
        nama = input("Masukkan Nama Properti : ")
        harga = input("Masukkan Harga Sewa per Hari : ")
        status = input("Masukkan Status (Tersedia/Disewa): ")
        
        properti[nomor_properti] = {
            "Jenis": jenis,
            "Nama": nama,
            "Harga Sewa per Hari": harga,
            "Status": status
        }
        print("Properti Berhasil Diperbarui")
    else:
        print("Properti Gak Ada") 

# menu sewa buat si penyewa 
def menu_sewa():
    admin_penyewa_liat()
    nomor_properti = input("Masukkan Nomor Properti Yang Ingin Disewa : ")

    if nomor_properti in properti:
        if properti[nomor_properti]["Status"] == "Tersedia": # fungsi if semisal ada properti yang tersedia
            hari = int(input("Masukkan Jumlah Hari Menyewa : ")) # masukin jumlah hari untuk sewa properti
            harga_sewa = int(properti[nomor_properti]["Harga Sewa per Hari"].replace(".", ""))
            total_harga = harga_sewa * hari # perhitugan junlah hari sewa dengan harga sewa
            print(f"Total Harga Untuk {hari} Hari Adalah Rp {total_harga:,}") # total semua harga sewa
            konfirmasi = input("Apakah Anda Yakin? (Y/N) : ") # konfirmasi lanjut bayar atau tidak
            
            # proses yang terjadi kalau lanjut bayar
            if konfirmasi == "Y": 
                properti[nomor_properti]["Status"] = "Disewa"
                print(f"Properti {properti[nomor_properti]['Nama']} Berhasil Disewa Selama {hari} Hari.")
            # proses yang terjadi kalau tidak jadi bayar
            else:
                print("Proses Penyewaan Dibatalin") 
        else:
            print("Properti Dah Disewa") # proses yang terjadi kalau properti dah disewa duluan
    else:
        print("Properti Gak Ada") # properti gak ada di dictionary

# menu penyewa setelah login
def menu_penyewa():
    while True:
        print("=" * 10 + "PILIH MENU YANG INGIN DIGUNAKAN" + "=" * 10)
        print("[1]. Liat Properti") # pilihan buat liat properti
        print("[2]. Sewa Properti") # pilihan buat sewa properti
        print("[3]. Balik Menu Login") # balik menu login
        
        pilihan_user = (input("Pilih Menu Yang Pengen Digunakan : ")) # disuruh milih menu apa
        
        if pilihan_user == '1':
            admin_penyewa_liat()
        elif pilihan_user == '2':
            menu_sewa()
        elif pilihan_user == '3':
            login()
        else:
            print("Masukkan Angka Yang Bener")

# menu buat admin setelah login
def menu_admin():
    while True:
        print("=" * 10 + "PILIH MENU YANG INGIN DIGUNAKAN" + "=" * 10)
        print("[1]. Tambah Properti") # pilihan buat nambah properti
        print("[2]. Hapus Properti") # pilihan buat ngapus properti
        print("[3]. Liat Properti") # pilihan buat liat properti
        print("[4]. Perbarui Properti") # pilihan buat perbarui properti
        print("[5]. Balik Menu Login") # pilihan balik menu login

        pilihan_menu = input("Pilih Menu Yang Ingin Digunakan : ")
        
        if pilihan_menu == '1':
            admin_tambah()
        elif pilihan_menu == '2':
            admin_hapus()
        elif pilihan_menu == '3':
            admin_penyewa_liat()
        elif pilihan_menu == '4':
            admin_perbarui()
        elif pilihan_menu == '5':
            return login()
        else:
            print("Pilihan Gak Bener, Coba Lagi")

# fungsi buat login, ngebedain kriteria/menu buat admin dengan si penyewa
def login():
    # pemilihan role admin atau penyewa
    while True:
        print("=" * 10 + "SELAMAT DATANG DI PENYEWAAN PROPERTI PAK AMBA" + "=" * 10)
        print("Pilih Menu Dibawah")
        print("[1]. Admin")
        print("[2]. Penyewa")
        print("[3]. Keluar Program")
        pilihan = input("Masukkan Pilihan Anda : ")
        # role buat admin
        if pilihan == "1":
            nama = input("Masukkan Nama : ")
            password = input("Masukkan Password : ")
            if nama == nama_admin and password == password_admin:
                print("SELAMAT DATANG ADMIN")
                menu_admin()
            else:
                print("Nama atau Password Salah")
        # role buat penyewa
        elif pilihan == "2":
            nama_user = input("Masukkan Nama : ")
            password_user = input("Masukkan Password : ")
            print(f"SELAMAT DATANG {nama_user}")
            menu_penyewa()
            
        elif pilihan == "3":
            print("Makasih Dah Make")
            exit()
        
        else:
            print("Pilihan Salah. Coba Lagi")

# untuk memulai segalanya
login()