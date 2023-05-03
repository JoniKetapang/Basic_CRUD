# database_utama
database = {
    'Id Barang' : [101,102,103,104,105],
    'Nama Barang' : ['Kursi', 'Chitoto', 'Televisi', 'Kemeja', 'Laptop'],
    'Jenis Barang' : ['Perabot', 'Kudapan', 'Elektronik', 'Pakaian', 'Elektronik'],
    'Kuantitas' : [5,7,8,25,10],
    'Lokasi Gudang' : ['Jakarta', 'Jakarta', 'Bekasi', 'Tangerang', 'Bekasi']
    } 

#buat rujukan List dalam Dictionary untuk mempermudah pengerjaan selanjutnya
IDbarang = database['Id Barang']
NamaBarang = database['Nama Barang']
JenisBarang = database['Jenis Barang']
LokasiGudang = database['Lokasi Gudang']
QtyBarang = database['Kuantitas']
#Jenis-jenis barang
RJB = ['Perabot','Kudapan','Elektronik','Pakaian']

import copy

# Menu satu #
# Menampilkan data tersedia #
def menusatu1():
    #print key dalam dictionary sebagai baris penunjuk
    print ()
    for keyDB in range(len(database)):
    # ^ memberikan penomoran pada list yang akan dikerjakan di bawah
        print (list(database.keys())[keyDB], end='\t|')
         # ^ database.keys diubah ke dalam bentuk list agar komand (.keys) dapat dioperasikan
    print()
    for angka in range(0,81):
        print ('=', end = '')
    print ()

    #print value sebagai isi tabel
    for a in range(len(list(database.values())[0])):
    # ^ memberikan penomoran pada list dalam dictionary yang akan dikerjakan
        for b in database:
        # ^ me-loop dictionary
            if len(str(database[b][a])) >= 7:
                print (database[b][a], end = '\t|')
                # ^ [b] merujuk pada keys yang sedang diproses, sedangkan [a] merujuk pada urutan dalam list 
            else:
                print (database[b][a], end = '\t\t|')
        print()
        # ^ untuk meng-enter tiapnomor pada list keys
    for angka in range(0,81):
        print ('=', end = '')
    print ()

def menusatu2():
    while True:
        idcari = input('Masukkan Id barang yang ingin ditampilkan: ')
        # ^ masukkan nama barang yang ingin ditampilkan
        if int(idcari) in IDbarang:
        # ^ mengecek ketersediaan nama barang dalam list
        ### MASALAH UTAMA: tidak bisa menampilkan 2 barang dengan nama yang sama ###
            idcari1 = IDbarang.index(int(idcari))
            print ()
            for keyDB in range(len(database)):
                print (list(database.keys())[keyDB], end='\t|')
            print()
            for angka in range(0,81):
                print ('=', end = '')
            print ()
            for barspes in database:
                if len(str(database[barspes][idcari1])) >=7:
                    print (database[barspes][idcari1], end='\t|')
                else:
                    print (database[barspes][idcari1], end='\t\t|')
            print()
            break
        else:
            batalcari = (input('Barang tidak terdapat dalam database.\nApakah ingin mencari yang lain? (Ya/Tidak)\n').capitalize())
            # ^ berikan opsi kembali ke menu utama (untuk mengecek database keseluruhan, misalnya)
            if batalcari == 'Ya':
                continue
            else:
                break
# Menu dua #
# Menambahkan data #
def menudua(): 
    while True: 
        DummyList1 = []
        # ^ buat list kosong untuk tampilan konfirmasi
        # input ID, Nama, Jenis, Kuantitas barang baru
        while True:
            # memastikan tidak ada double ID
            IDBarBar = (int(input('Masukkan ID Barang: ')))
            if IDBarBar in IDbarang:
                print ('ID terpakai! Harap masukkan nomor lainnya')
                continue
            # memastikan ID berupa 3 angka
            elif len(str(IDBarBar)) != 3:
                print ('Harap masukkan tiga digit angka!')
                continue
            else:
                DummyList1.append(IDBarBar)
                break
        NamBarBar = (input('Masukkan Nama Barang: ').capitalize())
        DummyList1.append(NamBarBar)
        while True:
            # memastikan jenis barang tersedia
            JenBarBar = (input ('Masukkan Jenis Barang: ').capitalize())
            if JenBarBar in RJB:
                DummyList1.append(JenBarBar)
                break
            else: 
                print (f"Jenis barang tidak tersedia!\nPastikan anda memasukkan salah satu dari {RJB}")
                continue
        QtyBarBar = int(input ('Masukkan Kuantitas Barang: '))
        DummyList1.append(QtyBarBar)
        LokGudBar = []
        # ^ list kosong untuk lokasi karena di sini lokasi sifatnya dependen
        if JenBarBar == 'Perabot':
            LokGudBar.append('Jakarta')
        elif JenBarBar == 'Kudapan':
            LokGudBar.append('Jakarta')
        elif JenBarBar == 'Elektronik':
            LokGudBar.append('Bekasi')
        elif JenBarBar == 'Pakaian':
            LokGudBar.append('Tangerang')
        DummyList2 = DummyList1 + LokGudBar
        # ^ membuat list baru yang menggabungkan kompilasi data dengan data lokasi gudang
        print ()
        for keyDB in range(len(database)):
            print (list(database.keys())[keyDB], end='\t|')
        print()
        for apapun in range(0,81):
            print ('=', end = '')
        print ()
        for BarBar in DummyList2:
            if len(str(BarBar)) >= 7:
                print (BarBar, end='\t|')
            else: 
                print (BarBar, end='\t\t|')
        print ()
        pastikan = (input('Apakah data di atas sudah benar? (Ya/Tidak) \n').capitalize())
        if pastikan == 'Ya':
            IDbarang.append(IDBarBar)
            NamaBarang.append(NamBarBar)
            JenisBarang.append(JenBarBar)
            QtyBarang.append(QtyBarBar)
            # ^ semua data dimasukkan ke dalam list awal
            LokasiGudang.extend(LokGudBar)
            # ^ gunakan (.extend) sebab LokGudBar merupakan list
            print()
            print ('Data berhasil ditambahkan...')
            print()
            break
        elif pastikan == 'Tidak':
            continue

# menu tiga #
# mengupdate data #
def menutiga():
    while True:
        while True:
            BarUp = input('Masukkan ID Barang dari barang yang datanya akan dirubah: ')
            if BarUp.isnumeric():
                pass
            else:
                print ('Harap masukkan angka!')
                continue
            if int(BarUp) in IDbarang:
                BarUp1 = IDbarang.index(int(BarUp))
                BarUp1 = IDbarang.index(int(BarUp))
                for keyDB in range(len(database)):
                    print (list(database.keys())[keyDB], end='\t|')
                print()
                for angka in range(0,81):
                    print ('=', end = '')
                print()
                for b in database:
                    if len(str(database[b][BarUp1])) >= 7:
                        print (database[b][BarUp1], end = '\t|')
                    else:
                        print (database[b][BarUp1], end = '\t\t|')
                print()
                pastikan2 = (input('Apakah data di atas yang ingin dirubah? (Ya/Tidak) ').capitalize())
                if pastikan2 == 'Ya':
                    print ('Melanjutkan proses...')
                    break
                else:
                    continue
            else:
                print ('ID Barang tidak tersedia!')
        while True:
            BagianUpdate = (input('Masukkan kolom data yang ingin dirubah: ').title())
            # (.title) sebab ada kolom yang lebih dari satu kata
            if BagianUpdate in database and BagianUpdate != 'Lokasi Gudang' and BagianUpdate != 'Id Barang':
                break
            elif BagianUpdate == 'Lokasi Gudang':
                print ('Lokasi Gudang tidak dapat dirubah!')
                continue
            elif BagianUpdate == 'Id Barang':
                print ('Id Barang tidak dapat dirubah!')
            else:
                print (f'Harap masukkan data sesuai kolom yang tersedia!\nPilihan kolom adalah: {list(database.keys())[1:4]}')
                continue
        while True:
            perubahandata = input('Masukkan nilai terbaru: ')
            if BagianUpdate == 'Kuantitas' and perubahandata.isalpha():
                print ('Harap masukkan angka!')
                continue
            elif BagianUpdate == 'Jenis Barang' and perubahandata.capitalize() not in RJB:
                print (f'Jenis Barang tidak teridentifikasi\nPastikan jenis barang termasuk dalam kategori berikut\nkategori barang: {RJB}')
                continue
            else:
                break
        if perubahandata.isnumeric():
            perubahandata = (int(perubahandata))
        elif perubahandata.isalpha():
            perubahandata = (perubahandata.title())
        database[BagianUpdate][BarUp1] = perubahandata
        if BagianUpdate == 'Jenis Barang' and perubahandata == 'Perabot':
            LokasiGudang[BarUp1] = 'Jakarta'
        elif BagianUpdate == 'Jenis Barang' and perubahandata == 'Kudapan':
            LokasiGudang[BarUp1] = 'Jakarta'
        elif BagianUpdate == 'Jenis Barang' and perubahandata == 'Elektronik':
            LokasiGudang[BarUp1] = 'Bekasi'
        elif BagianUpdate == 'Jenis Barang' and perubahandata == 'Pakaian':
            LokasiGudang[BarUp1] = 'Tangerang'
        konfirmasi = (input('Apakah ada lagi yang ingin dirubah? (Ya/Tidak)\n').capitalize())
        if konfirmasi == 'Ya':
            continue
        else:
            break

# menu empat #
# menghapus data #
def menuempat1():
    # menghapus data menggunakan nama barang #
    while True:
        while True:
            NamaHapus = (input('Masukkan nama barang yang ingin dihapus: ').capitalize())
            if NamaHapus in NamaBarang:
                NamaHapus1 = NamaBarang.index(NamaHapus)
                break
            else:
                continue
        print ()
        for keyDB in range(len(database)):
                print (list(database.keys())[keyDB], end='\t|')
        print()
        for apapun in range(0,81):
            print ('=', end = '')
        print ()
        for b in database:
            if len(str(database[b][NamaHapus1])) >= 7:
                print (database[b][NamaHapus1], end = '\t|')
            else:
                print (database[b][NamaHapus1], end = '\t\t|')
        print()
        pastikan2 = (input('Apakah data di atas yang ingin dihapus? (Ya/Tidak) ').capitalize())
        if pastikan2 == 'Ya':
           print('Menghapus data...\nKembali ke menu utama...')
           for IBarHap in database:
               del database[IBarHap][NamaHapus1]
           break
        elif pastikan2 == 'Tidak':
            pastikan2a = (input('Apakah anda masih ingin menghapus data? (Ya/Tidak)\n').capitalize())
            if pastikan2a == 'Ya':
                continue
            else:
                break

def menuempat2():
    # menghapus data menggunakan id barang #
    while True:
        while True:
            IDHapus = (input('Masukkan ID barang yang ingin dihapus: '))
            if IDHapus.isnumeric():
                pass
            else: 
                print ('Harap masukkan angka!')
                continue

            if int(IDHapus) in IDbarang:
                break
            else:
                print ('Tidak terdapat ID yang diinginkan')
                continue
        IDHapus1 = IDbarang.index(int(IDHapus))
        print ()
        for keyDB in range(len(database)):
                print (list(database.keys())[keyDB], end='\t|')
        print()
        for apapun in range(0,81):
            print ('=', end = '')
        print ()
        for b in database:
            if len(str(database[b][IDHapus1])) >= 7:
                print (database[b][IDHapus1], end = '\t|')
            else:
                print (database[b][IDHapus1], end = '\t\t|')
        print()
        pastikan2 = (input('Apakah data di atas yang ingin dihapus? (Ya/Tidak) ').capitalize())
        if pastikan2 == 'Ya':
           print ('Menghapus data...\nKembali ke menu utama...')
           for IBarHap in database:
               del database[IBarHap][IDHapus1]
           break
        elif pastikan2 == 'Tidak':
            pastikan2a = (input('Apakah anda masih ingin menghapus data? (Ya/Tidak)\n').capitalize())
            if pastikan2a == 'Ya':
                continue
            else:
                break

# menu lima #
# mengeluarkan dan memasukkan stock dari gudang #
def menulima1():
    while True:
        IDBarKel = (input('Masukkan ID Barang yang akan dikeluarkan: '))
        if IDBarKel.isnumeric():
            pass
        else: 
            print ('Harap masukkan angka!')
            continue
    
        if int(IDBarKel) in IDbarang:
            IDBarKel1 = IDbarang.index(int(IDBarKel))
            # ^ menambahkan (int) karena inputan bersifat string
            for keyDB in range(len(database)):
                print (list(database.keys())[keyDB], end='\t|')
            print()
            for angka in range(0,81):
                print ('=', end = '')
            print()
            for b in database:
                if len(str(database[b][IDBarKel1])) >= 7:
                    print (database[b][IDBarKel1], end = '\t|')
                else:
                    print (database[b][IDBarKel1], end = '\t\t|')
            print()
            pastikanBarkel = (input('Apakah data di atas yang ingin dikeluarkan? (Ya/Tidak) ').capitalize())
            if pastikanBarkel == 'Ya':
                break
            else:
                continue
        else:
            print ('ID Barang tidak tersedia!')
            continue
    while True:
        QtyBarKel = (input('Masukkan jumlah barang yang akan dikeluarkan: '))
        if QtyBarKel.isnumeric():
            pass
        else: 
            print ('Harap masukkan angka!')
            continue
        if int(QtyBarKel) > QtyBarang[IDBarKel1]:
            print ('Kuantitas barang tersisa tidak mencukupi permintaan\nHarap masukkan jumlah yang sesuai')
            continue
        elif int(QtyBarKel) < QtyBarang[IDBarKel1] or int(QtyBarKel) == QtyBarang[IDBarKel1]:
            QtyBarang[IDBarKel1] = QtyBarang[IDBarKel1]-int(QtyBarKel)
            print()
            print ('Barang dikeluarkan\nmengupdate data...')
            print()
            break

def menulima2():
    while True:
        IDBarMas = (input('Masukkan ID Barang yang akan dimasukkan: '))
        if IDBarMas.isnumeric():
            pass
        else: 
            print ('Harap masukkan angka!')
            continue
        if int(IDBarMas) in IDbarang:
            IDBarMas1 = IDbarang.index(int(IDBarMas))
            # ^ menambahkan (int) karena inputan bersifat string
            for keyDB in range(len(database)):
                print (list(database.keys())[keyDB], end='\t|')
            print()
            for angka in range(0,81):
                print ('=', end = '')
            print()
            for b in database:
                if len(str(database[b][IDBarMas1])) >= 7:
                    print (database[b][IDBarMas1], end = '\t|')
                else:
                    print (database[b][IDBarMas1], end = '\t\t|')
            print()
            pastikanBarMas = (input('Apakah data di atas yang ingin dikeluarkan? (Ya/Tidak) ').capitalize())
            if pastikanBarMas == 'Ya':
                break
            else:
                continue
        else:
            print ('ID Barang tidak tersedia!')
            continue
    while True:
        QtyBarMas = input('Masukkan jumlah barang yang akan dimasukkan: ')
        if QtyBarMas.isnumeric():
            break
        else: 
            print ('Harap masukkan angka!')
            continue
    QtyBarang[IDBarMas1] = QtyBarang[IDBarMas1]+int(QtyBarMas)
    print()
    print ('Barang dimasukkan\nmengupdate data...')
    print()

# program utama #
while True:
    print ('Gudang Barang Kylian Mbappe\n1. Tampilkan data\n2. Tambahkan Data\n3. Ubah Data\n4. Hapus Data\n5. Mengeluarkan atau memasukkan barang \n6. Keluar Program')
    x = (input('Pilih menu yang ingin digunakan!\nmasukkan angka menu: '))
    if x == '1':
        while True:
            pilihanlanjutan1 = input('1. Tampilkan data secara keseluruhan\n2. Tampilkan data barang spesifik\n3. Batal menggunakan menu\nMasukkan angka menu: ')
            if pilihanlanjutan1 == '1':
                menusatu1()
                break
            elif pilihanlanjutan1 == '2':
                menusatu2()
                break
            elif pilihanlanjutan1 == '3':
                break
            else:
                print()
                print ('Harap masukkan menu yang tersedia!')
                print()
                continue
        tambahanmenusatu = (input('Apakah anda ingin menggunakan menu yang lain? (Ya/Tidak)\n').capitalize())
        if tambahanmenusatu == 'Ya':
            print()
            continue
        elif tambahanmenusatu == 'Tidak':
            print()
            print ('Menonaktifkan aplikasi...\nSampai jumpa kembali...') 
            break
    elif x == '2':
        while True:
            print ('Menu Menambah Data\n1. Lanjut Menambah data\n2. Kembali ke menu utama')
            menudualanjut = input ('Masukkan menu pilihan: ')
            if menudualanjut == '1':
                menudua()
                while True:
                    print ('Masukkan input angka atau huruf untuk kembali ke menu penambahan data')
                    menudualanjut2 = input()
                    if menudualanjut2.isalnum():
                        break
                    else:
                        break
            elif menudualanjut == '2':
                break
            else:
                print ('Harap masukkan pilihan yang tersedia!')
                continue
    elif x == '3':
        while True: 
            tigakontinu = (input('1. Lanjut ubah data\n2. Kembali ke menu utama\n'))
            if tigakontinu == '1':
                menutiga()
                break
            elif tigakontinu == '2':
                break
            else:
                print ('Inputan salah. Harap masukkan menu yang tersedia!\n')
                continue 
    elif x == '4':
        while True:
            print ('1. Hapus berdasarkan ID Barang\n2. Hapur berdasarkan Nama Barang\n3. Kembali ke menu utama')
            empatlanjutan = (input('Masukkan menu yang diinginkan: '))
            if empatlanjutan == '1':
                menuempat2()
                break
            elif empatlanjutan == '2':
                menuempat1()
                break
            elif empatlanjutan == '3':
                break
            else:
                print ('Harap masukkan menu dari pilihan yang tersedia!')
                continue
    elif x == '5':
        while True:
            print ('1. Mengeluarkan barang\n2. Memasukkan barang\n3. Kembali ke menu utama')
            limalanjutan = (input('Masukkan menu yang diinginkan: '))
            if limalanjutan == '1':
                menulima1()
                while True:
                    print ('Masukkan input angka atau huruf untuk kembali ke menu penambahan data')
                    limalanjutan2 = input()
                    if limalanjutan2.isalnum():
                        break
                    else:
                        break
            elif limalanjutan == '2':
                menulima2()
                while True:
                    print ('Masukkan input angka atau huruf untuk kembali ke menu penambahan data')
                    limalanjutan3 = input()
                    if limalanjutan3.isalnum():
                        break
                    else:
                        break
            elif limalanjutan == '3':
                break
            else:
                print('Harap masukkan menu yang tersedia!')
                continue
    elif x == '6':
        print ('Menonaktifkan aplikasi...\nSampai jumpa kembali...')
        break
    else:
        print ()
        print ('Harap masukkan angka menu yang tersedia!')
        print()
        continue
    