import os
import bs4
import sys
import requests
import time
import marshal
h = "\033[92m"
p = "\033[0m"
os.system('clear')
print("========================================\n" + p)
print("Author	:@RTIST(Maulana S.A)\n" + h)
print("Tools	: SANTET ONLINE (HAPUS DOSA)\n" + h)
print("========================================\n" + p)
print("Lanjut?[Y/N]")
y=raw_input()
if y=='Y' or y=='y':
    menu()
else:
    keluar()
def santet():
	os.system('clear')
	print("Nama Korban:")
	nama=raw_input()
	print("Usia Korban")
	usia=raw_input()
	print("Alamat Korban")
	alamat=raw_input()
	print("alasan Kenapa Lo Santet dia")
	alasan=raw_input()
	time.sleep(5)
	titik = ['.   ', '..  ', '... ']
for o in titik:
    print ("\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92m[!]Semoga Hari mu baik-baik saja \x1b[1;97m")
    sys.stdout.flush()
    time.sleep(1)
    print("\x1b[1;97m[!]\x1b[1;92mIBLIS MENUJU KORBAN!!!")
    time.sleep(1)
    print("\x1b[1;90m10%")
    time.sleep(2)
    print("\x1b[1;91m20%")
    time.sleep(3)
    print("\x1b[1;92m30%")
    time.sleep(4)
    print("\x1b[1;93m40%")
    time.sleep(5)
    print("\x1b[1;94m50%")
    time.sleep(6)
    print("\x1b[1;95m60%")
    time.sleep(7)
    print("\x1b[1;96m70%")
    time.sleep(8)
    print("\x1b[1;97m80%")
    time.sleep(9)
    print("\x1b[1;98m90%")
    time.sleep(10)
    print("\x1b[1;99m100%")
    time.sleep(9)
    print("\x1b[1;90mSelamat Korban Sekarang sudah gila!\x1b[1;91mHati-hati ada hukum karma !!!")
def keluar():
	os.system('clear')
	print("\x1b[1;95mBAGOES ANDA TAKUT DOSA!!!")
	sys.out.exit()
	def dosa():
		os.system('clear')
		print("Kenapa Anda ingin menghapus Dosa?")
		dosa=raw_input()
		print("Anda Yakin ?[Y/N]")
		yakin=raw_input()
		if yakin=='Y' or yakin=='y':
			print("Nama:")
			nama=raw_input()
			print("umur:")
			umur=raw_input()
			print("Status")
			status=raw_input("1. Jomblo\n2. Nikah/Pacar\n3. Ga punya Status")
			if status=='01' or status=='1':
				print('Menjadi Jomblo Sangatlah baik,.\nDOSA yang bisa terhapus=banyak\nMulai Menghapus?[Y/N]')
				mulai=raw_input()
def mulai():
	os.system('clear')
	if mulai=='Y' or mulai=='y':
	   time.sleep(1)
	   print('\x1b[1;90m10%')
       time.sleep(2)
	   print('\x1b[1;91m20%')
       time.sleep(3)
	   print('\x1b[1;92m30%')
       time.sleep(4)
       print('\x1b[1;93m40%')
       time.sleep(5)
       print('\x1b[1;94m50%')
       time.sleep(6)
       print('\x1b[1;95m60%')
       time.sleep(7)
       print('\x1b[1;96m70%')
       time.sleep(8)
       print('\x1b[1;97m80%')
       time.sleep(9)
       print('\x1b[1;98m90%')
       time.sleep(10)
       print('\x1b[1;99m100%')
       time.sleep(3)
       print('\x1b[1;90m[+]\x1b[1;91mSelamat Dosa Anda Telah terhapus!!')
       menu()
    else:
		menu()
    else:
        menu()
    		elif status=='02' or status=='2':
    			time.sleep(4)
    			print('Ciee Selamat ya!!! Mimin Masi Jomblo nich:(..\nDosa yang bisa terhapus=lumayan\nMulai Menghapus?[Y/N]')
    			mulai=raw_input()
    			mulai()
    		else:
    			time.sleep(3)
    			print('Sedih nya Ga punya Status:( Ga usah idup woe !!!\nDosa yang bisa terhapus=sedikit\nMulai Menghapus?[Y/N]')
    			mulai=raw_input()
    			mulai()
def menu():
	os.system('clear')
	print('1. Santet Online\n2. Hapus Dosa\n3. Keluar')
	pilih=raw_input()
	if pilih=='01' or pilih=='1':
		santet()
	elif pilih=='02' or pilih=='2':
		dosa()
	else:
		keluar() 
