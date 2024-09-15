#rock, paper siscors SHOOT
import random
from importlib.metadata import pass_none
b=1
a=1
while b==a:
    choice_option = ['rock', 'paper', 'siscors']
    b = (str(input('rock, paper, siscors or shoot:'))).lower()
    a = random.choice(choice_option)
    print(a,'V/S',b)
    if a=='rock' and b=='siscors' or a=='siscors' and b=='paper' or a=='paper' and b=='rock':
        print('you lost')
    elif b=='rock' and a=='siscors' or b=='siscors' and a=='paper' or b=='paper' and a=='rock':
        print('you won')
    elif b==a:
        
        print('lets try again')
    else:
        print('i think you have a typo')

