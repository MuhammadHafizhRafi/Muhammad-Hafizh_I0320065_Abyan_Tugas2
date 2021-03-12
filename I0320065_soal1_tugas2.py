#menghitung luas persegi panjang
print("menghitung luas persegi panjang")
print("input nilai panjang dan lebar persegi panjang")
panjang = input("Panjang (cm): ")
lebar = input("Lebar (cm): ")
luas = (float(panjang)*float(lebar))
print("Luas dari persegi panjang adalah ", luas, "cm^2")

#menghitung luas lingkaran
print("menghitung luas lingkaran")
print("input nilai jari-jari lingkaran")
jari_jari = input("jari-jari (cm): ")
phy = 3.14
luas = (float(phy*float(jari_jari)**2))
print("luas dari lingkaran adalah", luas, "cm^2")

#menghitung luas permukaan kubus
print("mengitung luas permukaan kubus")
print("input nilai panjang sisi")
panjang = input("nilai panjang (cm): ")
luas = (6*(float(panjang))**2)
print("luas dari permukaan kubus adalah", luas, "cm^2")

#menghitung konverensi suhu ke farenheit
print("menghitung konverensi suhu ke farenheit")
print("input nilai suhu dalam farenheit")
c = float(input("masukkan nilai suhu dalam celcius: "))
f = 9*(c/5)+32
print("konversi suhu ke farenhit adalah", f, "farenhit")

#menghitung konverensi nilai suhu reamur ke kelvin
print("menghitung konverensi nilai suhu reamur ke kelvin")
print("input nilai suhu reamur dalam kelvin")
r = float(input("masukkan nilai suhu dalam reamur: "))
k = 5*(r/4)+273
print("nilai suhu reamur ke kalvin adalah", k, "kelvin")
