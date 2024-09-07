A="is a leap year"
B="is not a leap year"
is_a_leap=False
def leap_year(year):
    """gasikomalala"""
    if year%4==0:
        if year%100==0:
            if year%400:
                is_a_leap=True
                return year,A
            else:
                is_a_leap=True
                return year,B
        else:
            is_a_leap=False
            return year,A
    else:
        is_a_leap=False
        return year,B
    

