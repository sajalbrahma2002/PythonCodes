x=int(input("Enter the height of the first student (cm) :- "))
y=int(input("Enter the height of the second student (cm):- "))
z=int(input("Enter the height of the third student (cm):- "))
if x>0 and y>0 and z>0:
    if x<y and x<z:
        print("Height of the shortest person is :- ",x," cm.")
    elif y<x and y<z:
        print("Height of the shortest person is :- ",y," cm.")
    else:
        print("Height of the shortest person is :- ",z," cm.")
else:
    print("Invalid Input")