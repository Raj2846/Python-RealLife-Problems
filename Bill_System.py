
while True:
    print("\n===== ELECTRICITY BILL MENU =====")
    print("1. Calculate Electricity Bill")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        units = int(input("Enter units consumed: "))

        if units <= 100:
            bill = units * 2

        elif units <= 200:
            bill = (100 * 2) + (units - 100) * 3

        elif units <= 300:
            bill = (100 * 2) + (100 * 3) + (units - 200) * 5

        else:
            bill = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

        print("Total Electricity Bill = ₹", bill)

    elif choice == 2:
        print("Exit......")
        break

    else:
        print("Invalid Choice! Please try again.")