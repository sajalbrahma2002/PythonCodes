N=int(input("Enter the number of students whose details are to be stored in file :- "))
fo=open("student_detail.txt","w")
for i in range(0,N):
    name=input("Enter the name of the student :- ")
    mark1=int(input("Enter the mark1 :- "))
    mark2=int(input("Enter the mark2 :- "))
    mark3=int(input("Enter the mark3 :- "))
    total=mark1+mark2+mark3
    average=total/3
    fo.write(name+"  "+str(mark1)+"  "+str(mark2)+"  "+str(mark3)+"  "+str(total)+"  "+str(average)+"\n")
fo.close()
fo=open("student_detail.txt","r")
for i in range(0,N):
    l=fo.readline().split("  ")
    if l[5]>="90":
        for j in range(0,6):
            print(l[j],end=" ")
fo.close()