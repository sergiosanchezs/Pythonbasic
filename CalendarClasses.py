

class Event:
    def __init__(self, start_hr, start_min, finish_hr, finish_min, description, location):
        self.start_hr = start_hr
        self.start_min = start_min
        self.finish_hr = finish_hr
        self.finish_min = finish_min
        self.description = description
        self.location = location

    def displayEvent(self):
        return ('''
   -->  From {}:{} To {}:{}
        Description: {}
        Location: {}
        -----------------------------------------'''
        .format(self.start_hr, self.start_min, self.finish_hr, self.finish_min, self.description, self.location))
        # result = 'From ' + str(self.start_hr) + ':' + str(self.start_min)
        # result += ' To ' + str(self.start_hr) + ':' + str(self.start_min) + '\n'
        # result += 'Description: ' + self.description + '\n'
        # result += 'Location: ' + self.location + '\n'
        # result += '---------------------------------------------------'
        # return result

class Day:
    def __init__(self, name, day_of_month, month_belong_to):
        self.name = name
        self.day_of_month = day_of_month
        self.month_belong_to = month_belong_to
        self.events = []

    def addEvent(self, event):
        self.events.append(event)

    def displayAllEvents(self):
        print('\nAll events scheduled for: {}, {} {}'.format(self.name, self.day_of_month, self.month_belong_to))
        for i in self.events:
            print(i.displayEvent())

class Month:
    def __init__(self, name, month_of_year):
        self.name = name
        self.month_of_year = month_of_year
        if month_of_year == 2:
            self.number_of_days = 28
        elif month_of_year == 1 or month_of_year == 3 or month_of_year == 5 or month_of_year == 7 or month_of_year == 8 or month_of_year == 10 or month_of_year == 12:
            self.number_of_days = 31
        else:
            self.number_of_days = 30
        self.days =[] * self.number_of_days

    def addDay(self, day):
        self.days.insert(day.day_of_month-1, day)

    def displayEvents(self):
        # print('\nAll events scheduled for the month {}'.format(self.name))
        for i in self.days:
            i.displayAllEvents()

class Year:
    def __init__(self, year_number):
        self.year_number = year_number
        self.months = [] * 12
        
    def addMonth(self, month):
        self.months.insert(month, month.month_of_year - 1)

class Calendar:
    def __init__(self):
        self.years = []
    
    def addYear(self, year):
        self.years.append(year)

    def initializeCalendar(self):
        for i in range(2000, 2025):
            y = Year(i)
            self.years.append(y)
    
    def addEvent(self):
        pass

    def DisplayAllEventsInMonth(self):
        pass

    def displayOverlappingEvents(self):
        pass
    
    def removeEvent(self):
        pass

    def editEvent(self):
        pass
    




    

        


        

        




