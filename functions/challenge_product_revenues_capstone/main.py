# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]
quantities_sold = [150, 200, 100, 50]

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

def formatted_output(revenues):
    sorted_revenues = sorted(revenues)
    for revenue in sorted_revenues:
        print(f"{revenue[0]} has total revenue of ${revenue[1]}")

revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)
