year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        print ("Year ", year, " is a Leap Year.")
else:
    print ("Year ", year, " is NOT a Leap Year.")
