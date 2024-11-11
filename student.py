import logging
import datetime

logging.basicConfig(
    level=logging.DEBUG,
    filename='logger.log',
    filemode='w',
    encoding='utf-8',
    format='We have next log message: %(levelname)s:%(asctime)s - %(message)s'
)

logging.info("Program started")
logging.debug("In progress...")

class Student:
    def __init__(self, name, surname, birthdate, height=160):
        self.name = name
        self.surname = surname
        self.birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
        self.height = height
        logging.info(f"Student object created: {self.name} {self.surname}")

    def printStudent(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Birthdate: {self.birthdate.strftime('%d.%m.%Y')}")
        print(f"Height: {self.height}")

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nBirthdate: {self.birthdate.strftime('%d.%m.%Y')}\nHeight: {self.height}\n"

    def __int__(self):
        age = (datetime.datetime.now() - self.birthdate)
        return int(age.days / 365)

first_student = Student('vlad', 'karlinskij', '25.10.2006', 186)
second_student = Student('oleg', 'palkin', '25.5.2000', 220)

first_student.printStudent()

logging.debug("Program completed.")
logging.info("Program finished successfully.")

print('------------------------------')
print(type(first_student.__str__()))
print(first_student)
print('------------------------------')
print(type(first_student.__int__()))
print(int(first_student))
