
print("\n ===== Simple Calculator ===== \n")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\n Enter choice (1/2/3/4): ")

if choice == "1":
    print("\nResult =", num1 + num2)

elif choice == "2":
    print("\nResult =", num1 - num2)

elif choice == "3":
    print("\nResult =", num1 * num2)

elif choice == "4":
    if num2 != 0:
        print("\nResult =", num1 / num2)
    else:
        print("\nError! Division by zero is not allowed.")

else:
    print("\nInvalid choice! Please select a valid operation.")