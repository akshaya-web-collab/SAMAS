# WEEK 5: Dictionaries, Tuples and Sets in SAMAS

farm_records = []
crop_set = set()
fertilizer_set = set()

def add_record():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    crop = input("Enter crop name: ").strip().title()
    moisture = float(input("Soil moisture (%): "))
    ph = float(input("Soil pH: "))
    temperature = float(input("Temperature (°C): "))
    humidity = float(input("Humidity (%): "))
    rainfall = float(input("Rainfall (mm): "))
    irrigation = float(input("Irrigation used (liters): "))
    fert_type = input("Fertilizer type: ").strip().title()
    fert_qty = float(input("Fertilizer quantity (kg): "))
    growth = float(input("Crop height (cm): "))

    record = {
        "date": date,
        "crop": crop,
        "soil": {
            "moisture": moisture,
            "ph": ph
        },
        "environment": {
            "temperature": temperature,
            "humidity": humidity,
            "rainfall": rainfall
        },
        "irrigation": irrigation,
        "fertilizer": (fert_type, fert_qty),
        "growth": growth
    }

    farm_records.append(record)
    crop_set.add(crop)
    fertilizer_set.add(fert_type)

    print("Farm record added successfully!")

def view_records():
    print("\n--- FARM RECORDS ---")
    for r in farm_records:
        print(r)

def search_by_crop():
    search_crop = input("Enter crop name to search: ").title()
    found = False
    for r in farm_records:
        if r["crop"] == search_crop:
            print(r)
            found = True
    if not found:
        print("No records found for this crop.")

def view_unique_items():
    print("\nUnique Crops:", crop_set)
    print("Unique Fertilizers:", fertilizer_set)

while True:
    print("\n--- WEEK 5 FARM MENU ---")
    print("1. Add Farm Record")
    print("2. View All Records")
    print("3. Search by Crop")
    print("4. View Unique Crops & Fertilizers")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        view_records()
    elif choice == "3":
        search_by_crop()
    elif choice == "4":
        view_unique_items()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")