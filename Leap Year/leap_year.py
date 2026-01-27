year = int(input("Enter a year: "))

# Check if the year is within the Gregorian calendar period
if year < 1582:
    print("Not within the Gregorian calendar period.")

else:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} Leap year.")
            else:
                print(f"{year} Common year.")
        else:
            print(f"{year} Leap year.")
    else:
        print(f"{year} Common year.")