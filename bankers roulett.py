import random
li=[]
n=int(input("how many people competing? "))
for i in range(0,n): 
    li_elements=str(input(":>"))
    li.append(li_elements)
print("Hmmmmmmmmmm...............")
A=random.randint(0,n)
print("I believe YOU,",li[A-1],"are the chosen one")
