fruit=['Apple','Banana','Mango']
veges=['Carrot','Cabbage','Potato']
grocery=['Wheat','Sugar','Rice']
fprice=[100,50,80]
vprice=[70,40,55]
gprice=[45,55,50]
fruit_price=0
fruit_dis=0
fruit_sum=0
veges_price=0
veges_dis=0
veges_sum=0
grocery_price=0
grocery_dis=0
grocery_sum=0
N=int(input("Enter the total number of elements to be bought by Kishore :- "))
if N>0:
    list1=[]
    for a in range(N):
        item=input("Enter the item name : - ")
        if item in fruit:
            for i in range(len(fruit)):
                if(item==fruit[i]):
                    list1.append(item)
                    x=int(input("Enter the no of items to be bought :- "))
                    fruit_price=fprice[i]*x*0.05
                    fruit_dis=(fprice[i]*x)-fruit_price
                    fruit_sum=fruit_sum+fruit_dis
        elif item in veges:
            for j in range(len(veges)):
                if(item==veges[j]):
                    list1.append(item)
                    y=int(input("Enter the no of items to be bought :- "))
                    veges_price=vprice[j]*y*0.03
                    veges_dis=(vprice[j]*y)-veges_price
                    veges_sum=veges_sum+veges_dis
        elif item in grocery:
            for k in range(len(grocery)):
                if(item==grocery[k]):
                    list1.append(item)
                    z=int(input("Enter the no of items to be bought :- "))
                    grocery_price=gprice[k]*z*0.07
                    grocery_dis=(gprice[k]*z)-grocery_price
                    grocery_sum=grocery_sum+grocery_dis
        else:
            print("Item does not exist..")
    sum=fruit_sum+veges_sum+grocery_sum
    print("The final amount to be paid by Kishore after discount : - ",sum)
    print("Items bought by Kishore :- ",list1)
else:
    print("Invalid Input")  
        