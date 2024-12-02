#rock, paper, scissors, SHOOT!
import random
from importlib.metadata import pass_none
b=1
a=1
while b==a:
    choice_option = ['rock', 'paper', 'scissors']
    b = (str(input('rock, paper, scissors or shoot:'))).lower()
    a = random.choice(choice_option)
    print(a,'V/S',b)
    if a=='rock' and b=='scissors' or a=='scissors' and b=='paper' or a=='paper' and b=='rock':
        print('you lost')
    elif b=='rock' and a=='scissors' or b=='scissors' and a=='paper' or b=='paper' and a=='rock':
        print('you won')
    elif b==a:
        
        print('lets try again')
    else:
        print('i think you have a typo')

