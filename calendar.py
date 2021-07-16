days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]
#year = int(input("Input the year:"))
def is_leap_year(year):
    if year % 4 == 0:
        days_in_feb = 29
    else:
        days_in_feb = 28

    return days_in_feb

def first_year_day(year):
    base_year_day = days[1]
    base_year = 1900

    if year == base_year:
        return base_year_day
    else:
        previous_year_day = base_year_day
        for years in range(base_year + 1, year + 1):
            previous_year = years - 1
            if previous_year % 4 == 0:
                if previous_year % 100 == 0 and previous_year % 400 == 0:
                    if previous_year_day == days[5]:
                        previous_year_day = days[days.index(previous_year_day) - 5]
                    elif previous_year_day == days[6]:
                        previous_year_day = days[days.index(previous_year_day) - 5]
                    else:
                        previous_year_day = days[days.index(previous_year_day) + 2]
                elif previous_year % 100 == 0 and previous_year % 400 != 0:
                    if previous_year_day == days[6]:
                        previous_year_day = days[0]
                    else:
                        previous_year_day = days[days.index(previous_year_day) + 1]
                else:
                    if previous_year_day == days[5]:
                        previous_year_day = days[days.index(previous_year_day) - 5]
                    elif previous_year_day == days[6]:
                        previous_year_day = days[days.index(previous_year_day) - 5]
                    else:
                        previous_year_day = days[days.index(previous_year_day) + 2]
            else:
                if previous_year_day == days[6]:
                    previous_year_day = days[0]
                else:
                    previous_year_day = days[days.index(previous_year_day) + 1]
        return previous_year_day

def get_days_range(date, month, year):
    if month == 1:
        days_range = date
        return days_range
    else:
        months_range = [x for x in range(1,month)]
        days_range = 0
        for x in months_range:
            if x in [1, 3, 5, 7, 8, 10, 12]:
                max_month_days = 31
            elif x == 2:
                max_month_days = is_leap_year(year)
            else:
                max_month_days = 30

            days_range = days_range + max_month_days

        days_range = days_range + date
        return days_range

def which_day():
    year = int(input("Input the year:"))
    while len(str(year)) != 4 or year < 1970:
        print("The year must be a 4 digit number and greater than or equal to 1970.")
        year = int(input("Input the year:"))

    month = int(input("Input the month as a valid integer from 1 to 12:"))
    while len(str(month)) > 2 or len(str(month)) < 1 or month < 1 or month > 12:
        print("The month must be a valid integer from 1 to 12")
        month = int(input("Input the month as a valid integer from 1 to 12:"))

    date = int(input("Input a valid date:"))
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_month_days = 31
    elif month == 2:
        max_month_days = is_leap_year(year)
    else:
        max_month_days = 30

    while date > max_month_days:
        print("The date is out of range.\n"
              f"The valid dates for the month of {months[month - 1]} is a range from 1 to {max_month_days}")
        date = int(input("Input a valid date:"))

    new_years_day = first_year_day(year)

    range_of_days = get_days_range(date, month, year)
    previous_day = new_years_day

    if month == 1 and date == 1:
        return new_years_day
    else:
        for day in range(2, range_of_days + 1):
            if previous_day == days[6]:
                previous_day = days[0]
            else:
                previous_day = days[days.index(previous_day) + 1]
        return previous_day

print(which_day())


