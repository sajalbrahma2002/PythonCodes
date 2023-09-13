x=int(input("Enter the percentage of marks scored by the student in CAT1(0-100) :- "))
y=int(input("Enter the percentage of marks scored by the student in CAT2(0-100) :- "))
z=int(input("Enter the number of assignments completed by the student out of 3 :- " ))
if x>=75 and y>=75 and z==3:
    print("The student is eligible to attend final exam. ")
else:
    print("The student is not eligible to attend final exam. ")    