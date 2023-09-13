list1=["Apple","Orange","Mango","Banana"]
list2=[120,100,85,50]
N=int(input("Enter the no of products bought by Ram :- "))
sum=0
if N>0:
    list3=[]
    for i in range(0,N):
        X=input("Enter the product :- ")
        if X not in list1:
            print("Product not found.")
            exit()
        else:
            list3.append(X)
    for i in range(0,len(list3)):
        for j in range(0,len(list1)):
            if(list3[i]==list1[j]):
                sum=sum+list2[j]
    print("Total amount paid by Ram :- ",sum)
else:
    print("Invalid Input")