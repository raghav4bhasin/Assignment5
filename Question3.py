ages = []
for i in range (3):
    a = int(input("Enter age of person {}: ".format(i+1)))
    ages.append(a)

print(" ")
print("Person ",ages.index(max(ages))+1, " is the oldest." )
print("Person ",ages.index(min(ages))+1, " is the youngest." )            
