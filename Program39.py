s=input("Enter a sentence :- ")
x=input("Enter the word to be found and replaced :- ")
y=input("Enter a replacement word :- ")
original_s=s
s=s.lower()
x=x.lower()
l=s.split(' ')
if x not in l:
    print("Not Found")
else:
    print(len(s))
    print(len(x))
    print(len(y))
    print(s.index(x))
    original_s=original_s.replace(x,y)
    print(original_s)