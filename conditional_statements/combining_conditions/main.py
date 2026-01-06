# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Tentukan apakah barang sedang diskon ATAU stoknya menipis (salah satu atau keduanya True)
movingProduct = discounted or lowStock

# Tentukan apakah barang layak untuk promosi:
# yaitu TIDAK sedang diskon DAN stoknya TIDAK mencukupi (lowStock True)
promotion = not movingProduct

# Cetak hasil sesuai format yang diminta
print("Is the item eligible for promotion?", promotion)