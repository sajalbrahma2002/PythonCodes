a=0
e=0
i=0
o=0
u=0
fo=open("vowel.txt","w")
for x in range(0,4):
    string=input("Enter the details :- ")
    fo.write(string+"\n")
fo.close()
fo=open("vowel.txt","r")
for j in range(0,4):
    y=fo.readline().lower()
    for k in range(0,len(y)):
        if y[k]=="a":
            a=a+1
        elif y[k]=="e":
            e=e+1
        elif y[k]=="i":
            i=i+1
        elif y[k]=="o":
            o=o+1
        elif y[k]=="u":
            u=u+1
        else:
            pass
print("a is :- ",a)
print("e is :- ",e)
print("i is :- ",i)
print("o is :- ",o)
print("u is :- ",u)
fo.close()