def bubblesort(contoh):
	length = len(contoh) #Mengulang perulangan for sejumlah anggota elemen suatu tipe data,yang berlaku juga untuk menghitung character suatu string
	print "Angka Awal :",contoh
	for a in range(0,4): # Note == length-1 -> menempatkan elemen di antara 0,1 sampai -1
		for b in range(0, 4):#Note == length-1-a
			if(contoh[b] > contoh[b+1]):
				contoh[b], contoh[b+1] = contoh[b+1],contoh[b]
				print coba
coba = [82,23,88,18,79]
bubblesort(coba)

