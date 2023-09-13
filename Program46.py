phno=input("Enter the mobile number:- ")
if(len(phno)==10 and phno.isdigit()):
    otp=input("Enter the one time password :- ")
    if(len(otp)==6 and otp.isdigit()):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")