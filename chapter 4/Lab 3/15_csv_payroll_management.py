import csv

filename = "payroll.csv"

with open(filename, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Employee ID",
        "Name",
        "Basic Salary",
        "Allowance",
        "Total Salary"
    ])

    count = int(input("How many employees? "))

    for i in range(count):
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")

        basic = float(input("Enter basic salary: "))
        allowance = float(input("Enter allowance: "))

        total = basic + allowance

        writer.writerow([
            emp_id, name, basic, allowance, total
        ])

print("Payroll saved in", filename)

with open(filename, "r") as file:
    print(file.read())