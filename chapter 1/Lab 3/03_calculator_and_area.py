print("1. Addition  2. Subtraction  3. Multiplication  4. Division")

choice = int(input("Enter your choice: "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", a + b)
elif choice == 2:
    print("Result:", a - b)
elif choice == 3:
    print("Result:", a * b)
elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid choice.")

print("\nArea Calculator")
print("1. Rectangle  2. Square  3. Circle")

shape = int(input("Choose a shape: "))

if shape == 1:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area:", length * width)

elif shape == 2:
    side = float(input("Enter side: "))
    print("Area:", side * side)

elif shape == 3:
    radius = float(input("Enter radius: "))
    print("Area:", 3.14159 * radius * radius)

else:
    print("Invalid choice.")