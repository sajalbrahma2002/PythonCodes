N=int(input("Enter the number between whose factors of 7 are to be found :- "))
def division7(x):
    for i in range(1,x+1):
        if (i%7==0):
            print(i,end=" ")
        else:
            pass
if N>0:
    division7(N)
else:
    print("Invalid Input")