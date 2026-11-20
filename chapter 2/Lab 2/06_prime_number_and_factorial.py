number = int(input("Enter a number to check prime: "))

if number <= 1:
    print("Not a prime number.")

else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number.")
    else:
        print("Not a prime number.")

n = int(input("\nEnter a number for factorial: "))

if n < 0:
    print("Factorial is not defined.")

else:
    factorial = 1

    for i in range(1, n + 1):
        factorial = factorial * i

    print("Factorial:", factorial)