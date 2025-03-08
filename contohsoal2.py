def cek_digit_belakang(a, b, c):
    get_digit = lambda x: x % 10

    digit_a = get_digit(a)
    digit_b = get_digit(b)
    digit_c = get_digit(c)

    
    return digit_a == digit_b or digit_b == digit_c or digit_a == digit_c
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

hasil = cek_digit_belakang(a, b, c)
print(hasil)
