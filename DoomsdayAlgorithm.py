def check_leap_year(year):
    year_ = int(year)
    if year_ % 4 != 0:
        return 0
    else:
        if year_ % 100 != 0:
            return 1
        else:
            if year_ % 400 == 0:
                return 1
            else:
                return 0

def this_doomsday(year):
    if check_leap_year(year) == 1:
        return '29/02/'+str(year)
    else:
        return '28/02/'+str(year)

##def distance_from_doomday(day,month,year):
##    days_to_doomsday = 0
##
##    for days in days_in_month:
##
##        if days == '01' and month=='01':
##            days_to_doomsday += int(days_in_month['02']) + (int(days_in_month[month])-int(day))
##            return days_to_doomsday
##
##        else:
##            #We need to thin the dictionary down to only days we want
##            new_days_in_month = {}
##            for days in days_in_month:
##                if days != '01' and int(days) <= int(month):
##                    new_days_in_month.update({days:days_in_month[days]})
##            #We want to get the number of days between the given date and doomsday
##
##            #Case for if the given date is in February
##            if month == "02":
##                days_to_doomsday = int(this_doomsday(year)[:2]) - int(day)
##                return days_to_doomsday
##            new_days_in_month.pop(month)
##            new_days_in_month.pop("02")
##
##            for days_ in new_days_in_month:
##                days_to_doomsday+= new_days_in_month[days_]
##            days_to_doomsday += int(day)+1
##            
##            return days_to_doomsday

def distance_from_doomday(day,month,year):
    days_to_doomsday = 0

    if month=='01':
        days_to_end_jan = 31-int(day)
        days_to_doomsday = days_to_end_jan + int(days_in_month['02'])+1
        return days_to_doomsday
    elif month=='02':
        days_to_doomsday = int(days_in_month['02']) - int(day)
        return days_to_doomsday
    else:
        #Thin down dictionary to only relevant months
        days_in_month.pop('01')
        days_in_month.pop('02')

        new_days_in_month = {}
        
        for months in days_in_month:
            if int(months) == int(month):
                break
            else:
                new_days_in_month.update({months:days_in_month[months]})
        days_to_doomsday += int(day) + sum([new_days_in_month[month] for month in new_days_in_month])+3
        
        print(days_to_doomsday)
        return days_to_doomsday
                
    
            
def day_from_days():
    #I need to add logic to get the anchor day for the century
    print(days_of_week[distance_from_doomday(day,month,year)%7])
    #return days_of_week[distance_from_doomday(day,month,year)]%7
                
#Cases
#Jan-Feb, non leap year. Passes
#Jan-Feb, leap year
#Mar-Dec, non leap year. Passes
#Mar-Dec, leap year. Fails
        
        
print(64%7)
input_date = '01/04/2004'

day = input_date[:2]
month = input_date[3:5]
year = input_date[-4:]

days_in_month = {"01":31,
                 "02":this_doomsday(year)[:2],
                 "03":30,
                 "04":30,
                 "05":31,
                 "06":30,
                 "07":31,
                 "08":31,
                 "09":30,
                 "10":31,
                 "11":30,
                 "12":31}
days_of_week = {0:'Friday',
                1:'Saturday',
                2:'Sunday',
                3:'Monday',
                4:'Tuesday',
                5:'Wednesday',
                6:'Thursday'}

    
#print(distance_from_doomday(day,month,year))
print(day_from_days())

##for days in days_in_month:
##    print(days)


##new_days = {}
##for days in days_in_month:
##    if days != '01' and int(days) < int("11"):
##        new_days.update({days:days_in_month[days]})
##print(new_days)

#print([days_in_month[days] for days in days_in_month)





