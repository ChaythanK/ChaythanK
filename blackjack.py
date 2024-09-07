import random
A=random.randint(0,100)
print("welcome to gues the number")

print("im thinking of a number from one to a hundred")
decision="eas"
while decision!="hard" or decision!="easy":
    decision=str(input("do you want to play hard or easy:")).strip().lower()
    print(decision)
    if decision=="hard":
        break
    elif decision=="easy":
        break
if decision=="hard":
    ct=5
    for i in range(5):
        print("chances left,",ct)
        guess=int(input("guess the number, "))
        if guess==A:
             print("you guessed it! The correct number was indeed",A)
             break
        elif guess<A:
            print("The number is higher than",guess)
        elif guess>A:
             print("the number is lower than",guess)
        ct-=1
        
elif decision=="easy":
    ct=10
    for i in range(10):
        print("chances left",ct)
        guess=int(input("guess the number, "))
        if guess==A:
            print("you guessed it! The correct number was indeed",A)
            break
        elif guess<A:
            print("The number is higher than",guess)
        elif guess>A:
            print("the number is lower than",guess)
        ct-=1
