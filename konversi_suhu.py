#Perbandingan skala C : R : F : K = 5 : 4 : 9 : 5
# F = +32 K = +273
print ("Konversi Suhu")
print ("==================")
print ("[C] Celcius")
print ("[R] Reamur")
print ("[F] Farenheit")
print ("[K] Kelvin")
print ("==================")

skala1 = input ("Satuan suhu 1 : ")
skala2 = input ("Satuan suhu 2 : ")
suhu1 = int(input ("Nilai suhu 1 : "))

if skala1 == "R":
	suhu1 = suhu1 * 5/4
elif skala1 == "K":
	suhu1 = suhu1 - 273
elif skala1 == "F":
	suhu1 = (suhu1 - 32) * 5/9
elif skala1 == "C":
	suhu1 = suhu1
else:
	print ("Eror input satuan 1")

if skala2 == "R":
	suhu2 = suhu1 * 4/5
elif skala2 == "K":
	suhu2 = suhu1 + 273
elif skala2 == "F":
	suhu2 = suhu1 * 9/5 +32
elif skala2 == "C":
	suhu2 = suhu1
else:
	print ("Eror input satuan 2")

print (suhu2)

