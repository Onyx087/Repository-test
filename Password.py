import random

huruf = "abcdefghijklmnopqrstuvwxyz"
huruf_besar = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
angka = "0123456789"
karakter = "!@#$%^&*()"

semua = huruf + huruf_besar + angka + karakter

password = ''.join(random.sample(semua, 8))

print(f"Ini password kamu {password}")