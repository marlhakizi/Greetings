from timing import mealrec
def test_time():
    assert(mealrec(12,'PM')=="Lunch TIME!!")
    assert(mealrec(1,'AM')=="It's too early! Go TO BED!!")
    assert(mealrec(3,'M')=="Weird.., can't recognize input")