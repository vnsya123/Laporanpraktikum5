def cek_angka(a, b, c):

  if a == b or a == c or b == c:
    return False

  if a + b == c or a + c == b or b + c == a:
    return True
  else:
    return False

print(cek_angka(1, 2, 3))  
print(cek_angka(1, 2, 4))  
print(cek_angka(1, 1, 3))  