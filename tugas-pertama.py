angka = 2135

# biner
biner = format(angka,'b')
print(f"biner : ",biner)

# octal 
octal = format(angka,'o')
print(f"octal : ",octal)

# hexadecimal
hexadecimal = format(angka,'x')
print(f"hexadecimal : ",hexadecimal)

#Number dengan 4 angka dibelakang koma ( 2135.0000)
empat_angka_koma = f"{angka:.4f}"
print(empat_angka_koma)

# Pemisah ribuan dengan koma (2,135) 
pemisah_ribuan_koma = f"{angka:,}"
print(pemisah_ribuan_koma)