import leap_year_calc
from leap_year_calc import is_a_leap
from leap_year_calc import leap_year
print(leap_year_calc.leap_year.__doc__) 
print("welcome to the days of the year calculator")
r=int(input("what is the year?, "))
a=leap_year(r)
print(a)
print("which means, the days in the year are " + ("366" if "is a leap year" in a else "365"))
