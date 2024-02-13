year = int(input("What year would you like to test?\n"))

if year % 400 == 0:
    print("leap year")
elif year % 4 == 0:
    if year % 100 == 0:
        print('NOT a leap year')
    else:
        print('leap year')
else:
    print('NOT a leap year')