import sys
from random import *
import re

class Hospital:

    '''Hospital Managment Sytem Which Contains Data '''
    HospitalName='''
    ===========================
    Pakistan Group of Hospitals
    ===========================\n'''

    def addData(self):
        self.patient_no = Hospital.psno
        self.patient_name = input("Enter Patient Name:")
        self.patient_phone = input("Enter Patient Phone Number:")
        isPatternMatch = self.patientPhone(self.patient_phone)
        if isPatternMatch:
            self.patient_city = input("Enter Patient City Name:")
            self.patient_disease = input("Enter Patient Disease Name:")
            self.patient_bill = eval(input("Enter Patient Total Bill:"))
        else:
           print("Phone Number is invalid")

        self.mainmenu()

    def display(self):
        print("Patient Registration Number:",self.psno())
        print("Name of Patient:", self.patient_name)
        print("Phone Number of Patient:", self.patient_phone)
        print("City of Patient:", self.patient_city)
        print("Disease of Patient:", self.patient_disease)
        print("Total Bill of Patient:", float(self.patient_bill))
        self.mainmenu()

    def psno(self):
        return randint(10000, 99999)

    def patientPhone(self, number):
        matcher = re.fullmatch("[+][9][2][-]\d{10}", number)
        if matcher != None:
            return True
        else:
            return False

    def mainmenu(self):

        print("1-Add New Record \n2-Search In Record \n3-Exit")

        option=input("Enter Your Choice: ")

        if option.upper()=="1":
            h.addData()
        elif option.upper()=="2":
            h.display()
        elif option.upper()=="3":
            print("Thank you for choosing",Hospital.HospitalName)
            sys.exit()
        else:
            print("\nPlease Enter Valid Input!\n")
            self.mainmenu()

print("\t\t\tWELCOME IN",Hospital.HospitalName)
h=Hospital()
h.mainmenu()
#h.display()



#Modified One
import sys
from random import *
import re
import csv

class Hospital:

    """Hospital Management System Which Contains Data """

    HospitalName = '''
    ===========================
    Pakistan Group of Hospitals
    ===========================\n'''

    def addData(self):
        with open("Hospital Management System.csv", "a", newline="") as f:

            w = csv.writer(f)  # returns csv writer object pointing to f
            w.writerow(["PATIENT_NUMBER", "PATIENT_NAME", "PATIENT_NUMBER", "PATIENT_ADDRESS", "PATIENT_DISEASE",
                        "PATIENT_BILL"])
            self.patient_no = Hospital.patientsno
            self.patient_name = input("Enter Patient Name:")
            self.patient_phone = input("Enter Patient Phone Number:")
            isPatternMatch = self.patientPhone(self.patient_phone)
            if isPatternMatch:
                self.patient_city = input("Enter Patient City Name:")
                self.patient_disease = input("Enter Patient Disease Name:")
                self.patient_bill = eval(input("Enter Patient Total Bill:"))
            else:
               print("Phone Number is invalid")

            w.writerow([self.patientsno(), self.patient_name, self.patient_phone, self.patient_city, self.patient_disease,
                        self.patient_bill])
            print("\nRecord Added Successfully\n")

        self.mainmenu()


    def display(self):
        print("Patient Registration Number:",self.patientsno())
        print("Name of Patient:", self.patient_name)
        print("Phone Number of Patient:", self.patient_phone)
        print("City of Patient:", self.patient_city)
        print("Disease of Patient:", self.patient_disease)
        print("Total Bill of Patient:", float(self.patient_bill))
        self.mainmenu()


    def patientsno(self):
        return randint(10000, 99999)

    def patientPhone(self, number):
        matcher = re.fullmatch("[+]\d{2}[-]\d{3}[-]\d{7}", number)
        if matcher != None:
            return True
        else:
            return False

    def mainmenu(self):

        print("1-Add New Record \n2-Search In Record \n3-Exit")

        option=input("Enter Your Choice: ")

        if option.upper()=="1":
            h.addData()
        elif option.upper()=="2":
            h.display()
        elif option.upper()=="3":
            print("Thank you for choosing",Hospital.HospitalName)
            sys.exit()
        else:
            print("\nPlease Enter Valid Input!\n")
            self.mainmenu()

print("\t\t\tWELCOME IN",Hospital.HospitalName)
h=Hospital()
h.mainmenu()




#Again updated with logging
import sys
from random import *
import re
import csv
import logging

class Hospital:
    """Hospital Management System Which Contains Data """

    HospitalName = '''
    ===========================
    Pakistan Group of Hospitals
    ===========================\n'''

    def addData(self):
        logging.basicConfig(filename="Hospital_Management_System_Log.txt", level=logging.INFO)
        logging.info("A New Request Came")
        with open("Hospital Management System.csv", "a", newline="") as f:

            w = csv.writer(f)  # returns csv writer object pointing to f
            w.writerow(["PATIENT_NUMBER", "PATIENT_NAME", "PATIENT_NUMBER", "PATIENT_ADDRESS", "PATIENT_DISEASE",
                        "PATIENT_BILL"])
            self.patient_no = Hospital.patientsno
            self.patient_name = input("Enter Patient Name:")
            self.patient_phone = input("Enter Patient Phone Number:")
            isPatternMatch = self.patientPhone(self.patient_phone)
            
            if isPatternMatch:
                self.patient_city = input("Enter Patient City Name:")
                self.patient_disease = input("Enter Patient Disease Name:")
                self.patient_bill = eval(input("Enter Patient Total Bill:"))
            else:
                print("Phone Number is invalid")

            w.writerow(
                [self.patientsno(), self.patient_name, self.patient_phone, self.patient_city, self.patient_disease,
                 self.patient_bill])
            print("\nRecord Added Successfully\n")

        logging.info("Request Processing Completed")
        self.mainmenu()


    def display(self):
        print("Patient Registration Number:", self.patientsno())
        print("Name of Patient:", self.patient_name)
        print("Phone Number of Patient:", self.patient_phone)
        print("City of Patient:", self.patient_city)
        print("Disease of Patient:", self.patient_disease)
        print("Total Bill of Patient:", float(self.patient_bill))
        self.mainmenu()

    def patientsno(self):
        return randint(10000, 99999)

    def patientPhone(self, number):
        matcher = re.fullmatch("[+]\d{2}[-]\d{3}[-]\d{7}", number)
        if matcher != None:
            return True
        else:
            return False

    def mainmenu(self):

        print("1-Add New Record \n2-Search In Record \n3-Exit")

        option = input("Enter Your Choice: ")

        if option.upper() == "1":
            h.addData()
        elif option.upper() == "2":
            h.display()
        elif option.upper() == "3":
            print("Thank you for choosing", Hospital.HospitalName)
            sys.exit()
        else:
            print("\nPlease Enter Valid Input!\n")
            self.mainmenu()


print("\t\t\tWELCOME IN", Hospital.HospitalName)
h = Hospital()
h.mainmenu()

