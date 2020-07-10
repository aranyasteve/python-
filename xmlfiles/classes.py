class Student:

    def __init__(self):
        self.name = "N/A"
        self.Age = "N/A"
        self.Grade = "N/A"
        self.School = "N/A"
        self.city = "N/A"
        self.State = "N/A"
        self.pin_code = "N/A"

    def create_account(self, name, age, grade, school, city, state, pin_code):
        self.name = name
        self.Age = age
        self.Grade = grade
        self.School = school
        self.city = city
        self.State = state
        self.pin_code = pin_code
        # self.display()

    def display(self):
        print("Name is ", self.name)
        print("Age is ", self.Age)
        print("School Grade is ", self.Grade)
        print("School Name is ", self.School)
        print("City Name is ", self.city)
        print("State Name is ", self.State)
        print("Pin Code is ", self.pin_code)

    def __del__(self):
        print("Account done {}".format(__class__.__name__))





