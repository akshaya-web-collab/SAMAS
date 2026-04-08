# WEEK 7: FarmLog Class

class FarmLog:
    def __init__(self, date, crop, moisture, temp):
        self.date = date
        self.crop = crop
        self.moisture = moisture
        self.temp = temp

log = FarmLog(input("Date: "), input("Crop: "),
              float(input("Moisture: ")), float(input("Temp: ")))

print(log.date, log.crop, log.moisture, log.temp)