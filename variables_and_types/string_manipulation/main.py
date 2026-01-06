grocery_items = "milk cheese bread apples oranges chicken"

# Ekstrak item menggunakan string slicing
dairy1 = grocery_items[0:4]    # "milk"
dairy2 = grocery_items[5:11]   # "cheese"
bakery1 = grocery_items[12:17] # "bread"

# Buat dan cetak pesan sesuai format yang diminta
print("We have dairy and bakery items:", dairy1 + ",", dairy2 + ", and", bakery1, "in aisle 5")