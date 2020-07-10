from inheritance import Std


class Emergency(Std):
    def __init__(self):
        self.emergency_contact_number = "N/A"
        super(Emergency, self).__init__()

    def number(self, number):
        self.emergency_contact_number = number
    def disp_lay(self):
        self.dis_play()
        print("Emergency Contact Number: ",self.emergency_contact_number)
        print("*" * 25)
    def __del__(self):
        print("Account Completed", __class__.__name__)


s=Emergency()
name = input('Enter your Name')
age = int(input("Enter your Age"))
grade = int(input("Enter your Grade"))
school = input("Enter you school name")
city = input("Enter your city name ")
state = input("Enter your state name ")
pin_code = int(input("Enter your pin code "))
s.create_account(name, age, grade, school, city, state, pin_code)
maths_grade = int(input('Enter your maths grade'))
science_grade = int(input("Enter your science grade "))
english_grade = int(input("Enter your english grade"))
extra_curicular = int(input("Enter your extra co-curicular acrtivities"))
s.grade(maths_grade, science_grade, english_grade, extra_curicular)
number = int(input("Enter your Emergency Number "))
s.number(number)
s.disp_lay()
