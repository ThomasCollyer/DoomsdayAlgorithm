def get_anchor_day(year):
    century = int(year[:2])
    anchor_days = {0:'Sunday',1:'Monday',2:'Tuesday',3:'Wednesday',
                   4:'Thursday',5:'Friday',6:'Saturday'}
    #doomsday_offset = floor(century/12) + (century % 12) + floor( (century % 12)/4)
    this_anchor_day = ((5*(century % 4))%7 +2)%7
    return this_anchor_day

def get_this_years_doomsday(year):
    tens_year = int(year[2:])
    q1 = tens_year//12
    r1 = tens_year %12
    q2 = r1 // 4
    total = q1 +r1 +q2 + get_anchor_day(year)
    return total % 7

def check_leap_year_correction(year):
    year_ = int(year)
    if year_ % 4 != 0:
        return 28
    else:
        if year_ % 100 != 0:
            return 29
        else:
            if year_ % 400 == 0:
                return 29
            else:
                return 28

def construct_day_order(anchor_index):
    initial_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    pre_index, post_index = initial_days[:anchor_index], initial_days[anchor_index:]
    new_days_order = post_index+pre_index
    return new_days_order
    #days_of_week = {}
    
    #new_days = list_reshuffle(week_days,anchor_index)
    #for i in range(7):
    #    days_of_week.update({i:new_days[i]})
    #return(days_of_week)

def distance_from_doomsday(day,month,year):
    days_in_month = {"01":31,
                 "02":check_leap_year_correction(year),
                 "03":31,
                 "04":30,
                 "05":31,
                 "06":30,
                 "07":31,
                 "08":31,
                 "09":30,
                 "10":31,
                 "11":30,
                 "12":31}

    #Now I want to count the number of days between given date and last day of feb
    #Get the sum of the number of days in the year
    if days_in_month["02"] == 28:
        days_of_year = 365
    else:
        days_of_year = 366

    #Get the position of the last day of February in the days of the year
    doomsday_position = days_in_month["01"] + days_in_month["02"]
    #print(doomsday_position, get_this_years_doomsday(year))

    #Get the order of days with this years Doomsday as day 0
    this_years_doomsday_index = get_this_years_doomsday(year)
    this_years_day_order = construct_day_order(this_years_doomsday_index)
   
    #Get the numerical position of the given day with the doomsday
    given_day_position = 0
    if (month != '01') and (month != '02'):
        for item in days_in_month:
            if item == month:
                break
            else:
                given_day_position += days_in_month[item]
        given_day_position += int(day)
    elif month == '01':
        given_day_position += int(day)
    elif month == '02':
        given_day_position += int(day) + days_in_month['01']

    dist_to_doomsday = given_day_position-doomsday_position

    #print(dist_to_doomsday)
    #print("Doomsday is " + str(this_years_doomsday_index))
    #print("This years day ordering is: ")
    #print(this_years_day_order)
    #print("The desried day's position is: " + str(given_day_position))
    #print("Doomsday's position is: "+ str(doomsday_position))
    #print("Distance to Doomsday is: " + str(dist_to_doomsday))

    #Why isn't the line below sufficient?
    #print(this_years_day_order[given_day_position%7])
    #print(this_years_day_order[dist_to_doomsday%7])
    return this_years_day_order[dist_to_doomsday%7]




input_date = '01/01/2004'

day = input_date[:2]
month = input_date[3:5]
year = input_date[-4:]


#print(distance_from_doomsday(day,month,year))
#distance_from_doomsday(day,month,year)
#Test the anchor day function
#print(get_anchor_day(year))

####################################
#Could be that dates in Jan or Feb are the issue
#Could be a leap year issue. The gap from Jan to the end of Feb is different than the same day in March
#Why? Because to go from 01/03/2004 you take 1 step back, its agnostic to leap years
#unlike Jan and Feb
####################################


#Test cases
tests = [('01/01/1900','Monday'),
         ('23/02/1904','Tuesday'),
         ('10/04/1921','Sunday'),
         ('31/12/2004','Friday'),
         ('14/04/1948','Wednesday'),
         ('27/08/2098','Wednesday'),
         ('27/02/2000','Sunday'),
         ('19/01/1992','Sunday'),
         ('03/02/1899','Friday'),
         ('05/08/1897','Thursday')]
for test in tests:
    input_date = test[0]
    day = input_date[:2]
    month = input_date[3:5]
    year = input_date[-4:]
    if test[1] == distance_from_doomsday(day,month,year):
        print("Correct")
    else:
        print("Incorrect")
