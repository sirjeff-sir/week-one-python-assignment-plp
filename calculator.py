a = int(input("Please enter the first number: "))
b = int(input("Please input the second number: "))
Operation = str(input("Please input the operation((+, -, /, *): "))

if Operation == "+":
    c = a + b
    print(c)

elif Operation == "-":
    c = a - b
    print(c)

elif Operation == "*":
    c = a * b
    print(c) 

elif Operation == "/":
    c = a / b
    print(c)       

else:
    print("SYNTAX ERROR")