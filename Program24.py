list=[]
N=int(input("Enter the no of appliances to be added in the list :- "))
if N>0:
    sum=0
    for i in range (0,N):
        X=int(input("Enter the price of appliances : -"))
        list.append(X)
        sum=sum+X
    print("Total amount to be paid bt Sujith :- ",sum)
else:
    print("Invalid Input")