# Python Oriented Object

## Data abstraction

- Abstraction: hide low-level (implementation) details
- Abstract data types (ADTs) are data structures that are defined in terms of their operations, rather than their implementation. So a user of ADF will will need (or focus) to know about essentials (i.e., possible operations on that data), but not about details (i.e., how it is  implemented). *"Think of ADT as a black box which hides the inner structure and design of the data type"* (geeksforgeeks)
- In python classes are used to define ADT that encapsulate the data and the operations on that data
  - Example: primitive values like int, float, char data types
    - We know the kind of operations that we can perform on these data type without any idea of how they are implemented

- It encorages
  - *"Program designers to focus on the centrality of data objects rather than functions"*
  - *"To think about programming as a process of combining relatively large chunks"*
  - *"Thinking about a program more as a collecion of types than as a collection of functions"*
- The availablity of reusable abstractions reduce the development time

- Example 1: Using Classes to Keep Track of Students and Faculty
  - goal:
  - python code: `example1.py`
  - solution:
    - create abstraction data type that covers the common attributes of students, professors, and staf: `Person`
      - They are all humans

- Ref
  - [https://www.geeksforgeeks.org/abstract-data-types/](https://www.geeksforgeeks.org/abstract-data-types/)
  - [https://ocw.mit.edu/ans7870/6/6.005/s16/classes/12-abstract-data-types/](https://ocw.mit.edu/ans7870/6/6.005/s16/classes/12-abstract-data-types/)

## Classes

- Class variable: not created for each new class instance. The are associated to a class
- Intance veriables (defined in `__init__()` method) associated to an instence
- Example:

```py
  
  class Person:
    def __init__(name):
        self.name = name

  class MITPerson(Person):
    nextIdNum = 0 # class varibale
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
 ```

- `M = MITPerson("Issa")`
  - M is an `instance` of `MITPerson`
  - `MITPerson`: is a subclass of
`Person`, and inherits the attributes of its superclass (`Person`)

### Hiding information

- This means that they information (e.g., varibales, attributes) can not be accessed directly from outside the class
- When the name of an attribute starts with `__`  but does not end with `__`, that attribute is not visible outside the class
- Equivalent to an attribute is declared  as `private`in Java
