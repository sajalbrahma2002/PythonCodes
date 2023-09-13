T=input("Enter the type of jewellery(Earrings,Bracelets,Necklace) :- ")
W=int(input("Enter the weight of the jewellery needed (in grams):- "))
P=int(input("Enter the price for a gram of the jewellery :- "))
if(T=="Earrings") or (T=="Bracelets") or (T=="Necklace"):
    if(W>0) and (P>0):
        total=W*P
        if(T=="Earrings"):
            wastage=((total*5)/100)
            total1=total+wastage
        elif(T=="Bracelets"):
            wastage=((total*10)/100)
            total1=total+wastage
        else:
            wastage=((total*14)/100)
            total1=total+wastage
        amount=int(total1+(total1*3/100))
        print("The amount to be paid :- ",amount)    
    else:
        print("Invalid Input")
else:
    print("Invalid Type")