# How to build a simple calculator using python
#1. Add
#2. Subtract
#3. Multiply
#4. Divide

print("Select an arithmetic operation to perform")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()
if operation == "1":
    # code for add
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The sum is :", num1+num2)
elif operation == "2":
    # code for subtract
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The difference is :", num1-num2)
elif operation == "3":
    # code for multiply
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The product is :", num1*num2)
elif operation =="4":
    # code for divide
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print("The result is :", num1/num2)
else:
    print("Invalid entry")