#step-1:for loop mostly used in our project

# expenses = [250, 100, 700, 600, 900]

# for at in expenses:
#     print(at,end = ' ')
# for amt in expenses:
#     if amt> 500:
#         print(amt)
# for amnt in expenses:
#     print(amnt+100)

expenses = [250, 100, 700, 600, 900]

total = 0

for amount in expenses:
    total = total + amount

print("Total Expense:", total)

for amount in expenses:
    if amount > 500:
        print("High Expense:", amount)
