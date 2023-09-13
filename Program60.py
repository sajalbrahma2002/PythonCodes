name=input("Enter the name of the student :- ")
mark1=int(input("Enter the mark1 :- "))
mark2=int(input("Enter the mark2 :- "))
mark3=int(input("Enter the mark3 :- "))
if mark1>=0 and mark1<=100 and mark2>=0 and mark2<=100 and mark3>=0 and mark3<=100:
    total=mark1+mark2+mark3
    average=total/3
    fo=open("sample.txt","w")
    fo.write(name+"\n"+str(mark1)+"\t"+str(mark2)+"\t"+str(mark3)+"\n"+str(total)+"\n"+str(average))
    fo.close()
    fo=open("sample.txt","r")
    print(fo.read())
    fo.close()
else:
    print("Invalid Mark")