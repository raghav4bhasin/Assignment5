quant = int(input("Enter the purchased quantity: "))
cpu = 100
flag = 0
dsc = 0
if quant > 1000:
    bill = quant * cpu
    dsc = int((10/100) * bill)
    bill = bill - dsc
    flag = 1
else:
    bill = quant * cpu
if flag == 1:
    print("Total Discount: ",dsc)
    print("Total Bill: ",bill)
else:
    print("Total Bill: ",bill)

    
    
