
customer_name = input("Enter customer name: ")
balance = float(input("Enter initial account balance: "))

deposit = float(input("Enter deposit amount: "))
balance = balance + deposit

withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance = balance - withdraw
    print("Withdrawal successful")
else:
    print("Insufficient balance")

print("\n----- Account Details -----")
print("Customer Name:", customer_name)
print("Updated Account Balance:", balance)