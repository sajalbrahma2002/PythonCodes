p=input("Enter the password :- ")
len_p=len(p)
if len_p>=8 and len_p<=15:
    count_upper=0
    count_lower=0
    count_num=0
    count_symbol=0
    for i in range(0,len_p):
        if (p[i]>='A' and p[i]<='Z'):
            count_upper=count_upper+1
        elif (p[i]>='a' and p[i]<='z'):
            count_lower=count_lower+1
        elif (p[i]>='0' and p[i]<='9'):
            count_num=count_num+1
        else:
            count_symbol=count_symbol+1
    if (count_upper>=1 and count_lower>=1 and count_num>=1 and count_symbol>=1):
        print("Valid")
    else:
        print("Invalid")
else:
    print("Invalid")