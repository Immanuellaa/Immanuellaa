class Person:
    def __init__(self, name):
        self.name = name

    def myfunc(self):  # Ensure this method exists
        print("Hello, my name is", self.name)

p1 = Person("John")
p1.myfunc()

class female(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def myfunc(self):
        Person.myfunc(self)
        print('salary: "{:d}"'.format(self.salary))

class Male(Person):
    def __init__(self, name, height):
        Person.__init__(self, name)
        self.height = height
        
    def myfunc(self):
        Person.myfunc(self)
        print('height: "{:d}"'.format(self.height))   

f = female('ana', 500)
m = Male('ben', 198)

# prints a blank line
print()

members = [f, m]
for member in members:
    # Works for both  females and males
    member.myfunc()
    