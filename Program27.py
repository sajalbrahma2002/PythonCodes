d={}
for i in range(3):
    t=input("enter the name of test :- ")
    minv=int(input("Enter minimum value :- "))
    maxv=int(input("Enter maximum value : - "))
    d[t]=[minv,maxv]
a=input("Enter the test name : -")
b=int(input("Enter the test value : -"))
for i ,j in d.items():
    if (a==i):
        if(j[0]<b<j[1]):
            print("Normal.")
        else:
            print("Abnormal..")

        