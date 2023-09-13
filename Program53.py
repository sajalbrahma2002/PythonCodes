N=int(input("Enter the number whose factorial is to be calculated :- "))
def fact(x):
    if x==1:
        return 1
    else:
        return (x*fact(x-1))
if N>0:
    print("The number entered is :- ",N)
    a=fact(N)
    print("The factorial of",N,"is :-",a)
else:
    print("Invalid Input")