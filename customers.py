# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Antonio Quiros
#
# Reflection 1: .get() vs bracket notation
# I use .get() when a key might legitimately be missing, such as optional
# fields like email or phone, or when I'm counting things and want a default
# of 0. I use bracket notation when the key must exist, so a missing key means
# the data is broken and I want the program to fail loudly instead of hiding
# the problem. My rule of thumb: optional data gets .get(), required data
# gets brackets.
#
# Reflection 2: summary dictionary vs Excel
# The region-totals loop reminds me of a PivotTable or a SUMIF, where I group
# rows by a category and add up an amount for each group. The Python version
# scales better because it makes one pass through the data, is not limited by
# Excel's row limit, and can be rerun on new data without rebuilding anything.

# ---------- Exercise 1: One customer ----------
print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# ---------- Exercise 2: Update and add ----------
print("\n--- Exercise 2 ---")
customer["phone"] = "555-123-4567"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# ---------- Exercise 3: Safe lookup ----------
print("\n--- Exercise 3 ---")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as e:
    print("KeyError caught: key", e, "does not exist")

# ---------- Exercise 4: Iterate ----------
print("\n--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterating without .items() gives only the keys, not the values.
# .items() gives (key, value) pairs, so we can unpack both in the loop.
for key in customer:
    print(key)

# ---------- Exercise 5: Lookup table ----------
print("\n--- Exercise 5 ---")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
price = 200
final_price = price * (1 - discount)
print(f"Tier: {tier} | Discount: {discount:.0%} | Final price: ${final_price:.2f}")

# ---------- Exercise 6: List of dicts ----------
print("\n--- Exercise 6 ---")
customers = [
    {"name": "Alice", "email": "alice@example.com", "tier": "platinum", "ytd_spend": 5200.00},
    {"name": "Bob", "email": "bob@example.com", "tier": "silver", "ytd_spend": 800.25},
    {"name": "Carla", "email": "carla@example.com", "tier": "bronze", "ytd_spend": 150.00},
]
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    amount = 300 * rate
    print(f"{c['name']} | {c['tier']} | discount: ${amount:.2f}")

# ---------- Exercise 7: Nested catalog ----------
print("\n--- Exercise 7 ---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} units left")

# ---------- Exercise 8: Sales by region ----------
print("\n--- Exercise 8 ---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")