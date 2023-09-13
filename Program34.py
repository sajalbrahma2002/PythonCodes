s=input("Enter the sentence to check for vowels :- ")
count_a=0
count_e=0
count_i=0
count_o=0
count_u=0
for i in range(len(s)):
    if(s[i]=='a'):
        count_a=count_a+1
    elif(s[i]=='e'):
        count_e=count_e+1
    elif(s[i]=='i'):
        count_i=count_i+1
    elif(s[i]=='o'):
        count_o=count_o+1
    elif(s[i]=='u'):
        count_u+count_u+1
    else:
        pass
if (count_a==0) and (count_e==0) and (count_i==0) and (count_o==0) and (count_u==0):
    print("None")
if(count_a>0):
    print("a is",count_a)
if(count_e>0):
    print("e is",count_e)
if(count_i>0):
    print("i is",count_i)
if(count_o>0):
    print("o is",count_o)
if(count_u>0):
    print("u is",count_u)

