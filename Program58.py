N=int(input("Enter the number of students :- "))
name=[]
if N<=0:
    print("Invalid Input")
else:
    for i in range(0,N):
        x=input("Enter the name :- ")
        name.append(x)
    y=lambda a:a.sort()
    y(name)
    for j in range(0,N):
        print(name[j])