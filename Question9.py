list1 =[12, 560, "Hello", 111.2, "Gym", 522, 77000, "Food", 3.14, 55.2, 55.5]
list_int=[]
list_str=[]
list_float=[]

for i in list1:
    if(isinstance(i, int)):
        list_int.append(i)

    elif(isinstance(i, str)):
         list_str.append(i)
         
    elif(isinstance(i, float)):
         list_float.append(i)
         
print("Integers: ", list_int)
print("Strings: ", list_str)
print("Float: ", list_float)
