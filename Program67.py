fo=open("detail.txt","w")
for x in range(0,4):
    details=input("Enter the details :- ")
    fo.write(details+"\n")
fo.close()
lines=0
words=0
word_num=0
word_letter=0
fo=open("detail.txt","r")
for y in range(0,4):
    z=fo.readline().lower()
    lines=lines+1
    l=z.split()
    length=len(l)
    words=words+length
    for i in l:
        if i.isalpha():
            word_letter=word_letter+1
        elif i.isnumeric():
            word_num=word_num+1
        else:
            pass
print("Total lines in the file :- ",lines)
print("Total words in the file :- ",words)
print("Total words having only numbers :- ",word_num)
print("Total words having only letters :- ",word_letter)
fo.close()