# Daftar awal sayuran
vegetables = ["tomatoes", "potatoes", "onions", "carrots"]

# Hapus "onions" dari daftar
vegetables.remove("onions")

# Tambahkan "carrots" jika belum ada
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

# Tambahkan "cucumbers" jika belum ada
if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# Urutkan daftar secara alfabetis
vegetables.sort()

# Cetak hasil akhir
print("Updated Vegetable Inventory:", vegetables)