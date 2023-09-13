N=int(input("Enter the N value to calculate sum of N factorial :- "))
def fact(x):
    sum=0
    for i in range(1,x+1):
        fact=1
        for j in range(1,i+1):
            fact=fact*j
        sum=sum+fact
    print(sum)
if N>0:
    fact(N)
else:
    print("Invalid Input")