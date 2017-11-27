""""
print("Cek Bilangan Prima")
number=int(raw_input("Masukkan Bilangan Prima:"))
if number <= 1:
    print "Angka gk termasuk bilangan Prima"
else:
    a=2
    check = True
    while a != number:
        if number%a == 0:
            print "Angka gk termasuk bilangan Prima"
            check = False
            break
        a+=1
    if check == True:
        print "Angka Prima" 
"""

#menampilkan deretan bil prima sesuai jumlah inputan
n=int(raw_input("Masukkan jumlah bilangan:"))
for i in range(2,n):
    prima=True
    for j in range(2,i):
        if(i%j==0):
            prima=False
    if(prima):
        print i,"Adalah bilangan prima"

#while search prime

i = 2
while(i < 30):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print (i, " adalah bilangan prima")
   i = i + 1