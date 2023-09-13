N=int(input("Enter the value of N :- "))
count1=0
count2=0
count3=0
if N>0 :
    i=1
    while(i<=N):
        X=int(input("Enter a number :- "))
        if X>0:
            count1=count1+1
            i=i+1
        elif X<0:
            count2=count2+1
            i=i+1
        else:
            count3=count3+1
            i=i+1
    print("Totak positive Numbers :- ",count1)
    print("Total Negative Numbers :- ",count2)
    print("Total zeroes :- ",count3)
else:
    print("Invalid Input")