import os
import time

def menu():
    print("\n--- ALAT PEMANTAU KEAMANAN ---")
    print("1. Cek Koneksi Internet")
    print("2. Lihat Info Sistem/Perangkat")
    print("3. Cek Folder/File yang Ada")
    print("4. Keluar")

while True:
    menu()
    pilihan = input("\nPilih menu (1-4): ")

    if pilihan == "1":
        print("\nMengecek koneksi...")
        os.system("ping -c 3 google.com")
    elif pilihan == "2":
        print("\nInformasi Perangkat:")
        os.system("uname -a")
    elif pilihan == "3":
        print("\nDaftar file:")
        os.system("ls -l")
    elif pilihan == "4":
        print("Keluar...")
        break
    else:
        print("Pilihan tidak ada!")
    
    time.sleep(1)
