print("""
1. addition
2. subtraction
3. multiplication
4. exit
""")

choice = input("Enter your choice: ")

if choice == "1":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("Addition is:", num1 + num2)

elif choice == "2":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("Subtraction is:", num1 - num2)

elif choice == "3":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print("Multiplication is:", num1 * num2)

elif choice == "4":
    exit()

else:
    print("Invalid choice")