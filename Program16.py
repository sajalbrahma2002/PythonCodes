X=int(input("Enter a number :- "))
rem=0
sum=0
temp=X
if X>0 :
    if X>9:
        while(X!=0):
            rem=X%10
            sum=sum+rem**3
            X=X//10
        if (temp==sum):
            print(" Equal")
        else:
            print("Not Equal")
    else:
        print("Do not enter single digit.")
else:
    print("Invalid Input")