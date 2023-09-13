import re
name=input("Enter the name of the proctee :- ")
regno=input("Enter the registration no of the proctee :-")
phno=input("Enter the mobile number :-")
if(name.isalpha()):
    if(len(regno)==9):
        if (re.match("21.*[BCE|BPS|BAI][0-9]{4}$",regno)):
            if(len(phno)==10 and phno.isdigit()):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")