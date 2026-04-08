# WEEK 4: Function Based Modular SAMAS

records = []

def validate_moisture(m):
    return m >= 0

def validate_temperature(t):
    return -10 <= t <= 60

def add_record():
    date = input("Date: ")
    crop = input("Crop: ").title()
    moisture = float(input("Moisture: "))
    temp = float(input("Temperature: "))

    if not validate_moisture(moisture):
        print("Invalid moisture value!")
        return
    if not validate_temperature(temp):
        print("Invalid temperature value!")
        return

    records.append([date, crop, moisture, temp])
    print("Record added successfully!")

def view_records():
    print("\nDate\t\tCrop\tMoisture\tTemp")
    for r in records:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t\t{r[3]}")

def search_record():
    date = input("Enter date to search: ")
    for r in records:
        if r[0] == date:
            print(r)
            return
    print("Record not found.")

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Search Record")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_record()
    elif ch == "2":
        view_records()
    elif ch == "3":
        search_record()
    elif ch == "4":
        break
    else:
        print("Invalid choice!")