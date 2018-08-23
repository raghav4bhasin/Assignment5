age = int(input("Enter your age: "))
gender = input("Enter your sex (M or F): ")
status = input("Are you Married? (Y or N): ")
flag2 = 0 
if (status != 'Y' and status !='N') or (gender != 'M' and gender != 'F'):
    a = "ERROR!!"
    print(a)
    flag2 = 1
if flag2 == 0:    
    place = "rural"
    flag = 0
    if gender == "F":
        place = "in Urban areas only."

    elif gender == "M":
        if age >= 20 and age < 40:
            place = "anywhere."
        elif age >= 40 and age <= 60:
            place = "in Urban areas only."
        else:
            flag = 1
    else:
        flag = 1

    print(" ")

    if flag == 0:
        print("You can work", place)
    else:
        print("ERROR!!")
