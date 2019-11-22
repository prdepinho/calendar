# calendar
A simple calendar app.

The current day highlighted in white.

To add a schedule, edit the dicionary at schedule.py and the
program will show it in red in the calendar, and the description
will be in the bottom.

Yearly scheduling is also supported.

To see the current month:

```
py cal.py
```

To see a certain month (october in this case):

```
py cal.py -m 10
```

To see a certain month in a certain year:

```
py cal.py -m 10 -y 2020
```

To see a couple of months in advance in additioin to the chosen month:

```
py cal.py -m 10 -y 2020 -a 2
```
