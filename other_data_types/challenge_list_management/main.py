# 1. Inisialisasi list untuk setiap kategori
meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

# 2. Gabungkan menjadi satu list utama
deli_dept = [meat, cheese, condiment]

# Cetak kondisi awal
print("Initial Deli List:", deli_dept)

# 3. Restock Ham jika quantity kurang dari 100
if "Ham" in meat and meat[2] < 100:  # meat[2] adalah quantity
    meat[2] = 100

# 4. Tambahkan seasonal meat
seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

# 5. Hapus condiment dari deli_dept
deli_dept.remove(condiment)

# 6. Urutkan deli_dept berdasarkan elemen pertama dari setiap sublist (nama item)
deli_dept.sort(key=lambda item: item[0])

# Cetak hasil akhir setelah semua operasi
print("Updated Deli List:", deli_dept)