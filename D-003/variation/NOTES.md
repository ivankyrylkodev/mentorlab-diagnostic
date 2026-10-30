## Bug 1
Input: 20
Error: IndexError: list index out of range
Line: 9
Cause: Last i in for is len(basket) = 3 and busket[3] is not exist. Last element in busket is busket[2] =  "apples".
Change: I deleted "+ 1" from line 8.

## Bug 2
Input: 20
Error: TypeError: can only concatenate str (not "int") to str
Line: 15
Cause: it can't print string variable, + and int variable. Both should be string (or int but it would show sum).
Change: I added str in print (print("Discount: " + str(discount) + "%")).

## Inputs tested:
20
Discount in percent (0-50): 20
bread: 20 UAH
milk: 30 UAH
apples: 50 UAH
Discount: 20%
Total: 80 UAH

50
Discount in percent (0-50): 50
bread: 20 UAH
milk: 30 UAH
apples: 50 UAH
Discount: 50%
Total: 50 UAH

0
Discount in percent (0-50): 0
bread: 20 UAH
milk: 30 UAH
apples: 50 UAH
Total: 100 UAH
## AI use: none.