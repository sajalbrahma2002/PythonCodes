s=input("Enter a string :- ")
b=input("Enter the character whose frequency to be found in the string :- ")
count=0
for i in range(0,len(s)):
    if(b==s[i]):
        count=count+1
print(count)
print(s[::-1])