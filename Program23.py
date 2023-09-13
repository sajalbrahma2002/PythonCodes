N=int(input("Enter the value of N :- "))
if N<=0:
    print("Invalid Input")
elif N==1:
    print("Not a prime")
elif N==2:
    print(2)
else:
    for i in range (0,N):
        if(i>1):
            for j in range(2,i):
                if (i%j)==0:
                    break
            else:
                print(i,end=" ")