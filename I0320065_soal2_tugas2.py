#biodata
nama= "Muhammad Hafizh Rafi Susanto"
tempat_lahir= "Jakarta"
tanggal_lahir= 16
bulan_lahir= 10
tahun_lahir= 2002
hobi= "Bermain music dan Berolahraga"
univ= "Universitas Sebelas Maret"
prodi= "Teknik Industri"
nim= "I0320065"
print("biodata saya: ")
print("nama:",nama)
print("tempat tanggal lahir:",tempat_lahir+",",str(tanggal_lahir)+"-"+str(bulan_lahir)+"-"+str(tahun_lahir))
print("hobi: ",hobi)
print("univ: ",univ)
print("prodi: ",prodi)
print("nim:",nim)

#menghitung umur
tanggal_sekarang= 12
bulan_sekarang= 3
tahun_sekarang= 2021
umur=int((tanggal_sekarang-tanggal_lahir)/30+(bulan_sekarang-bulan_lahir)+(tahun_sekarang-tahun_lahir)*12)
print("umur saya dalam bulan adalah",umur,"bulan")

#tinggi badan saya
tinggi= float(201/2)+(24.67*3)
print("tinggi badan saya adalah",tinggi,"cm")

#ukuran sepatu saya
ukuran_sepatu= int(50/2)+(4.25*4)
print("ukuran kaki saya adalah",ukuran_sepatu,"cm")