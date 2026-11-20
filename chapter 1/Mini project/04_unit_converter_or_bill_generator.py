print("UNIT CONVERTER")
print("1. Kilometres to Miles")
print("2. Celsius to Fahrenheit")
print("3. Kilograms to Pounds")

choice = int(input("Enter your choice: "))
value = float(input("Enter the value: "))

if choice == 1:
    print("Miles:", value * 0.621371)

elif choice == 2:
    print("Fahrenheit:", (value * 9 / 5) + 32)

elif choice == 3:
    print("Pounds:", value * 2.20462)

else:
    print("Invalid choice.")