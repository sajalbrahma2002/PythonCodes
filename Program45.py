import re
cust_id=input("Enter the customer id :-")
password=input("Enter the password :-")
if(len(cust_id)==10):
    if (re.match("[A-Z]{1}[0-9]{9}$",cust_id)):
        if(len(password)==5):
            if(re.match("[0-9]{2}[A-Za-z]{3}$",password)):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
