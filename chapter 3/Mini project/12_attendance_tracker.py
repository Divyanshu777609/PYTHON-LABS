attendance = {}

while True:
    print("\n1. Mark attendance")
    print("2. View attendance")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        status = input("Present or Absent (P/A): ").upper()

        if status == "P":
            attendance[name] = "Present"

        elif status == "A":
            attendance[name] = "Absent"

        else:
            print("Enter P or A.")
            continue

        print("Attendance saved.")

    elif choice == "2":
        for name, status in attendance.items():
            print(name, "-", status)

    elif choice == "3":
        break

    else:
        print("Invalid choice.")