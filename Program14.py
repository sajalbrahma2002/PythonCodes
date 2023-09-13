N=int(input("Enter the value of N :- "))
if N>0:
    i=1
    sum=0
    while(i<=N):
        j=1
        fact=1
        while(j<=i):
            fact=fact*j
            j=j+1
        sum=sum+fact
        i=i+1
    print(" The sum of the",N,"factorial numbers is :- ",sum)
else:
    print("Invalid Input")