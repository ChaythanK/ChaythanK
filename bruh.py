silent_bid={}
print("WELCOME!!")
print("To silent BIDDING!")
desicion=str(input("would you like to particapate?, ")).strip().lower()
while desicion=="yes":
    name=str(input("what is your name?, ")).strip()
    bid=float(input("and your bid is?, $"))
    silent_bid[name]=bid
    desicion=str(input("any other bidders?, ")).strip().lower()
    inverse = [(value, key) for key, value in silent_bid.items()]
print("The highest bidder is",max(inverse)[1],"with a bid of",max(inverse)[1])
