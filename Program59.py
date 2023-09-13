salary=int(input("Enter the salary  of the person :-"))
gender=input("Enter the gender of the person (Male/Female):- ")

def taxfun(salary,gend):
    if gend=="Male":
        a=taxmale(salary)
    else:
        a=taxfemale(salary)
    print("The tax to be paid is :-",a)

def taxmale(sal):
    if sal<=250000:
        taxsal=0
    elif sal>250000 and sal<=500000:
        sal1=sal-250000
        taxsal=0+(sal1*0.05)
    elif sal>500000 and sal<=1000000:
        sal1=sal-500000
        taxsal=0+12500+(sal1*0.2)
    else:
        sal1=sal-1000000
        taxsal=0+12500+100000+(sal1*0.3)
    return taxsal

def taxfemale(sal):
    if sal<=250000:
        taxsal=0
    elif sal>250000 and sal<=500000:
        sal1=sal-250000
        taxsal=0+(sal1*0.05)
    elif sal>500000 and sal<=1000000:
        sal1=sal-500000
        taxsal=0+12500+(sal1*0.1)
    else:
        sal1=sal-1000000
        taxsal=0+12500+100000+(sal1*0.2)
    return taxsal

if gender=="Male" or gender=="Female":
    taxfun(salary,gender)