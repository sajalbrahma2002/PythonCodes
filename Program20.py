S=input("Enter the text :- ")
T=int(input("Enter the digit to be added in plain text after converted to cipher text :- "))
h=' '
for i in S:
    h+=chr(ord(i)+T)
print("The cipher text is :- ",h)
