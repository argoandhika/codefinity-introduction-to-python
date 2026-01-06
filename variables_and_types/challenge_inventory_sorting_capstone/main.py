# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Ekstrak nama barang menggunakan string slicing
candy1 = items[0:9]        # "Bubblegum"
candy2 = items[11:20]      # "Chocolate"
dry_goods = items[22:27]   # "Pasta"

# Ekstrak kategori menggunakan string slicing
category1 = categories[0:11]   # "Candy Aisle"
category2 = categories[13:]  # "Pasta Aisle"

# Tetapkan harga
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# Cetak laporan sesuai format yang diminta
print("We have", candy1, "for", bubblegum_price, "in the", category1)
print("We have", candy2, "for", chocolate_price, "in the", category1)
print("We have", dry_goods, "for", pasta_price, "in the", category2)