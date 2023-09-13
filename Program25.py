N=int(input("enter the no of products to be added in a list :- "))
list=[]
for i in range (0,N):
    y=input("Enter the product :-")
    list.append(y)
z=input("Enter the new product : - ")
w=int(input("Enter the position index of the product in the list"))
if z in list:
    print("Already Exists")
    exit()
else:
    list.insert(w,z)
    for i in range (0,len(list)):
        print(list[i],end=" ")