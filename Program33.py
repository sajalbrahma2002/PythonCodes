N=int(input("Enter the no of person for the ticket booking in ABC theme park :- "))
group1=set()
group2=set()
group3=set()
count1=0
count2=0
count3=0
sum1=0
sum2=0
sum3=0
avg1=0
avg2=0
avg3=0
if N>0:
    for i in range(N):
        age=int(input("Enter age of the person :- "))
        if age>0:
            if 1<=age<=10:
                group1.add(age)
                count1=count1+1
                sum1=sum1+age
            elif 11<=age<=60:
                group2.add(age)
                count2=count2+1
                sum2=sum2+age
            else:
                group3.add(age)
                count3=count3+1
                sum3=sum3+age
        else:
            print("Invalid Input")
    avg1=float(sum1/count1)
    avg2=float(sum2/count2)
    avg3=float(sum3/count3)
    print("Group 1 count ",count1)
    print("Group 2 count ",count2)
    print("Group 3 count ",count3)
    print("Group 1 Avearge ",avg1)
    print("Group 2 Average ",avg2)
    print("Group 3 Average ",avg3)
else:
    print("Invalid Input")