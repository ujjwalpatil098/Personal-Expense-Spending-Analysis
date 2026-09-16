#Step 1 — if-else and Conditions
category = input("Enter category: ")
amount = int(input("Enter amount: "))
date = input("Enter date: ")

print("\nExpense Details")
print("Category:", category)
print("Amount:", amount)
print("Date:", date)

if amount >= 1000:
    print("Type: High expense")
elif amount >= 500 and amount < 1000:
    print("Type: Medium expense")
else:
    print("Type: Normal expense")

