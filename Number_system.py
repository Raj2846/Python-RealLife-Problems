"""Number system in Python"""

while True:
    print("\nNUMBER SYSTEM MENU")
    print("\n1.Decimal to Binary")
    print("\n2.Decimal to Octal")
    print("\n3.Decimal to Hexadecimal")
    print("\n4.Binary to Decimal")
    print("\n5.Octal to Decimal")
    print("\n6.Hexadecimal to Decimal")
    print("\n7.Exit")

    ch= int(input("Enter your choice: "))

    if ch==1:
        n = int(input("Enter Decimal Number: "))
        print("Binary =", bin(n))

    elif ch==2:
        n = int(input("Enter Decimal Number: "))
        print("Octal =", oct(n))

    elif ch==3:
        n = int(input("Enter Decimal Number: "))
        print("Hexadecimal =", hex(n))

    elif ch==4:
        b = input("Enter Binary Number: ")
        print("Decimal =", int(b, 2))

    elif ch==5:
        o = input("Enter Octal Number: ")
        print("Decimal =", int(o, 8))

    elif ch==6:
        h = input("Enter Hexadecimal Number: ")
        print("Decimal =", int(h, 16))

    elif ch==7:
        print("EXIT.......")
        break

    else:
        print("Invalid Choice! ")