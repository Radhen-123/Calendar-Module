def Time_Module():
    import datetime

    #       All Functions for Today
    Today = datetime.datetime.today()
    print("Todays Date And Time: ", Today)
    Date = Today.date()
    Time = Today.time()
    Month = Today.month
    Year = Today.year
    Day = Today.day
    Time_Parts = Today.time()
    WeekdayList = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    Weekday = Today.weekday()
    print("Date: ", Date)
    print("Time: ", Time)
    print("Year: ", Year)
    print("Month: ", Month)
    print("Day: ", Day)
    print("Weekday: ", WeekdayList[Weekday])
    print("Time Hour:", Time_Parts.hour, " Minute: ", Time_Parts.minute, " Seconds: ", Time_Parts.second,
          " Microsecond: ", Time_Parts.microsecond)
    # Another Way
    Another_Now = datetime.datetime.now()
    print("By Different way: ", Another_Now)
    Time_Another = datetime.datetime.time(datetime.datetime.now())
    print("Time by another way: ", Time_Another)
    #       Today Functoin Gets Over

    #           Formatting DateTime

    print("Formate with % operation: ", Today.strftime("%a WeekDays %A, %d Date %D, %b Months %B, %y Year %Y"))
    #           Formate for specific Location
    print(Today.strftime("Local Date and Time: %c"))
    print(Today.strftime("Local Date: %x "))
    print(Today.strftime("Local time: %X "))
    #           Formate Time
    print(Today.strftime("Current time 12 Hour formate: %I:%M:%S %p"))
    print(Today.strftime("24 Hour Formate time: %H:%M"))

    #           Perform Math
    print(datetime.timedelta(days=365, hours=5,minutes=60))
    AfterYear = Today + datetime.timedelta(days=365)
    print(AfterYear.strftime("One Year From Now: %A,%d,%B,%Y"))
    Calculate = Today + datetime.timedelta(days=2, weeks=3, hours=4, minutes=35, seconds=55, milliseconds= 55)
    print(Calculate.strftime("Future Calculation: %A,%d,%B,%Y"))

    #               Past Calculation
    LastYear = Today - datetime.timedelta(days=365)
    print(LastYear.strftime("Last Year From Now was: %A,%d,%B,%Y"))
    CalculatePast = Today - datetime.timedelta(days=2, weeks=3, hours=4, minutes=35, seconds=55, milliseconds=55)
    print(CalculatePast.strftime("Past Calculation :%A,%d,%B,%Y"))
    #       Assign Date
    DateOfBirth = datetime.date(day=6, month=12, year=2020)
    print(DateOfBirth.strftime("%A,%d,%B,%Y"))
