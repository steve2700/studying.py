#code to check if a given year is a leap year or not in Python and explain the ocode logic.
def is_leap_year(year):
    if (year % 4 == 0 and year % 400 ==0 or year % 100 != 0):
        return True
    return False
    
    
year = 2021
if is_leap_year(year):
    print("the leap year",year)
else:
    print("this is not a leap year",year)
