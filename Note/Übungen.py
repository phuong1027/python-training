""" 
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc. Task Given a year, return the century it is in.
"""
def centuryFromYear(year):
    # if year % 100 == 0:
    #     century = year // 100
    # else:
    #     century = (year // 100) + 1 # chia nguyen de lay 2 so dau
    # return century
    return (year + 99) // 100

year = int(input('Enter a year: '))
print('Century of the year', year, 'is:', centuryFromYear(year))

""" def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1 """