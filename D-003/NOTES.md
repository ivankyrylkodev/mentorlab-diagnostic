## Bug 1
Input: 3
Error: TypeError: '>' not supported between instances of 'int' and 'str'
Line: 13
Cause: Budget variable is string variable in line 4 and '>' is not working with string and int value in 13 line.
Change: I add int in an assignment to budget. (budget = int(input("Your budget in UAH: ")))

## Bug 2
Input: 145
Error: NameError: name 'lefts' is not defined. Did you mean: 'left'?
Line: 17
Cause: lefts is not identified variable. If program want show left it should be written left not lefts.
Change: I delete letter s in word lefts in 17 line.

## Inputs tested:
3
Your budget in UAH: 3
Items: 3
Total: 135 UAH
Over budget by 132 UAH

146
Your budget in UAH: 146
Items: 3
Total: 135 UAH
Within budget. Left: 11 UAH

135
Your budget in UAH: 135
Items: 3
Total: 135 UAH
Within budget. Left: 0 UAH
## AI use: none.
## Time: 
Learning 0 min
Practice 20 min