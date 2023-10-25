
from abstract_data_type import Person

class MITPerson(Person):
    
    """MITPerson is a subclass of Person, and therefore inherits the attributes of its superclass.
     In addition to what it inherits, the subclass can:
     - Add new attributes. For example, the subclass MITPerson has added the 
     class variable nextIdNum, the instance variable idNum, and the method getIdNum.
     - Override, i.e., replace, attributes of the superclass
    """
 
    # class variable (different from instance variable, i.e defined in __init__ method) 
    # that belongs to the class MITPerson, rather than to instances of the class.
    # When an instance of MITPerson is created, a new instance of nextIdNum is not created. 
    # This allows __init__ to ensure that each instance of MITPerson has a unique idNum.
    nextIdNum = 0 
 
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def isStudent(self):
        return isinstance(self, Student)
    
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum


class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
 
class Grad(Student):
    pass


class TransferStudent(Student):
    def __init__(self, name, fromSchool):
        MITPerson.__init__(self, name)
        self.fromSchool = fromSchool    
    def getOldSchool(self):
        return self.fromSchool




class Grades(object):
    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True
        
    def addStudent(self, student):
        """Assumes: student is of type Student
        Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        """Assumes: grade is a float
        Add grade to the list of grades for student"""
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError('Student not in mapping')
        
    def getGrades(self, student):
        """Return a list of grades for student"""
        try: 
            return self.grades[student.getIdNum()][:] #return copy of list of student's grades
        except:
            raise ValueError('Student not in mapping')
        
    def getStudents(self):
        """Return a sorted list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] #return copy of list of students (to avoid unexpected mofifications)

    def getStudentsGenerator(self):
        """Return the students in the grade book one at a time in alphabetical order.
        
        The number of students can be hugh (~2M or more) and creating a new list of that size 
        when the list already exists is a significant inefficiency and expensive (memory usage)
        
        We need to define new getStudents method using generators.
        """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s




def gradeReport(course: "Grades"):
    """Assumes course is of type Grades"""
    report = ''
    for s in course.getStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report = report + '\n' + str(s) + '\'s mean grade is ' + str(average)
        except ZeroDivisionError:
            report = report + '\n' + str(s) + ' has no grades'
    return report

if __name__ == "__main__":
    p0 = MITPerson('Barbara Beaver')
    print(str(p0) + '\'s id number is ' + str(p0.getIdNum()))
    
    p1 = MITPerson('Mark Guttag')
    p2 = MITPerson('Billy Bob Beaver')
    p3 = MITPerson('Billy Bob Beaver')
    p4 = Person('Billy Bob Beaver')
    
    print(f"'{str(p1)} < {str(p2)} ='", p1 < p2)
    print(f"'{str(p3)} < {str(p2)} ='", p3 < p2)
    ## p1 is an instance of MITPerson and p4 is an instance of Person
    # p4 < p1 is equivalent to p4.__lt__(p1). 
    # Therefore, the interpreter uses the __lt__ method associated with the type of p4,
    # Person, and the “people” will be ordered by name
    print(f"'{str(p4)} < {str(p1)} ='", p4 < p1)
    
    ## p1 < p4 => AttributeError: 'Person' object has no attribute 'idNum'
    # p1 < p4 equivalent to p1.__lt__(p4)

    # print(f"'{str(p1)} < {str(p4)} ='", p1 < p4)
    
    
    print('*' * 20)
    ug1 = UG('Jane Doe', 2014)
    ug2 = UG('John Doe', 2015)
    ug3 = UG('David Henry', 2003)
    g1 = Grad('Billy Buckner')
    g2 = Grad('Bucky F. Dent')
    
    sixHundred = Grades()
    sixHundred.addStudent(ug1)
    sixHundred.addStudent(ug2)
    sixHundred.addStudent(g1)
    sixHundred.addStudent(g2)
    
    for s in sixHundred.getStudents():
        sixHundred.addGrade(s, 75)
        
    sixHundred.addGrade(g1, 25)
    sixHundred.addGrade(g2, 100)
    sixHundred.addStudent(ug3)
    
    print(gradeReport(sixHundred))
    
    
    print("Test get student using generators")
    book = Grades()
    book.addStudent(Grad('Julie'))
    book.addStudent(Grad('Charlie'))
    for s in book.getStudentsGenerator():
        print(s)


    