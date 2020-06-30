def Calendar_Module():
    import calendar
    #           Plain Calender
    Text_Calendar = calendar.TextCalendar(calendar.SUNDAY)
    Text_String = Text_Calendar.formatmonth(2020, 6, 0, 0)
    print(Text_String)

    #           HTML Code
    HTML_Calendar = calendar.HTMLCalendar(calendar.SUNDAY)
    HTML_String = HTML_Calendar.formatmonth(2020,6)
    print(HTML_String)
    print("\n\nIteration\n\n")
    for i in Text_Calendar.itermonthdays(2020,6):
        print(i)
    print("List in calendar library")
    print(calendar.day_name[:])
    print(calendar.month_name[:])
    cal = calendar.monthcalendar(2020,7)
    print(cal[:])
    print(cal[0][3])
    print(calendar.MONDAY)
    print("Team Meeting")
    for m in range(1,13):
        calen = calendar.monthcalendar(2020, m)
        weekone = calen[0]
        weektwo = calen[1]
        if weekone[calendar.SUNDAY] != 0:
            meetday = weekone[calendar.SUNDAY]
        else:
            meetday = weektwo[calendar.SUNDAY]
        print("%10s %2d"%(calendar.month_name[m],meetday))
