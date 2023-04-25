n = int(input("Enter a year : "))
if n % 4 == 0:
    if n % 100 == 0:
        if n % 400 == 0:
            print("It is a leap year")
        else:
            print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")
