N=int(input("Enter the no of patients whose details are to be stored :- "))
fo=open("patient.txt","w")
for i in range(0,N):
    name=input("Enter patient's name :- ")
    age=input("Enter patient's age :- ")
    reason=input("Enter patien's reason :- ")
    fo.write(name+" "+age+" "+reason+"\n")
fo.close()
fo=open("patient.txt","r")
for i in range(0,N):
    l=fo.readline().split()
    if l[2]=='Fever':
        for j in l:
            print(j,end=" ")
fo.close()