def show(s):
    print "the word is ",
    for i in s:
        print i,
import random
random_word=random.choice(['father','brother','good','bad','class','github'])
t=list(random_word)
s=['*']
s=s*len(t)
show(s)
print " its length is ",len(t)
c=len(t)
d=0
while c>0 and d<(len(t)):
    print "you have ",c," attempts left"
    ch=raw_input("Enter a char(lowercase) : ")
    f=0
    for i in range(len(t)):
        if t[i]==ch and s[i]=='*':
            print "correct..."
            s[i]=t[i]
            d=d+1
            f=1
            break
    if f==0:
        print "try again..."
        c-=1
    show(s)
if d==len(t):
    print "\nCongratulations! you got the word"
else:
    print "\n\tGAME OVER!!!"
