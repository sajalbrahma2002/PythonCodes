list_a=[]
N=int(input("Enter the no of patients name to be entered :- "))
def Getname(X,list_b):
    for i in range(0,X):
        s=input("Enter the patient name :- ")
        list_b.append(s)
    return(list_b)

def Sortname(list_d):
    for j in range(0,len(list_d)):
        for k in range(j+1,len(list_d)):
            if(list_d[j]>list_d[k]):
                temp=list_d[k]
                list_d[k]=list_d[j]
                list_d[j]=temp
            else:
                pass
    for m in range(0,len(list_d)):
        print(list_d[m])

if N>0:
    list_c=Getname(N,list_a)
    Sortname(list_c)
else:
    print("Invalid Input")