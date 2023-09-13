T=input("Enter the type of two wheeler required :- ")
P=int(input("Enter  the  price of the two wheeler :- "))
if P>0:
    if (T=="Activa") or (T=="Shine") or (T=="Unicorn"):
        if(T=="Activa"):
            sum=(P-((P*5)/100))
        elif(T=="Shine"):
            sum=(P-((P*10)/100))
        else:
            sum=(P-((P*15)/100))
        print("The amount to be paid to buy the two wheeler :- ",sum)
    else:
        print("Invalid Type")
else:
    print("Enter positive value.")