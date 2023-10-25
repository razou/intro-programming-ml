class Person:
    def __init__(self, name, age, country):
        self.__name = name  # Private member
        self.__age = age  # Private member
        self.__country__ = country # NOT Private: attribute's name ending with "__" (double underscores)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        self.__age = new_age
        
    def get_country(self):
        return self.__country__
    
    def set_country(self, new_country):
        self.__country__ = new_country


class Student(Person):
    def __init__(self, name, age, country, university):
        super().__init__(name, age, country)
        self.university = university
     
    def getName(self):
         return self.__name
        
        
        

def main():
    person = Person("Sidi", 30, "Mauritania")
    
    print("name: ", person.get_name())
    print("age: ", person.get_age())
    print("country (using get country): ", person.get_country())
    print("country (direct access): ", person.__country__)
    # print(person.__name) # raise an error because __name is a private member


if __name__ == "__main__":
    
    print("test attributes' access")
    main()
    
    print('*'*20)
    print('Using sub classes:')
    s = Student("Sidi", 20, "Mauritania", "FST")
    print(s.get_country())
    print(s.get_name())
    print(s.get_age())
    print(s.getName()) # AttributeError: 'Student' object has no attribute '_Student__name'
    