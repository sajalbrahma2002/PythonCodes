import math
print("The quadratic equation is of the form ax^2+bx+c=0 , enter the values of a,b,c")
a=int(input("enter the value of a :- "))
b=int(input("enter the value of b :- "))
c=int(input("enter the value of c :- "))
dis = b * b - 4 * a * c
sqrt_dis=math.sqrt(abs(dis))
if dis>0:
    print("Real and Different Roots")
    root1= ((-b +sqrt_dis)/(2*a))
    root2= ((-b-sqrt_dis)/(2*a))
    print("Root 1 =",root1)
    print("Root 2 =",root2)
elif dis==0:
    print("Real and Same Roots") 
    root3= (-b /(2*a))
    print(" Root = ",root3)
else:
    print("Complex Roots")
    root4=((-b/(2*a)),"+i",sqrt_dis)
    root5=((-b/(2*a)),"-i",sqrt_dis)
    print("Root 1 =",root4)
    print("Root 2 =",root5)

