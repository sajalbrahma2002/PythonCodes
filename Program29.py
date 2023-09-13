v=int(input("Enter the no of veges to be entered :- "))
f=int(input("Enter the no of fruits to be entered : - "))
g=int(input("Enter the no f grocery to be entered : -"))
if v>0 and f>0 and g>0:
    veges=[]
    fruits=[]
    grocery=[]
    for i in range(v):
        x=input("Enter the vegetable name : - " )
        veges.append(x)
    for j in range(f):
        y=input("Enter the fruit name : - ")
        fruits.append(y)
    for k in range(g):
        z=input("Enter the grocery name : - ")
        grocery.append(z)
    veges.sort()
    fruits.sort()
    grocery.sort()
    sort1=veges+fruits+grocery
    print("List of items before consolidation :- ")
    for m in range(len(sort1)):
        print(sort1[m],end=" ")
    sort1.sort()
    print("\nList of items after consolidation :- ")
    for n in range(len(sort1)):
        print(sort1[n],end=" ")
else:
    print("Invalid Input..")