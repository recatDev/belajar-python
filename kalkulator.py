print ("Kalkulator")
print ("================")
print ("(+) Penjumlahan")
print ("(-) Pengurangan")
print ("(x) Perekalian")
print ("(:) Pembagian")
print ("================")
n1 = int(input ("Masukkan Angka Pertama : "))
opr = input ("Masukkan Operator : ")
n2 = int(input ("Masukkan Angka Kedua : "))
if (opr == "+"):
	hasil = n1+n2
elif (opr == "-"):
	hasil = n1-n2
elif (opr == "x"):
	hasil = n1*n2
elif (opr == ":"):
	hasil = n1/n2
else:
	print ("Eror Input Operator")

print (hasil)
