import getpass
class Atm:
    def pilih_menu():
        saldo = 10000000
        print("="*52)
        print("\t\tATM BERSAMA")
        print("\tJl. S Parman No. 14 Balikpapan Tengah")
        print("\t\ttelp.0542-48215")
        print("====================MENU PILIHAN====================")
        print("[1] Informasi Saldo")
        print("[2] Bayar")
        print("[3] Transfer")
        print("[4] Ambil Uang")
        print("[5] Keluar Apk")
        print("="*52)
        pilih =  int(input("Masukkan Menu Pilihan [1/2/3/4/5]: "))
        if(pilih == 1):
            n = 1
            while( n == 1):
                print("Menu: INFORMASI SALDO")
                print("Informasi Rekening Tabungan")
                print("Informasi Giro")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    Atm.pilih_menu()
                    continue
        elif(pilih == 2):
            n = 1
            while( n == 1):
                print("Menu: BAYAR")
                print("[1] BPJS\t   [3] PDAM")
                print("[2] PLN\t    [4] PULSA PASCABAYAR")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    Atm.pilih_menu()
                    continue
        elif(pilih == 3):
            n = 1
            while( n == 1):
                print("Menu: TRANSFER")
                print("[1] Transfer Antar Bank")
                print("[2] Transfer Sesama Bank")
                kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    Atm.pilih_menu()
                    continue
        elif(pilih == 4):
            n = 1
            while( n == 1):
                print("Menu: AMBIL UANG")
                print("[1] Rp. 1.000.000,-")
                print("[2] Rp. 500.000,-")
                print("[3] Rp. 300.000,-")
                print("[4] Nominal Lain")
                print("="*52)
                ambil = int(input("Masukkan nilai uang yang akan diambil[1/2/3/4]"))
                uang1 = 1000000
                uang2 = 500000
                uang3 = 300000
                if(ambil == 1):
                    saldo = saldo - uang1
                    print('Sisa Saldo :',saldo)
                    print('Status : Penarikan Berhasil')
                    kembali = input("Masukkan Transaksi Baru [y/t]:")
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                elif(ambil == 2):
                    saldo = saldo - uang2
                    print('Sisa Saldo :',saldo)
                    print('Status : Penarikan Berhasil')
                    kembali = input("Masukkan Transaksi Baru [y/t]:")
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                elif(ambil == 3):
                    saldo = saldo - uang3
                    print('Sisa Saldo :',saldo)
                    print('Status : Penarikan Berhasil')
                    kembali = input("Masukkan Transaksi Baru [y/t]:")
                    if((kembali == "y") or (kembali == "Y")):
                        Atm.pilih_menu()
                        continue
                elif(ambil == 4):
                    uanglain = int(input("Masukkan Nominal uang yang diambil: Rp."))
                    if(saldo >= uanglain):
                        saldo = saldo - uanglain
                        print('Sisa Saldo :',saldo)
                        print('Status : Penarikan Berhasil')
                    else :
                        print("Sorry Saldo Anda Tidak cukup")
                        kembali = input("Masukkan Transaksi Lagi [y/t]: ")
                if((kembali == "y") or (kembali == "Y")):
                    Atm.pilih_menu()
                    continue 
                    
        elif(pilih == 5):
            print("Thank You silakan ambil kartu anda")
            exit()   
            
            
def menu_utama():  
    pin= "12345" 
    print("="*52)
    print("\t\tATM BERSAMA")
    print("\tJl. S Parman No. 14 Balikpapan Tengah")
    print("\t\ttelp.0542-48215")
    print("====================MENU PILIHAN====================")
    for i in range(3) :
        sandi = getpass.getpass("Masukkan PIN\t: ")
        if(sandi == pin):
            Atm.pilih_menu()
        else :
            print("Pin Anda Salah")
            if i == 2 :
                print("Anda telah melukukan 3x percobaan")
                print("Kartu ATM Terblokir")
                exit()
menu_utama()
# Atm.pilih_menu()
        