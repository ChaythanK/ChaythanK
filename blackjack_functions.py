import random
from ascii_art import card_king,card_queen,card_jack,card_ace,card_2,card_3,card_4,card_5,card_6,card_7,card_8,card_9,card_10,unknown_card,black_jack_ascii,black_jack

game="k"
account=1000
player_count = 0
player_cards = []
dealer_cards = []
dealer_count = 0
game = "u"
win="not won yet"
card_values = {
    "king": 10,
    "queen": 10,
    "jack": 10,
    "ace": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10
}
black_jack_ascii()
def bet(bet):
    global win
    global account
    if win=="won":
        account=+bet
    else:
        account=-bet

def show():
    global player_count
    global player_cards
    global game
    global dealer_cards
    global dealer_count
    global win
    while game != "over":
        if dealer_count > 17:
            if dealer_count > 21:
                print("you WON")
                print("good job")
                win="won"
                game = "over"
            elif dealer_count <= 21 and dealer_count > player_count:
                print("you lost, maybe always hitting IS a good strategy")
                game = "over"
            elif player_count<=21 and player_count>dealer_count:
                print("you won")
                print("nice job")
                win="won"
                game = "over"
            elif player_count == dealer_count:
                print("ooooooh so uneventfull")
                print("   Its a Draw....")
                win="won"
                game = "over"
        else:
            while dealer_count <= 17:
                dealer_hit()

identity = ["king", "queen", "jack", "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def deal():
    global player_count
    global player_cards
    global game
    global dealer_cards
    global dealer_count
    if game != "over":
        dealer_count=0
        dealer_cards=[]
        player_count = 0
        player_cards = []
        player_hit()
        player_hit()
        dealer_hit()
        unknown_card()
        print("")
        print("")
        print("player count,", player_count)
        print_card(player_cards)        

def dealer_hit():
    global dealer_count
    global dealer_cards
    global game
    if game != "over":
        if (dealer_count + 11)<= 21:
            card_values["ace"] = 11
        else:
            card_values["ace"] = 1
        A = random.choice(identity)
        dealer_cards.append(A)
        dealer_count += card_values[A]
        print("dealer count,", dealer_count)
        print_card(dealer_cards)



def blackyjacky():
    global dealer_count
    global dealer_cards
    global game
    if game != "over":
        if (dealer_count + 11)<= 21:
            card_values["ace"] = 11
        else:
            card_values["ace"] = 1
        A = random.choice(identity)
        dealer_cards.append(A)
        dealer_count += card_values[A]

        

def player_hit():
    ce = 'ace'
    global player_count
    global player_cards
    global game
    if game != "over":
        if (player_count + 11)<= 21:
            card_values["ace"] = 11
        else:
            card_values["ace"] = 1
        A = random.choice(identity)
        player_cards.append(A)
        player_count += card_values[A]
        
        if player_count > 21:
            if ce in player_cards and card_values[ace]==11:
                player_count-=10
            elif game != "over":
                print("GAME OVER")
                print("looks like you went over 21")
                game = "over"
        elif player_count==21:
            black_jack()
            input()
            while dealer_count <= 17:
                blackyjacky()
            if dealer_count==21:
                print("what a tragedy, you were so close to the ultimate win, but it ended in a draw")
            else:
                print("hurray!!!!!")
                print("YOU WON!!")
            

def print_card(card_list):
    for card in card_list:
        function_name = "card_"+card
        eval(function_name + "()")



input("press enter to continue")
j="yes"
while j=="yes" or j=="ye" or j=="y" or j=="sure;":
    game='not over'
    win="not won yet"
    deal()
    while game!="over":
        l=str(input(":>"))
        if l=="show":
             show()
        elif l=="hit":
            player_hit()
            print("count,", player_count)
            print(print_card(player_cards))
    print("")
    j=str(input("do you want to continue(yes/no)")).strip().lower()
print("see u later")
exit(0)




















