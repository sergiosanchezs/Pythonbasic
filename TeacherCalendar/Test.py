from CalendarCLasses import *

c = Calendar()

c.initializeCalendar()

c.addEvent(12, 10, 14, 30, "Graduation", "CeStar", 11, 5, 2019)
c.addEvent(13, 10, 15, 10, "MidTerm", "Lambton", 9, 2, 2020)

c.displayAllEventsInMonth(11, 2019)