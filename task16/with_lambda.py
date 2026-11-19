orders = [
    ["Order-A", 45],
    ["Order-B", 20],
    ["Order-C", 35],
    ["Order-D", 15]
]
sorted_orders = sorted(orders, key=lambda x: x[1])
print("Order delivery by time:")
for order_name, minutes in sorted_orders:
    print(f"{order_name}: {minutes} minutes")
