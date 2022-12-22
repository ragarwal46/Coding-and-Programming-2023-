import random


class Student:
    import random
    # parti is short for participation
    # This will be used to create computer generated students that judge can only see
    def __init__(self, name, age, gradeLvl, GPA, points, parti):
        self.name = name
        self.age = age
        self.gradeLvl = gradeLvl
        self.GPA = GPA
        self.points = points
        self.parti = parti

    # for name, we have an array and randomly generate a number which will be called from the array. for age,
    # use random number gen to generate an age between 14 and 18 for gradeLvl, use random number generator from 1-12
    # and age to determine gradeLVL. For example, if age is 14 and random gen chooses 5, then person is in 9th but if
    # age is 14 and gen chooses 7 then person is in 10th grade for GPA

    # Allows user to add number of events participated in
    def addParti(self, parti, newParti):
        totalParti = self.parti + newParti
        return totalParti


def createNewStudent():
    studentListOfFirstNames = ["Liam", "Noah", "Oliver", "William", "Elijah", "James", "Benjamin", "Lucas", "Mason", "Logan",
                                "Alexander", "Ethan", "Michael", "Daniel", "Matthew", "Aiden", 
                                "Henry", "Jackson", "Sebastian", "Aiden",
                                "Samuel", "David", "Joseph", "Carter" "Emma", "Olivia", "Ava", "Isabella", 
                                "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",
                                "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila", 
                                "Aria", "Scarlett",  "Victoria", "Madeline", "Naomi", "Lauren", "Gianna"]

    studentListOfLastNames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
                              "Rodriguez", "Martinez", "Wilson", "Anderson", "Thomas", "Taylor", "Jackson", 
                              "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Clark", "Young",
                              "Phillips", "Evans","Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins",
                              "Morgan", "Cooper","Peterson", "Bailey", "Reed", "Kelly", "Bennet", "Hughes", 
                              "Price", "Myers","Foster", "Jimenez"]


    studentFName = random.choice(studentListOfFirstNames)
    studentLName = random.choice(studentListOfLastNames)
    studentAge = random.randint(14, 18)
    if studentAge >= 14 and studentAge < 15: 
        studentGrade = 9
    elif studentAge >= 15 and studentAge < 16:
        studentGrade = 10
    elif studentAge >= 16 and studentAge <= 17:
        studentGrade = 11
    else:
        studentGrade = 12

    studentGPA = round(random.uniform(2.5, 4.0), 2)
    return studentFName, studentLName, studentAge, studentGrade, studentGPA, 0, 0

