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

def distance_from_doomday(day,month,year):
    days_to_doomsday = 0

    for days in days_in_month:

        if days == '01' and month=='01':
            days_to_doomsday += int(days_in_month['02']) + (int(days_in_month[month])-int(day))
            return days_to_doomsday

        else:
            #We need to thin the dictionary down to only days we want
            new_days_in_month = {}
            for days in days_in_month:
                if days != '01' and int(days) <= int(month):
                    new_days_in_month.update({days:days_in_month[days]})
            return new_days_in_month
            #Pick up here
                
    
        
        

input_date = '01/01/2005'

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


    
print(distance_from_doomday(day,month,year))


##for days in days_in_month:
##    print(days)


##new_days = {}
##for days in days_in_month:
##    if days != '01' and int(days) < int("11"):
##        new_days.update({days:days_in_month[days]})
##print(new_days)







