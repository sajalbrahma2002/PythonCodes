jewel=input("Enter the name of jewel (Silver|Gold|Platinum|Diamond) :- ")
grams=float(input("Enter the weight of jewel in grams :- "))
price=float(input("Enter the price of jewel for each gram :- "))

def Silverfun(g,p):
    total=g*p
    wastage=total*0.03
    gst=(total+wastage)*0.03
    net=total+wastage+gst
    print("The total amount to be paid :- ",net)

def Goldfun(g,p):
    total=g*p
    wastage=total*0.1
    gst=(total+wastage)*0.03
    net=total+wastage+gst
    print("The total amount to be paid :- ",net)

def Platinumfun(g,p):
    total=g*p
    wastage=total*0.14
    gst=(total+wastage)*0.03
    net=total+wastage+gst
    print("The total amount to be paid :- ",net)
def Diamondfun(g,p):
    total=g*p
    wastage=total*0.15
    gst=(total+wastage)*0.03
    net=total+wastage+gst
    print("The total amount to be paid :- ",net)

if jewel=='Silver':
    Silverfun(grams,price)
elif jewel=='Gold':
    Goldfun(grams,price)
elif jewel=='Platinum':
    Platinumfun(grams,price)
elif jewel=='Diamond':
    Diamondfun(grams,price)
else:
    print("Invalid Type")
