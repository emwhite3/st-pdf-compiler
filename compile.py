from PyPDF2 import PdfFileReader
from cleaner import CleanUtil
import shutil, errno, cgi
import os, glob
from student import Student
from Trips import Trips

"""
This reads the file given which st form to read and the pdf directory
@param int, string
@return 
"""
def read_pdf(filedir, stForms, i):
    form_fields = {}
    clean = CleanUtil()
    try:
        pdf_reader = PdfFileReader(open(filedir, "rb")) #this creates a pdf reader so we can gather information from the pdf form
        fields = pdf_reader.getFields()                 #this is a dictionary with field key values and their associative input data
    except:
        fields = None
    if fields is None:
        fields = {}
    for key in fields:                                  #key is the forms field name i.e 'email' is  the key for 'someone@utep.edu'
        if key != 'sig_univ_employee' and key != 'sig_dept_chair' and key != 'dean_students':
            fl = fields[key]
            form_fields[fl.name] = clean.sanitize(fl.value, fl.fieldType)
    if 'employee_responsible_name' in form_fields:
        stForms['1'] = form_fields
    elif 'colleges-st10' not in form_fields:
        stForms['2' + str(i)] = form_fields
    return


#inbox, report
fileloc = ["/home/emwhite3/Documents/student-affairs/pdfs", "/home/emwhite3/Documents/student-affairs/pdfs/report"]
homedir = os.listdir(fileloc[0])
stForms = {}
trips = []
i = 0
classif = [0, 0]

if homedir:                                                                                             #boolean check for directories in the given path
    for folder in homedir:                                                                              #for every directory within the given path
        for dirpath, dirnames, filenames in os.walk(os.path.join(fileloc[0], folder), topdown=True):    #The os walk returns 3 tuples, the directory path to folder, the directory names, and all file names in the given folder
            for name in filenames:                                                                      #Finally we can now check all files for pdf files
                if name.endswith('.pdf'):                                                               #if this is a pdf we can scrape for data
                    read_pdf(os.path.join(dirpath, name), stForms, i)
                    i += 1
            if stForms and '1' in stForms:
                #print(stForms)
                #print('\n\n\n\n\n\n\n\n')
                students = []
                for key in stForms:
                    if key != '1':
                        students.append(stForms[key])
                trips.append(Trips(stForms['1'], students))
            stForms = {}
print(len(trips))
for trip in trips:
    trip.populateStudent()
    ug, g = trip.classifications()
    classif[0] += ug
    classif[1] += g

print('UnderGraduates: ' + str(classif[0]))
print('Graduates: ' + str(classif[1]))
