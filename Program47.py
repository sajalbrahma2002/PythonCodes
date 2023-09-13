import re
user_id=input("Enter the user id :- ")
password=input("Enter the password :- ")
captcha_code=input("Enter the captcha code :- ")
if(len(user_id)==9):
    if re.match("21.*[BCE|BPS|BPI][0-9]{4}$",user_id):
        if (len(password)==5):
            if re.match("[0-9]{2}[a-zA-Z]{3}$",password):
                if (len(captcha_code)==6):
                    if re.match("[A-Za-z]{2}[0-9]{1}[a-zA-Z]{1}[0-9]{1}[A-Za-z]{1}$",captcha_code):
                        print("Valid")
                    else:
                        print("Invalid")
                else:
                    print("Invalid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")