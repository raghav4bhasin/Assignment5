print("Prime Numbers Between 1 and 101 are:-")
for val in range(1, 101):
   if val > 1:
       for i in range(2, val):
           if (val % i) == 0:
               break
       else:
           print("\t", val)
