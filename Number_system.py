"""Number system in Python"""

number=int(input("Enter the number : "))

while(True):
    ch=int(input("Enter your choice :"))
    #Decimal to binary
    if ch==1:
        print(bin(number))
    #Decimal to octal
    elif ch==2:
        print(oct(number))
    #decimal to hexa
    elif ch==3:
        print(hex(number))
    elif ch==4:
        num=chr(number)
        print(num)
    elif ch==0:
        break
    else:
        print("Invalid input")