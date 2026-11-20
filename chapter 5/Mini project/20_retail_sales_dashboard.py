import csv
import matplotlib.pyplot as plt

filename = "sales.csv"

sample_sales = [
    ["Product", "Sales"],
    ["Laptop", 50000],
    ["Phone", 35000],
    ["Headphones", 12000],
    ["Keyboard", 8000],
    ["Mouse", 5000]
]

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(sample_sales)

products = []
sales = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        products.append(row["Product"])
        sales.append(float(row["Sales"]))

print("RETAIL SALES SUMMARY")

for product, amount in zip(products, sales):
    print(product, ":", amount)

print("Total sales:", sum(sales))

plt.bar(products, sales)

plt.title("Retail Sales Dashboard")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.xticks(rotation=30)
plt.tight_layout()

plt.show()