import random
total_lives=5
li=[]
l=[]
ct=0
Q=1
print("welcome, to single player hangman")
genre="animals"
animals = [
    "alpaca", "wombat", "tarantula", "leopard", "jaguar", "oyster", "seagull", "pangolin", "poodle", "coyote",
    "lizard", "meerkat", "caracal", "seahorse", "antelope", "bison", "octopus", "flamingo", "buffalo", "chimpanzee",
    "gorilla", "hamster", "hedgehog", "iguana", "jackal", "kangaroo", "koala", "lynx", "mongoose", "narwhal",
    "ocelot", "penguin", "cobra", "raccoon", "salamander", "tortoise", "cheetah", "vicuna", "walrus", "woodpecker",
    "albatross", "tree frog", "donkey", "emu", "finch", "gecko", "heron", "impala", "cardinal", "thestral",
    "lapwing", "mallard duck", "flying fox", "ostrich", "pangolin", "quail", "raven", "osprey", "lemur", "anemone",
    "vulture", "wallaby", "spider monkey", "millipede", "guinea fowl", "basilisk lizard", "baboon", "camel", "wolverine", "eagle",
    "falcon", "vole", "heron", "black widow", "jaguar", "clown fish", "lobster", "manatee", "newt", "orca",
    "python", "cobra", "rattlesnake", "sparrow", "tapir", "anemone", "viper", "wombat", "silverfish", "guinea pig",
    "bandicoot", "caribou", "dingo", "echidna", "fossa", "gorilla", "hyena"
]

A=random.randint(0,len(animals))
if genre=="animals":
    for letter in animals[A]:
        li.append(letter)
    for i in range(len(li)):
        l.append('_')
    print("Total Lives are:",total_lives)
    while l!=li:
        guese=str(input(":>"))
        guese=guese.lower()
        for i in range(len(li)):
            if guese==li[i]:
                l[i]=guese                
            elif guese!=i:
                Q*=1/len(li)
        if Q==1:
            total_lives-=1
        Q=1
        ct+=1
        print(l)
        print(li)
        print(total_lives)
        if total_lives<1:
            print("GAME OVER")
            break
            if i==li:
                print("you won!")
    if i==li:
                print("you won!")
print("you either won or lost")

