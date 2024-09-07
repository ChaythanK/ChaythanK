import random
lis=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
li=[]
l = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '/', '.', '<', '>', '?', '\\', '|', '{', '}', '[', ']', ',']
lib=[]
print(len(l))
letter_numb=int(input("number of letters, "))
numb_numb=int(input("number of numbers, "))
symbol_numb=int(input("number of symbols, "))
for i in range(letter_numb):
    a=random.randint(0,25)
    b=str(lis[a])
    li.append(b)
for i in range(numb_numb):
    a=random.randint(0,9)
    b=str(a)
    li.append(b)
for i in range(symbol_numb):
    a=random.randint(0,27)
    b=str(l[a])
    li.append(b)
for i in range(0,len(li)-1):
    A=random.randint(0,len(li)-1)
    li.append(li[A])
    li.remove(li[A])
print(li)

