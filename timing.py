
#function taking in 2 parameters hr and period and returns a meal recommendation
def mealrec(hr,period):
    if period=='AM':
        if hr>=5 and hr<=11:
            return("Breakfast TIME!!")
        else:
            return("It's too early! Go TO BED!!")
    elif period=="PM":
        if hr==12 or hr<=3:
            return("Lunch TIME!!")
        if hr==4 or hr<=6:
            return("Snack TIME!!")
        if hr==7 or hr<=10:
            return("Dinner TIME!!")
        else:
            return("It's too late, GO TO BED!!")
    else:
        return("Weird.., can't recognize input")
#print(mealrec(12,'PM'))