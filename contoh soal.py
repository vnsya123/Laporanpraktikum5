# definisi fungsi 
# menghitung luas persegi panjang 



def menghitung_luas_persegi_panjang(panjang, lebar):
    x = panjang * lebar  
    return x  
panjang = 15
lebar = 10

# argument dan parameter
luas = menghitung_luas_persegi_panjang(panjang, lebar)
print(luas)  

def hitung_luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

alas = 8   
tinggi = 5  

luas_segitiga = hitung_luas_segitiga(alas, tinggi)
print("Luas Segitiga =", luas_segitiga)


# lamdba 
hitung_luas_segitiga = lambda alas, tinggi: 0.5 * alas * tinggi

alas = 8   
tinggi = 5  

luas_segitiga = hitung_luas_segitiga(alas, tinggi)
print("Luas Segitiga =", luas_segitiga)

