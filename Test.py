# from CalendarClasses import Event, Day, Month
from CalendarClasses import *

e1 = Event(12, 10, 14, 10, 'Meegin with Co-op advisor', 'Cestar College')
e2 = Event(10, 4, 16,  10, 'Graduation', 'Lambton College')
e3 = Event(20, 00, 22, 00, 'Watching Movie', 'Fairview Mall')
e4 = Event(7, 0, 8, 00, 'Meeting for breakfast', 'Restaurant')

d = Day('Monday', 12, 'October')
d.addEvent(e1)
d.addEvent(e2)
# d.displayAllEvents()

d2 = Day('Wednesday', 14, 'October')
d2.addEvent(e3)
d2.addEvent(e4)

m = Month('October', 10, 31)
m.addDay(d)
m.addDay(d2)
m.displayEvents()
