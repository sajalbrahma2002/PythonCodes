labtest={}
for i in range(3):
    test=input("Enter the name of the test : - ")
    min=int(input("Enter the minimun value for the test :- "))
    max=int(input("Enter the maximun value for the test :- "))
    labtest[test]=(min,max)
ptest=input("Enter the name of the observed test :- ")
pvalue=int(input("Enter the value for the observed test :- "))
range=labtest[ptest]
min1=range[0]
max1=range[1]
if min<=pvalue<=max:
    print("Normal...")
else:
    print("Abnormal...")
    