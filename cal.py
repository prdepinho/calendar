import calendar
import datetime
import colorama
import sys
import getopt
from schedule import schedule, yearly

cal = calendar.Calendar(6)
today = datetime.date.today()

year = today.year
month = today.month
advance = 0

try:
    optlist, args = getopt.getopt(
            sys.argv[1:],
            'm:y:a:',
            ['month=', 'year=', 'advance=', 'help'])

except getopt.GetoptError as e:
    print(e)
    exit()

for o, a in optlist:
    if o in ['-m', '--month']:
        month = int(a)
        if month not in range(1, 13):
            print("Month must be between 1 and 12.")
            exit()
    elif o in ['-y', '--year']:
        year = int(a)
    elif o in ['-a', '--advance']:
        advance = int(a)
    elif o == '--help':
        print('%-40s %s' % ('-m, --month [month]:', 'Show the selected month.'))
        print('%-40s %s' % ('-y, --year [year]:', 'Show the selected year.'))
        print('%-40s %s' % ('-a, --advance [months]:', 'Show months in advance.'))
        exit()
    else:
        print('unhandled option: %s' % o)



def print_month(month, year):
    monthdays = [x for x in cal.itermonthdays2(year, month)]

    calstr = ""
    calstr += datetime.date(year, month, 1).strftime("%B, %Y")
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
            if day == 0:
                calstr += "%+6s" % ""

            else:
                if year in schedule and month in schedule[year]:
                    scheduled = datetime.date(year, month, day) in [datetime.date(year, month, d) for d in schedule[year][month]]
                    passed_schedule = scheduled and datetime.date(year, month, day) < today
                else:
                    scheduled = False
                    passed_schedule = False

                yearly_scheduled = month in yearly and day in yearly[month]


                if today == datetime.date(year, month, day):
                    if scheduled:
                        calstr += colorama.Back.WHITE + colorama.Fore.RED + colorama.Style.BRIGHT + "%+6s" % (">" + str(day))
                        calstr += colorama.Style.RESET_ALL
                        datesstr += "%6d: %s\n" % (day, schedule[year][month][day])
                    elif yearly_scheduled:
                        calstr += colorama.Back.WHITE + colorama.Fore.RED + "%+6s" % (">" + str(day))
                        calstr += colorama.Style.RESET_ALL
                    else:
                        calstr += colorama.Back.WHITE + colorama.Fore.BLACK + colorama.Style.BRIGHT + "%+6s" % (">" + str(day))
                        calstr += colorama.Style.RESET_ALL

                elif scheduled:
                    if passed_schedule:
                        calstr += colorama.Fore.BLUE + "%+6s" % str(day)
                        datesstr += colorama.Fore.BLUE + "%6d: %s%s\n" % (day, colorama.Style.RESET_ALL, schedule[year][month][day])
                    else:
                        calstr += colorama.Fore.RED + colorama.Style.BRIGHT + "%+6s" % str(day)
                        datesstr += colorama.Fore.RED + colorama.Style.BRIGHT + "%6d: %s%s\n" % (day, colorama.Style.RESET_ALL, schedule[year][month][day])
                    calstr += colorama.Style.RESET_ALL

                else:
                    if yearly_scheduled:
                        calstr += colorama.Fore.RED + "%+6s" % str(day)
                    else:
                        calstr += "%+6s" % str(day)
                    calstr += colorama.Style.RESET_ALL

                if yearly_scheduled:
                    datesstr += colorama.Fore.RED + "%6d: %s%s\n" % (day, colorama.Style.RESET_ALL, yearly[month][day])
                    calstr += colorama.Style.RESET_ALL

            iday += 1
        calstr += "\n"
        week += 1

    print(calstr)
    print(datesstr)


if __name__ == "__main__":
    print_month(month, year)
    if advance > 0:
        for a in range(0, advance):
            if (month + a) % 12 + 1 == 1:
                year += 1
            print_month((month + a) % 12 + 1, year)
