# WEEK 6: Simple Classes

class Crop:
    def __init__(self, name, height):
        self.name = name
        self.height = height

class Soil:
    def __init__(self, moisture):
        self.moisture = moisture

class Environment:
    def __init__(self, temp):
        self.temp = temp

c = Crop(input("Crop: "), float(input("Height: ")))
s = Soil(float(input("Moisture: ")))
e = Environment(float(input("Temp: ")))

print(c.name, c.height, s.moisture, e.temp)