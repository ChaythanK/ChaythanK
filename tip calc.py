print("welcome to tip calculator")
bill=float(input("what is your bill, may I ask?, "))
split=float(input("how many people are you splitting the bill with?, "))
tip=float(input("how much tip would you like to give?,10%, 12% or 15% "))
cost=(bill+(bill*tip/100))/split
print("you need to pay",cost)
