s=input("Enter a string :- ")
dict_alpha={}
for i in s:
    alpha=s.count(i)
    dict_alpha[i]=alpha
max=0
for j in dict_alpha:
    if(max<dict_alpha[j]):
        max=dict_alpha[j]
for k in dict_alpha:
    if(max==dict_alpha[k]):
        print(k,max)
        