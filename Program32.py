phy=set()
math=set()
sci=set()
p_pass=0
m_pass=0
s_pass=0
p_fail=0
m_fail=0
s_fail=0
N=int(input("Enter the no of students whose marks are to be entered :- "))
for i in range(N):
    a=int(input("Enter Physics MArks :- "))
    phy.add(a)
    if a>=50:
        p_pass=p_pass+1
    else:
        p_fail=p_fail+1
for j in range(N):
    b=int(input("Enter the Mathematics Marks : -"))
    math.add(b)
    if b>=50:
        m_pass=m_pass+1
    else:
        m_fail=m_fail+1
for k in range(N):
    c=int(input("Enter Science Marks :- "))
    sci.add(c)
    if c>=50:
        s_pass=s_pass+1
    else:
        s_fail=s_fail+1
print("No. of Pass in Physics :-",p_pass)
print("No. of Failure in Physics :-",p_fail)
print("No. of Pass in Mathematics :-",m_pass)
print("No. of Failure in Mathematics :-",m_fail)
print("No. of Pass in Science :-",s_pass)
print("No. of Failure in Science :-",s_fail)