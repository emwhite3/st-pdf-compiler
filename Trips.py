from student import Student

class Trips:
    """Required Fields"""
    employee = {}
    student = []

    """Default Constructor"""
    def __init__(self, employee, student):
        self.employee = employee
        self.student = student

    def classifications(self):
        ug = 0
        g = 0
        print('yee: ' + str(len(self.student)))
        for stud in self.student:
            print(stud.classification)
            if stud.classification != 'Bachelor':
                g += 1
            else:
                ug += 1
            return ug, g

    """Sets the Student Object"""
    def addStudent(self, student):
        self.student.append(student)

    def populateStudent(self):
        studArr = []
        for i in range(len(self.student)):
            if 'name-st1' in self.student[i] and len(self.student[i]['name-st1']) >= 3:
                studArr.append(Student(self.student[i]['Activity-Event'], self.student[i]['classification-st1'],
                                       self.student[i]['colleges-st1'], self.student[i]['country'],
                                       self.student[i]['date_completed'], self.student[i]['departure_date_list'],
                                       self.student[i]['destination_desc'], self.student[i]['email-st1'],
                                       self.student[i]['is-st1'], self.student[i]['local-address-1'],
                                       self.student[i]['major-st1'], self.student[i]['name-st1'],
                                       self.student[i]['phone-st1'], self.student[i]['return_date_list']))
            for j in range(2, 7):
                if ('name-st' + str(j)) in self.student[i] and len(self.student[i]['name-st' + str(j)]) >= 3:
                    studArr.append(Student(self.student[i]['Activity-Event'], self.student[i]['classification-st' + str(j)], self.student[i]['colleges-st' + str(j)], self.student[i]['country'], self.student[i]['date_completed'], self.student[i]['departure_date_list'], self.student[i]['destination_desc'], self.student[i]['email-st' + str(j)], self.student[i]['is-st' + str(j)], self.student[i]['local-address-st' + str(j)], self.student[i]['major-st' + str(j)], self.student[i]['name-st' + str(j)], self.student[i]['phone-st'+str(j)], self.student[i]['return_date_list']))
        self.student = studArr
        return
