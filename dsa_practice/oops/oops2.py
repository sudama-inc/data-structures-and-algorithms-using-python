"""
You can create Attributes outside the class

User defined classes are Mutable.
"""

# ----------------------------------------------------------------

"""
Reference Variables:
Reference Variables holds the objects.
We can create objects without reference variable as well.
An object can can have multiple reference variables.
Assigning a new reference variable to an existing object doesn't create a new object.

Ex: objectname = classname()
objectname is not a actual object, Technically it stores the address of the class.
While calls the classname(), a object (objectname) is created in the memory, but/
/ it stortes the reference of the classname.
objectname is just a variable name or it has a memory (reference) address/
 / of classname, so thatsby its called reference variable.  
"""


class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def greet(self):
        if self.country == 'India':
            return 'Namaste', self.name
        else:
            return 'Hello', self.name


p = Person('Sudama', 'India')
q = p
r = Person('Sharma', 'India')
# print(id(p))
# print(id(q))
# print(id(r))


# ----------------------------------------------------------------


"""
Pass by Reference

"""


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# outside the class
def greet(person):
    return f'Hi my name is {person.name}, and I am a {person.gender}.'


p = Person('Sudama', 'Male')
print(greet(p))