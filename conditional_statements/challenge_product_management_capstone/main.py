# Variabel input
days_until_expiration = 5   # Contoh nilai
stock_level = 60            # Contoh nilai
product_type = "Perishable" # Bisa "Perishable" atau "Non-Perishable"

if product_type == "Perishable":
    if days_until_expiration <= 3 and stock_level > 50:
        print("30% discount applied")
    elif 4 <= days_until_expiration <= 6 and stock_level > 50:
        print("20% discount applied")
    elif days_until_expiration > 6 and stock_level <= 50:
        print("10% discount applied")
    # Jika tidak memenuhi salah satu kondisi di atas, tidak ada output untuk perishable
else:
    print("No discount available for non-perishable items.")