# WEEK 2: Menu Driven Farm Monitoring System

records = []

while True:
    print("\n--- FARM MONITORING MENU ---")
    print("1. Add Daily Farm Record")
    print("2. View All Records")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Date: ")
        crop = input("Crop name: ").title()
        moisture = float(input("Soil moisture (%): "))
        temperature = float(input("Temperature (°C): "))

        records.append([date, crop, moisture, temperature])
        print("Record added successfully!")

    elif choice == "2":
        print("\n--- All Farm Records ---")
        for record in records:
            print(record)

    elif choice == "3":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Try again.")