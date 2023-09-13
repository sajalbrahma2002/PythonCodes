N=int(input("Enter the no of products to be enterd in tuple :- "))
t=[]
for i in range(N):
    x=input("Enter the name of the product :- ")
    t.append(x)
t=tuple(t)
y=input("Enter the new product :- ")
t=list(t)
t.append(y)
t=tuple(t)
for p in range(0,len(t)):
    print(t[p],end=" ")
