N=int(input("Enter the no of students to be entered in the list :- "))
stud_list=[]
if N>0:
    for i in range(N):
        name=input("Enter the name of the student :- ")
        stud_name=str.lower(name)
        stud_list.append(stud_name)
else:
    print("Invalid Input")
for j in range(len(stud_list)):
    for k in range(j+1,len(stud_list)):
        if(stud_list[j]>stud_list[k]):
            temp=stud_list[k]
            stud_list[k]=stud_list[j]
            stud_list[j]=temp
        else:
            pass
for m in range(len(stud_list)):
    print(str.capitalize(stud_list[m]))