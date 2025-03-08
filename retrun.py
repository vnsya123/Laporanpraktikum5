def kuadrat (x):
    hasil  = x **2 
    return hasil 
y = kuadrat(4)
print (y)



def hitung_volume(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume
volume_balok = hitung_volume(5, 3, 2)
print("Volume balok:", volume_balok)
