lst = []
print("Enter list elements:- ")

for i in range (5):
    num = int(input())
    lst.append(num)
    
print("Original List: ", lst)

x = int(input("Enter Element to delete: "))
print(' ')

for i in lst:
    if(x == i):
        lst.remove(i)
        
else:
    print("List after Deletion: ",lst)
