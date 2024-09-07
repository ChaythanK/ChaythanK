data = {
    "price per kg kiwis": 7,
    "price per kg uranium 235": 189,
    "price per 1 gram of rhodium":164,
    "price per kg elephant ivory": 3000,
    "price per 0.25kg gold": 18982,
    "luxury japanese bonsai scissors": 35000,
    "price per kg musk": 45000,
    "price per kg ambergris (whale dung)": 50000,
    "price per kg lab grown mammoth meat": 100000,
    "price of a Lamborghini Urus": 250500,
    "price per kg golden or weaver spider silk": 500000,
    "gucci net worth": 18900000000,
    "louis vuitton net worth": 234000000000,
    "global economy value": 100662950000,
    "price per gram antimatter": 62500000000000
}
def printpairs(dictionary):
    keys = list(dictionary.keys())
    i=0
    while i<len(keys)-1:
        n=i+1
        print(keys[i])
        print(keys[n])
        # Ask for user input
        user_input="higher"
        while user_input!="higher" or user_input!="lower":
            user_input = str(input("Enter 1 to print the next pair of keys, or any other key to exit: "))
            if user_input=="higher" or user_input=="lower":
                break
        if user_input == "higher" and dictionary[keys[i]]<dictionary[keys[i + 1]] or user_input=="lower" and dictionary[keys[i]]>dictionary[keys[i + 1]]:
            i +=1

printpairs(data)
