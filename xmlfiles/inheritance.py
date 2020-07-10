from classes import Student


class Std(Student):
    def __init__(self):
        self.maths_grade = 'N/A'
        self.science_grade = "N/A"
        self.english_grade = "N/A"
        self.extra_activities_grade = "N/A"
        super(Std, self).__init__()
        # print('Done')

    def grade(self, maths, science, english, extra_cocuricular_activities_grade):
        self.maths_grade = maths
        self.science_grade = science
        self.english_grade = english
        self.extra_activities_grade = extra_cocuricular_activities_grade
        print('Done')

    def dis_play(self):
        print("*"*25)
        self.display()
        print("*"*25)
        print("Grades Are :")
        print("Maths Grade:", self.maths_grade)
        print("Science Grade: ", self.science_grade)
        print("English grade:", self.english_grade)
        print("Other co-cucuricular activities name:", self.extra_activities_grade)

    def __del__(self):
        print("Account done {}".format(__class__.__name__))


# s = Std()
# name = input('Enter your Name')
# age = int(input("Enter your Age"))
# grade = int(input("Enter your Grade"))
# school = input("Enter you school name")
# city = input("Enter your city name ")
# state = input("Enter your state name ")
# pin_code = int(input("Enter your pin code "))
# s.create_account(name, age, grade, school, city, state, pin_code)
# maths_grade = int(input('Enter your maths grade'))
# science_grade = int(input("Enter your science grade "))
# english_grade = int(input("Enter your english grade"))
# extra_curicular = int(input("Enter your extra co-curicular acrtivities"))
# s.grade(maths_grade, science_grade, english_grade, extra_curicular)
# s.dis_play()
