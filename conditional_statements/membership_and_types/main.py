# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

# Gunakan operator keanggotaan 'in' pada string description
contains_raw = 'raw' in description
contains_Imported = 'Imported' in description

# Gunakan type() untuk memverifikasi tipe data
price_is_float = type(price) is float
count_is_int = type(count) is int

# Cetak hasil sesuai format yang diminta
print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)