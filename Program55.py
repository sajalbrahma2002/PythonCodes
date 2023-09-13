z=int(input("Enter the number :- "))
rev=0
rem=0
def reverse(z):
    global rev
    global rem
    if z>0:
        rem=z%10
        rev=(rev*10)+rem
        return reverse(z//10)
    else:
        return rev
if z<=0:
    print("Invalid Input")
elif z>0 and z<10:
    print("Do not enter single digit.")
else:
    a=reverse(z)
    print("The reverse number is :- ",a)