name = input("Enter customer name: ")
balance = float(input("Enter initial account balance: "))

deposit = float(input("Enter deposit amount: "))
balance = balance + deposit

withdrawal = float(input("Enter withdrawal amount: "))

if balance - withdrawal >= 1000:
    balance = balance - withdrawal
    print("Withdrawal successful")
else:
    print("Withdrawal denied! Minimum balance of 1000 required.")

print("Customer Name:", name)
print("Updated Account Balance:", balance)