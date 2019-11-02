class Event:

    def __init__(self, start_hr, start_min, finish_hr, finish_min, description, location):
        self.start_hr = start_hr
        self.start_min = start_min
        self.finish_hr = finish_hr
        self.finish_min = finish_min
        self.description = description
        self.location = location

    def displayEvent(self):
        result = "From " + str(self.start_hr) + ":" + str(self.start_min)
        result += " To " + str(self.finish_hr) + ":" + str(self.finish_min) + "\n"
        result += "Description: " + str(self.description) + "\n"
        result += "Location: " + str(self.location) + "\n"
        result += "------------------------------------------------------------"
        return result


class Day:


    def __init__(self, day_of_month):
        #self.name = name
        self.day_of_month = day_of_month
        self.events = []
       # self.month_belong_to = month_belong_to


    def addEvent(self, event):
        self.events.append(event)

    def displayAllEvents(self):
        if len(self.events) > 0:
            print("All events scheduled for " + str(self.day_of_month) )
            for i in self.events:
                print(i.displayEvent())


class Month:
    number_of_days = 30
    def __init__(self, name, month_of_year):
        self.name = name
        self.month_of_year = month_of_year

        if month_of_year == 2:
            number_of_days = 28
        elif month_of_year == 1 or month_of_year == 3 or month_of_year == 5 or month_of_year == 7 or month_of_year == 8 or month_of_year == 10 or month_of_year == 12:
            number_of_days = 31
        else:
            number_of_days = 30

    days = [] * number_of_days

    def addDay(self, day):
        self.days.insert(day.day_of_month-1, day)

    def displayEvents(self):
        for i in self.days:
            i.displayAllEvents()

class Year:

    months = [Month] * 12

    def __init__(self, year_number):
        self.year_number = year_number



class Calendar:

    def __init__(self):
        self.years = [Year] * 25

    def addYear(self, year):
        self.years.add(year)

    def initializeCalendar(self):
        #Creating years
        for i in range(2000, 2025):
            y = Year(i)
            self.years.append(y)
        my_months = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        for y in range(0, 25):
            for m in range(1, 13):
                tmp_month = Month(my_months[m], m)
                self.years[y].months.append(tmp_month)
                # Creating days and appending them to month
                for d in range(1, tmp_month.number_of_days):
                    tmp_day = Day(d)
                    tmp_month.days.append(tmp_day)

    def addEvent(self, start_hr, start_min, finish_hr, finish_min, description, location, dd, mm, yy):
        referred_year = self.years[yy - 2000]
        referred_month = referred_year.months[mm-1]
        referred_day = referred_month.days[dd-1]
        myEvent = Event(start_hr, start_min, finish_hr, finish_min, description, location)
        referred_day.addEvent(myEvent)
        print("Event added successfully")

    def displayAllEventsInMonth(self, mm, yy):
        referred_year = self.years[yy - 2000]
        referred_month = referred_year.months[mm - 1]
        for i in range(0, referred_month.number_of_days):
            referred_day = referred_month.days[i]
            referred_day.displayAllEvents()

    #def displayOverlappingEvents(self):
        #To be developed

    #def removeEvent(self):
        #To be developed

    #def editEvent(self):
        #To be developed



