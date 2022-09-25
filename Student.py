class Student:
    #parti is short for participation
    def __init__(self, name, age, gradeLvl, GPA, points, parti):
        self.name = name
        self.age = age
        self.gradeLvl = gradeLvl
        self.GPA = GPA
        self.points = points
        self.parti = parti

      # for name, we have an array and randomly generate a number which will be called from the array.  
    # for age, use random number gen to generate an age between 14 to 18 
    # for gradeLvl, use random number generator from 1-12 and age to determine gradeLVL. For example, if age is 14 and random gen chooses 5, then person is in 9th 
        # but if age is 14 and gen chooses 7 then person is in 10th grade
    # for GPA, 
    points = 0 
    parti = 0
    
    def getName(self):
        return self.name
    
    def getAge(self):
        #will state student's age
        return self.age
    
    def getGPA(self):
        #will state student's grade 
        return self.GPA

    def getGradeLvl(self):
        #will state student's grade Level 
        return self.gradeLvl

    def getPoints(self):
        #will state how many points student has accumulated
        return self.points
    
    def getparti(self):
        #will state how many times student has participated
        return self.parti
    
    def addParti(self, parti):
        parti += 1
        return print(parti)


