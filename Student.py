class Student:
    #parti is short for participation
    def __init__(self, name, age, gradeLvl, GPA, points, parti):
        self.name = str(name)
        self.age = int(age)
        self.gradeLvl = int(gradeLvl)
        self.GPA = float(GPA)
        self.points = float(points)
        self.parti = int(parti)
        
    
        

    # for name, we have an array and randomly generate a number which will be called from the array.  
    # for age, use random number gen to generate an age between 14 to 18 
    # for gradeLvl, use random number generator from 1-12 and age to determine gradeLVL. For example, if age is 14 and random gen chooses 5, then person is in 9th 
        # but if age is 14 and gen chooses 7 then person is in 10th grade
    # for GPA, 

