m=int(input("Enter the number for the range to check multiples of 3 between 1 and M :-"))
if m>0:
    i=1
    if m>1:
        print("the multiples of 3 between 1 and ",m," are :- ")
        while(i<=m):
            if(i%3)==0:
                print(i,end=" ")
                i=i+1
            else:
                i=i+1
    else:
        print("Enter value grater than 1.")
else:
    print("Invalid Input")
