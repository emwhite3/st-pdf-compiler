#student class repredesents the students in the st2 and st2a forms
class Student:
    name = ''
    classification = ''
    college = ''
    address = ''
    phone = ''
    sid = ''
    email = ''
    major = ''
    country = ''
    dateCompleted = ''
    destination = ''
    departureDate = ''
    returnDate = ''
    event = ''

    def __init__(self, event, classification, college, country, dateCompleted, departureDate, destination, email, sid, address, major, name, phone, returnDate):
        self.event = event
        self.classification = classification
        self.college = college
        self.country = country
        self.dateCompleted = dateCompleted
        self.departureDate = departureDate
        self.destination = destination
        self.email = email
        self.sid = sid
        self.address = address
        self.major = major
        self.name = name
        self.phone = phone
        self.returnDate = returnDate
        return

    def setAll(self, lst):

        return

    def setname(self, name):
        self.name = name
    
    def getname(self):
        return self.name

    def setcollege(self, college):
        self.college = college

    def getcollege(self):
        return self.college

#TODO add the rest of the getters and setters