class kendaraan_darat:
    def __init__(self,tahunKeluaran,nama,warna,kecepatan,bahanBakar,jumlahRoda,kapasitasPenumpang):
        self.tahun_Keluaran = tahunKeluaran
        self.Nama = nama
        self.Warna = warna
        self.Kecepatan = kecepatan
        self.bahan_Bakar = bahanBakar
        self.jumlah_Roda = jumlahRoda
        self.kapasitas_Penumpang = kapasitasPenumpang

class kereta(kendaraan_darat):
    def __init__(self, tahunKeluaran, nama, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang,jenisGerbong,jumlahKursi,jenisLayananKereta,Rute):
        super().__init__(tahunKeluaran,nama,warna,kecepatan,bahanBakar,jumlahRoda,kapasitasPenumpang)
        self.jenis_Gerbong = jenisGerbong
        self.jumlah_Kursi = jumlahKursi
        self.jenis_LayananKereta = jenisLayananKereta
        self.rute = Rute

    def tambahRute(self):
        ruteBaru = input("Masukkan Rute Baru: ")
        self.rute=ruteBaru
        print(f"Rute baru {ruteBaru} telah ditambahkan!!!")
        return ruteBaru
        
    def kurangiRute(self):
        ruteHapus = input("Masukkan Rute yang Ingin Dihapus: ")
        if ruteHapus in self.rute:
            self.rute = self.rute.replace(ruteHapus, "").strip()
            print(f"Rute {ruteHapus} telah dihapus!!!")
        else:
            print(f"Rute {ruteHapus} tidak ditemukan !!!")
        

    # def kurangiRute(self):
    #     ruteHapus = input("Masukkan Rute yang Ingin Dihapus: ")
    #     self.rute=ruteHapus
    #     self.rute.(ruteHapus)
    #     print(f"Rute {ruteHapus} telah dihapus!!!")
    
        

class mobil(kendaraan_darat):
    def __init__(self, tahunKeluaran, nama, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang,jenisMobil):
        super().__init__(tahunKeluaran,nama,warna,kecepatan,bahanBakar,jumlahRoda,kapasitasPenumpang)
        self.jenis_Mobil = jenisMobil

    def startEngine():
        print("Mesin Mobil  Dinyalakan")

    def stopEngine():
        print("Mesin Dimatikan")

    def maju():
        print("Mobil Bergerak Maju")

    def mundur():
        print("Mobil Bergerak Mundur")

    def belok():
        print("Mobil Bergerak Belok")

class mobilBalap(mobil):
    def __init__(self, tahunKeluaran, nama, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil,frontWing,rearWing):
        super().__init__(tahunKeluaran,nama,warna,kecepatan,bahanBakar,jumlahRoda,kapasitasPenumpang,jenisMobil)
        self.front_Wing = frontWing
        self.rear_Wing = rearWing

    def race():
        print("Mobil Sedang Melangsungkan Balapan")

class mobilCrossroad(mobil):
    def __init__(self, tahunKeluaran, nama, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil,sunroopType,shockBreaker):
        super().__init__(tahunKeluaran, nama, warna, kecepatan, bahanBakar, jumlahRoda, kapasitasPenumpang, jenisMobil)
        self.sunroop_type = sunroopType
        self.shock_breaker = shockBreaker

    def sunroofTerbuka():
        print("======>Sunroof Terbuka<=======")
        

    def sunroofTertutup():
        print("======>Sunroof Tertutup<======")
        


def menu1():
    print("""Jenis-Jenis Kereta
            1.KAAJ
            2.MRT""")
    pilih = input("Masukkan Jenis kereta :")
    if pilih == "1":
        print("")
        kereta1 = kereta(2002,"JogloSemar","putih", "120 km/jam", "Batu Bara", "12 Roda", 100, "Gerbong Terbuka", 100,"Eksekutif", "Jogja-semarang" )
        print("======>Info Tentang Kereta<======")
        print(' Tahun keluaran = ',kereta1.tahun_Keluaran,)
        print(' Nama kereta = ',kereta1.Nama,)
        print(' Warna kereta = ',kereta1.Warna,)
        print(' Kecepatan kereta = ',kereta1.Kecepatan,)
        print(' Bahan bakar kereta = ',kereta1.bahan_Bakar,)
        print(' Jumlah roda = ',kereta1.jumlah_Roda,)
        print(' Kapasitas penumpang = ',kereta1.kapasitas_Penumpang,)
        print(' Jenis gerbong = ',kereta1.jenis_Gerbong,)
        print(' Jumlah kursi penumpang = ',kereta1.jumlah_Kursi,)
        print(' Jenis layanan kereta = ',kereta1.jenis_LayananKereta,)
        print(' Rute kereta = ',kereta1.rute)
        print("")
        tanya = input("Apakah Anda Ingin Menambahkan / mengurangi Rute  (y/n):")
        if tanya == 'y':
            print('Rute kereta = ',kereta1.rute,kereta1.tambahRute())
            pilih2 = (input("apakah anda ingin menhapus rute y/n: "))
            if pilih2 == "y":
                print(kereta1.kurangiRute())
            elif tanya == "n":
                print("Anda Memilih Untuk Tidak Mengurangi")
            else:
                print("pilihan tidak tersedia")
        else:
            print("Pilihan tidak tersedia!!!")
            
    elif pilih == "2":
        print("")
        kereta1 = kereta(2002,"Kerta Exspress","hitam", "120 km/jam", "Listrik", "12 Roda", 200, "Gerbong Tertutup", 200,"biasa", "Bandara Kota" )
        print("======>Info Tentang Kereta<======")
        print(' Tahun keluaran = ',kereta1.tahun_Keluaran,)
        print(' Nama kereta = ',kereta1.Nama,)
        print(' Warna kereta = ',kereta1.Warna,)
        print(' Kecepatan kereta = ',kereta1.Kecepatan,)
        print(' Bahan bakar kereta = ',kereta1.bahan_Bakar,)
        print(' Jumlah roda = ',kereta1.jumlah_Roda,)
        print(' Kapasitas penumpang = ',kereta1.kapasitas_Penumpang,)
        print(' Jenis gerbong = ',kereta1.jenis_Gerbong,)
        print(' Jumlah kursi penumpang = ',kereta1.jumlah_Kursi,)
        print(' Jenis layanan kereta = ',kereta1.jenis_LayananKereta,)
        print(' Rute kereta = ',kereta1.rute)
        print("")
        tanya = input("Apakah Anda Ingin Menambahkan / mengurangi Rute  (y/n):")
        if tanya == 'y':
            if tanya == 'y':
                print('Rute kereta = ',kereta1.rute,kereta1.tambahRute())

                pilih2 = (input("apakah anda ingin menhapus rute y/n: "))
                if pilih2 == "y":
                    print(kereta1.kurangiRute())
                elif tanya == "n":
                    print("Anda Memilih Untuk Tidak Mengurangi")
                else:
                    print("pilihan tidak tersedia")
        else:
            print("Pilihan tidak tersedia!!!")

        
def sunroop():
    fitur = input("Apakah anda ingin membuka sunroof (y/n):")
    if fitur == "y":
        print("")
        mobilCrossroad.sunroofTerbuka()
        print("")
        fiturr = input("Apakah anda ingin menutup sunroof (y/n):")
        if fiturr == "y":
            print("")
            mobilCrossroad.sunroofTertutup()
        
        elif fitur == "n":
            print ("Sunroof Tidak di buka")
        else:
            print("Menu tidak tersedia")

    elif fitur == "n":
        print ("Sunroof Tidak di buka")
    else:
        print("Menu tidak tersedia")
    
def nyalaMobil():
        tanya= input ("apakah anda ingin mengunakan mobil (y/n):")
        if tanya =="y":
            print("""Apa yang ingin anda lakukan:
                1. Menyalakan mobil
                2. Mematikan mobil
                3. Memajukan mobil
                4. Memundurkan mobil
                5. Membelokkan mobil
                6. Balapan""")
            pilih2=int(input("Masukkan pilihan anda : "))
            if pilih2 == 1:
                mobil.startEngine()
            elif pilih2== 2:
                mobil.stopEngine()
            elif pilih2 == 3:
                mobil.maju()
            elif pilih2 == 4:
                mobil.mundur()
            elif pilih2 == 5:
                mobil.belok()
            elif pilih2 == 6:
                mobilBalap.race()
            else:
                print("Menu tidak tersedia")
        elif tanya == "n":
            print("Anda Memilih Untuk Tidak Menggunakan Mobil")
        else:
            print("Menu tidak tersedia")

def menu2():
    print("""Jenis-Jenis Mobil
            1. Mobil Balap
            2. Mobil Crossroad""")
    pilih = input("Masukkan Jenis Mobil :")
    
    if pilih =="1":
        y=mobilBalap(2022,"Lamborghini","Biru", '311 km/jam',"Bensin",0,0, "Mobil Balap","Front Wing", "Rear Wing")
        print("Jenis Mobil adalah :", y.jenis_Mobil)

        print("---- More Info ----")
        print(' Tahun keluaran mobil = ',y.tahun_Keluaran,)
        print(' Nama mobil= ',y.Nama,)
        print(' Warna mobil = ',y.Warna,)
        print(' Kecepatan mobil= ',y.Kecepatan,)
        print(' Bahan bakar mobil = ',y.bahan_Bakar,)
        print(' Memiliki Sayap Depan = ',y.front_Wing, "Dan  Sayap Belakang",y.rear_Wing)
        print("")
        nyalaMobil()

    elif pilih == "2":
        y=mobilCrossroad(2022,"Honda Cross Road","merah", '311 km/jam',"Bensin",0,0, "Mobil Croos Road","Sunroop","Shock Breaker")
        print("Jenis Mobil adalah :", y.jenis_Mobil)

        print("---- More Info ----")
        print(' Tahun keluaran mobil = ',y.tahun_Keluaran,)
        print(' Nama mobil = ',y.Nama,)
        print(' Warna mobil = ',y.Warna,)
        print(' Kecepatan mobil = ',y.Kecepatan,)
        print(' Bahan bakar mobil = ',y.bahan_Bakar,)
        print(' Fitur Tambahan Pada Mobil adalah = ',y.sunroop_type,"dan", y.shock_breaker)

        print("")
        tanya= input ("apakah anda ingin mengunakan mobil (y/n):")
        if tanya =="y":
            print("""Apa yang ingin anda lakukan:
                1. Menyalakan mobil
                2. Mematikan mobil
                3. Memajukan mobil
                4. Memundurkan mobil
                5. Membelokkan mobil
                """)
            pilih2=int(input("Masukkan pilihan anda : "))
            if pilih2 == 1:
                mobil.startEngine()
            elif pilih2== 2:
                mobil.stopEngine()
                
            elif pilih2 == 3:
                mobil.maju()
                sunroop()

            elif pilih2 == 4:
                mobil.mundur()
                sunroop()

            elif pilih2 == 5:
                mobil.belok()
                sunroop()

            else:
                print("menu tidak tersedia")
        elif tanya == "n":
            print("Anda Memilih Untuk Tidak Menggunakan Mobil")
        else:
            print("menu tidak tersedia")
            

while True:
    print("")
    print(""" Pilih kendaraan terlebih dahulu :
            1. Kereta
            2. Mobil
            0. Keluar""")
    pilih = int(input("masukkan pilihan anda: "))
    if pilih == 1:
        menu1()
    elif pilih == 2 :
        menu2()
    elif pilih == 0 :
        exit('Anda telah keluar')


