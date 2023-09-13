a=input("Enter a String :- ")
switch=0
k=len(a)-1
if(len(a)==0):
    print("Palindrome")
for i in range(0,len(a)//2):
    if(a[i].lower()==a[k].lower()):
        pass
    else:
        switch=0
    k=k-1
if(switch==0):
    print("Palindrome")
else:
    print("Not a Palindrome")