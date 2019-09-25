import calendar
import datetime
import colorama

cal = calendar.Calendar(6)
today = datetime.date.today()
monthdays = [x for x in cal.itermonthdays2(today.year, today.month)]

calstr = ""
calstr += today.strftime("%B, %Y")
calstr += "\n"
calstr += "%+6s" % "sun"
calstr += "%+6s" % "mon"
calstr += "%+6s" % "tue"
calstr += "%+6s" % "wed"
calstr += "%+6s" % "thu"
calstr += "%+6s" % "fri"
calstr += "%+6s" % "sat"
calstr += "\n"

week = 1
iday = 0
while iday < len(monthdays):
    for _ in range(7):
        day = monthdays[iday][0]
        if  day == 0:
            calstr += "%+6s" % ""
        else:
            if today.day == day:
                calstr += colorama.Fore.GREEN + "%+6s" % str(day)
                calstr += colorama.Style.RESET_ALL
            else:
                calstr += "%+6s" % str(day)
        iday += 1
    calstr += "\n"
    week += 1

print(calstr)
