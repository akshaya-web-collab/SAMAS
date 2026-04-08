# WEEK 1: Basic Farm Data Entry Script

date = input("Enter date (YYYY-MM-DD): ").strip()
crop_name = input("Enter crop name: ").strip().title()

soil_moisture = float(input("Enter soil moisture (%): "))
temperature = float(input("Enter temperature (°C): "))

# Basic validation
if soil_moisture < 0:
    print("Invalid soil moisture value!")
elif temperature < -10 or temperature > 60:
    print("Invalid temperature value!")
else:
    print("\n--- Farm Record ---")
    print(f"Date        : {date}")
    print(f"Crop        : {crop_name}")
    print(f"Soil Moisture: {soil_moisture}%")
    print(f"Temperature : {temperature}°C")