Z=int(input("Enter a number :- "))
rem=0
rev=0
sum=0
if Z>0:
    while(Z!=0):
        rem=Z%10
        rev=rev*10+rem
        sum=sum+rem
        Z=Z//10
    if sum>9:
        print("The reverse order of the entered no",Z," is :- ",rev)
        print("The sum of the reverse number is :-",sum)
    else:
        print("Do not enter single digit number.")
else:
    print("Invalid Input")