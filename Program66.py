y=int(input("Enter the number of days to find the production of super computers :- "))
def calculate(a):
    if a<=3:
        return a
    else:
        return calculate(a-1)+calculate(a-2)+calculate(a-3)

if y<=0:
    print("Invalid Input")
else:
    for i in range(1,y+1):
        print(calculate(i),end=" ")
