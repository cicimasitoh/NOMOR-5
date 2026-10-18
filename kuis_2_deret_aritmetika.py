# kuis2_deret_aritmetika.py

print("=== Program Deret Aritmetika (Perulangan For dan While) ===")

# Penerimaan Input
a = int(input("Masukkan suku pertama (a): "))
b = int(input("Masukkan beda / selisih (b): "))
n = int(input("Masukkan jumlah suku yang ingin ditampilkan (n): "))

# 1. Proses Iteratif Menggunakan Perulangan 'for'
print("\n--- Menampilkan Deret Menggunakan Perulangan 'for' ---")
total_for = 0
for i in range(1, n + 1):
    suku = a + (i - 1) * b
    total_for += suku
    print(f"Suku ke-{i}: {suku}")

print(f"Total Jumlah Keseluruhan Deret (for): {total_for}")

# 2. Proses Iteratif Menggunakan Perulangan 'while'
print("\n--- Menampilkan Deret Menggunakan Perulangan 'while' ---")
count = 1
total_while = 0
while count <= n:
    suku = a + (count - 1) * b
    total_while += suku
    print(f"Suku ke-{count}: {suku}")
    count += 1

print(f"Total Jumlah Keseluruhan Deret (while): {total_while}")