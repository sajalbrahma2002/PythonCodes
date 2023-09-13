s=str(input("Enter the Sentence :- "))
x=input("Enter the word to be replaced :- ")
original_s=s
s=s.lower()
x=x.lower()
l=s.split(" ")

def Compute(a,b,c):
    print("The length of the Sentence :- ",len(a))
    print("The length of the word to be replaced from the sentence :- ",len(b))
    print("The length of the word to be replaced with ",b," in the sentence is :- ",len(c))
    print("The position of the replecement word in the sentence :- ",a.index(b))
    t=a.replace(b,c)
    print("The sentence after the word is replaced is :- ",t)

if x in l:
    y=input("Enter the word to be replaced with in the sentence :- ")
    Compute(original_s,x,y)
else:
    print("Not Found...")