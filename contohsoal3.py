# Fungsi konversi suhu menggunakan lambda function
celcius_to_fahrenheit = lambda C: (9/5) * C + 32  
celcius_to_reamur = lambda C: 0.8 * C  
C = float(input("Masukkan suhu dalam Celcius: "))

print(f"Input C = {C}. Output F = {celcius_to_fahrenheit(C)}.")
print(f"Input C = {C}. Output R = {celcius_to_reamur(C)}.")
