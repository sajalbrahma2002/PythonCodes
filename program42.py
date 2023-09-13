import re
s=input("Enter the Email ID :- ")
if re.match("[A-Za-z0-9]*[@].*[.com|.in|.org|.edu|.net|.mil]$",s):
    print("Valid")
else:
    print("Invalid")