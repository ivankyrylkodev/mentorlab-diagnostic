# budget.py: checks whether a shopping list fits into a budget.
prices = {"bread": 30, "milk": 45, "apples": 60}

budget = int(input("Your budget in UAH: "))

total = 0
for item in prices:
    total = total + prices[item]

print("Items: " + str(len(prices)))
print("Total: " + str(total) + " UAH")

if total > budget:
    print("Over budget by " + str(total - budget) + " UAH")
else:
    left = budget - total
    print("Within budget. Left: " + str(lefts) + " UAH")