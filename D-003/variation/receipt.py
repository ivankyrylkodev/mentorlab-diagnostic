# receipt.py: prints a receipt for a shopping list and applies a discount.
prices = {"bread": 20, "milk": 30, "apples": 50}
basket = ["bread", "milk", "apples"]

discount = int(input("Discount in percent (0-50): "))

total = 0
for i in range(len(basket)):
    item = basket[i]
    print(item + ": " + str(prices[item]) + " UAH")
    total = total + prices[item]

if discount > 0:
    total = total - total * discount // 100
    print("Discount: " + discount + "%")

print("Total: " + str(total) + " UAH")