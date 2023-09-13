x=int(input("Enter the money to buy chocolates (in multiples of Rs.10 :- "))
if x>0:
    if (x%10)==0:
        N=x/10
        print("The no of chocolates bought are :- ",N)
    else:
        print("Enter multiples of Rs.10")
else:
    print("Enter positive value.")
