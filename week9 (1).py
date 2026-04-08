# WEEK 9: Simple Validation

def valid_moisture(m):
    return m >= 0

m = float(input("Enter moisture: "))

if valid_moisture(m):
    print("Valid")
else:
    print("Invalid")