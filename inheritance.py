class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)

# here (Parent) means that the class Child will now inherit or reuse everything
# that is publically available in the class Parent.
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)
        #here str(object) refers to string function whcih converts the object to string
        print("Number of Toys - "+str(self.number_of_toys))
        

# Always try to define the class and it's instances in two different files.
# This is just for practice.
billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)
billy_cyrus.show_info()

miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)
