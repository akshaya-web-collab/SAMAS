# WEEK 8: File Handling

while True:
    print("\n1.Add 2.View 3.Exit")
    ch = input("Choice: ")

    if ch == "1":
        d = input("Date: ")
        c = input("Crop: ")
        with open("farm.txt", "a") as f:
            f.write(d + "," + c + "\n")

    elif ch == "2":
        try:
            with open("farm.txt", "r") as f:
                print(f.read())
        except:
            print("No file")

    elif ch == "3":
        break
