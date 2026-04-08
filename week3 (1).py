# WEEK 3: Farm Record Storage and Search

records = []

while True:
    print("\n1. Add Record")
    print("2. View Records")
    print("3. Search by Date")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        date = input("Date: ").strip()
        crop = input("Crop: ").strip().title()
        moisture = float(input("Moisture: "))
        temp = float(input("Temperature: "))

        records.append([date, crop, moisture, temp])
        print("Record added.")

    elif choice == "2":
        print("\nDate\t\tCrop\tMoisture\tTemp")
        for r in records:
            print(f"{r[0]}\t{r[1]}\t{r[2]}\t\t{r[3]}")

    elif choice == "3":
        search_date = input("Enter date to search: ").strip()
        found = False
        for r in records:
            if r[0] == search_date:
                print(r)
                found = True
        if not found:
            print("No record found.")

    elif choice == "4":
        break

    else:
        print("Invalid option.")