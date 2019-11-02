'''
years = [0, 1, 2, 3, ..., 24]
years[0] = Year(2000)
years[1] = Year(2000)
...
years[24] = Year(2000)

months = [0, 1, 2, ..., 11]
month[1] = Month('January', 1)
month[2] = Month('February', 2)
...
month[11] = Month('December', 12)

'''


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

    #def __init__(self, name, day_of_month, month_belong_to):
    def __init__(self, day_of_month):
        #self.name = name
        self.day_of_month = day_of_month
       # self.month_belong_to = month_belong_to
        self.events = []

    def addEvent(self, event):
        self.events.append(event)

    def displayAllEvents(self):
        print("All events scheduled for " + self.name + ", " + str(self.day_of_month) + " " + self.month_belong_to)
        for i in self.events:
            print(i.displayEvent())


class Month:

    def __init__(self, name, month_of_year):
        self.name = name
        self.month_of_year = month_of_year

        if month_of_year == 2:
            self.number_of_days = 28    # for 28 days
        elif month_of_year == 1 or month_of_year == 3 or month_of_year == 5 or month_of_year == 7 or month_of_year == 8 or month_of_year == 10 or month_of_year == 12:
            self.number_of_days = 31    # for 31 days
        else:
            self.number_of_days = 30    # for 30 days 

        # lengh_days_array = self.number_of_days + 1
        self.days = [] * self.number_of_days

    def addDay(self, day):
        self.days.insert(day.day_of_month-1, day)

    def displayEvents(self):
        for i in self.days:
            i.displayAllEvents()

class Year:

    def __init__(self, year_number):
        self.year_number = year_number
        self.months = []

class Calendar:

    def __init__(self):
        self.years = []

    def addYear(self, year):
        self.years.append(year)

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
                for d in range(1, tmp_month.number_of_days + 1):
                    tmp_day = Day(d)
                    tmp_month.days.append(tmp_day)
               

    # Example (12, 10, 14, 20, 'Grad', 'Graduate', 15, 12, 2019)
    def addEvent(self,  start_hr, start_min, finish_hr, finish_min, description, location, dd, mm, yy):
        referred_year = self.years[yy - 2000]
        referred_month = referred_year.months[mm - 1]
        referred_day = referred_month.days[dd - 1]
        
        myEvent = Event(start_hr, start_min, finish_hr, finish_min, description, location)

        referred_day.addEvent(myEvent)

    #def displayAllEventsInMonth(self):
        #To be developed

   #def displayOverlappingEvents(self):
        #To be developed

    #def removeEvent(self):
        #To be developed

    #def editEvent(self):
        #To be developed



