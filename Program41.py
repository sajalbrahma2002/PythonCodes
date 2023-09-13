import re
s=input("Enter the PAN Number (10 characters) :- ")
if len(s)==10:
    if re.match("[A-Z]{5}[0-9]{4}[A-Z]{1}$",s):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")