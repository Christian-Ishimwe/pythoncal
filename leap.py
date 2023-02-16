#leap year calculator
year=int(input("Enter the year:\n"))
month=int(input("Enter the month:\n"))
def leap_year(year):
    # in_year=int(input("write the year:\n"))
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_month(year,month):
    if month>12:
        return  "invalid month!"
    days =[31,28,30,31,30,31,30,31,30,31,30,31]
    real_day=days[month-1]
    if leap_year(year) is True and month==2:
        return f"The month has 29 days"
    else:
        return f"the year is {year} has {real_day}  days"
conclusion =days_month(year,month)
print(conclusion)
