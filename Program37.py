name=input("Enter the name of the student whose grade is to found :- ")
mark=[]
grade=[]
sum=[]
detail={}
total=0
average=0
for i in range(4):
    marks=int(input("Enter marks of the student :- "))
    if(marks>0)and (marks<=100):
        if(marks<50):
            mark.append(marks)
            total=total+marks
            grade.append("fail")
        elif(60>marks>=50):
            mark.append(marks)
            total=total+marks
            grade.append("e")
        elif(70>marks>=60):
            mark.append(marks)
            total=total+marks
            grade.append("d")
        elif(80>marks>=70):
            mark.append(marks)
            total=total+marks
            grade.append("c")
        elif(90>marks>=80):
            mark.append(marks)
            total=total+marks
            grade.append("b")
        elif(95>marks>=90):
            mark.append(marks)
            total=total+marks
            grade.append("a")
        else:
            mark.append(marks)
            total=total+marks
            grade.append("s")
    else:
        print("Enter marks between 0 and 100..")
        exit()
average=float(total/4)
sum=mark+grade
sum.append(total)
sum.append(average)
detail[name]=sum
print(detail)

