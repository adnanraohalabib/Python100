def leap_year(year):
    if year%4 ==0 and year % 400 != 0:
        return True
    else:
        return False


print(leap_year(2024))
