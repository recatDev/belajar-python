import random
#easy 1-10
#normal 1-100
#hard 1-1000
#custom
print ("Game Tebak Angka")
print ("====================")
print ("(1) Easy")
print ("(2) Normal")
print ("(3) Hard")
print ("(4) Custom")
print ("====================")
mode = input("Pilih Mode : ")
if mode == "1" :
	a = 1 
	b = 10
elif mode == "2":
	a = 1
	b = 100
elif mode == "3":
	a = 1
	b = 1000
elif mode == "4":
	print ("Buat modemu sendiri!")
	a = int(input ("Masukkan range angka awal : "))
	b = int(input ("Masukkan range angka akhir : "))
else :
	print ("Eror input mode")

def play():
	hasil = "false"
	num = random.randint(a,b)
	print (num)
	while hasil != "true":
		tebak = int(input("Tebakan : "))
		if tebak == num:
			hasil = "true"
			print ("Selamat, tebakanmu benar!")
			loop = input("Ingin main lagi?(y/n) ")
			if loop == "y":
				play()	
			else:
				print ("Terima kasih sudah bermain..")
		elif tebak < num:
			print ("terlalu rendah, coba lagi!")
			hasil = "false"
		elif tebak > num:
			print ("terlalu tinggi, coba lagi!")
			hasil = "false"
		else:
			print ("Eror input tebak")

play()