import calendar
import datetime
import colorama
from schedule import schedule

cal = calendar.Calendar(6)
today = datetime.date.today()

year = today.year
month = today.month
monthdays = [x for x in cal.itermonthdays2(year, month)]

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

datesstr = ""

week = 1
iday = 0
while iday < len(monthdays):
    for _ in range(7):
        day = monthdays[iday][0]
        # import pdb; pdb.set_trace()
        if day == 0:
            calstr += "%+6s" % ""

        else:
            scheduled = datetime.date(year, month, day) in [datetime.date(year, month, d) for d in schedule[year][month]]

            if today == datetime.date(year, month, day):
                calstr += colorama.Fore.GREEN + "%+4s" % ">"
                calstr += colorama.Style.RESET_ALL

                if scheduled:
                    calstr += colorama.Fore.RED + "%s" % str(day)
                    calstr += colorama.Style.RESET_ALL
                    datesstr += "%6d: %s\n" % (day, schedule[year][month][day])
                else:
                    calstr += colorama.Fore.GREEN + "%s" % str(day)
                    calstr += colorama.Style.RESET_ALL

            elif scheduled:
                calstr += colorama.Fore.RED + "%+6s" % str(day)
                calstr += colorama.Style.RESET_ALL
                datesstr += "%6d: %s\n" % (day, schedule[year][month][day])

            else:
                calstr += "%+6s" % str(day)

        iday += 1
    calstr += "\n"
    week += 1

print(calstr)
print(datesstr)
