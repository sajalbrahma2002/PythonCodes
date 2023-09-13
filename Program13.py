K=int(input("Enter the value of  K :- "))
if K>0:
    i=1
    sum=0
    print("The multiples of 10 between 1 and ",K," are :- ")
    while(i<=K):
        if(i%10)==0:
            print(i,end=" ")
            sum=sum+i
            i=i+1
        else:
            i=i+1
    print("The sum of multiples of 10 between 1 and ",K," is :- ",sum)
else:
    print("Invalid Input")