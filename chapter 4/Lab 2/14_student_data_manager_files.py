filename = "students.txt"

while True:
    print("\n1. Add student")
    print("2. View students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")

        with open(filename, "a") as file:
            file.write(roll + "," + name + "\n")

        print("Student saved.")

    elif choice == "2":
        try:
            with open(filename, "r") as file:
                print(file.read())

        except FileNotFoundError:
            print("No student records found.")

    elif choice == "3":
        break

    else:
        print("Invalid choice.")