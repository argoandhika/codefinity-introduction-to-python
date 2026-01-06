seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# 1. Apakah ada risiko overstock?
# Item seasonal DAN stok saat ini melebihi ambang batas tinggi
overstock_risk = seasonal and (current_stock > high_stock_threshold)

# 2. Apakah layak diberi diskon karena performa penjualan?
# Tidak laku (not selling_well) DAN belum sedang diskon (not on_sale)
discount_eligible = not selling_well and not on_sale

# 3. Apakah barang harus diberi diskon?
# Benar jika salah satu (atau keduanya) kondisi di atas terpenuhi
make_discount = overstock_risk or discount_eligible

# Cetak hasil sesuai format yang diminta
print("Should the item be discounted?", make_discount)