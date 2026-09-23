# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
#
#     def eat(self):
#         print(f"{self.name} is eating food. Yumm!")
#
#
# # Fish INHERITS from Animal
# class Fish(Animal):
#     def __init__(self, name, water_type):
#         # 1. Call the Parent's __init__ using super()
#         super().__init__(name)
#
#         # 2. Add Fish-specific attributes
#         self.water_type = water_type
#
#     def swim(self):
#         print(f"{self.name} is swimming in {self.water_type} water.")
#
# # Create a Fish object
# nemo = Fish(name="Nemo", water_type="saltwater")
#
# # 1. Inherited from Animal parent:
# print(nemo.is_alive)  # Output: True
# nemo.eat()            # Output: Nemo is eating food. Yumm!
#
# # 2. Unique to Fish child:
# nemo.swim()           # Output: Nemo is swimming in saltwater water.

#Parent class
class Animal():
    #this have attributes
    def __init__(self):
        self.num_of_eyes = 2
        self.num_of_nose = 1
        self.num_of_mouth = 1
    #Method breathe
    def breathe(self):
        print("Inhale, Exhale")

#Child class that inherited the Parent class which is Animal
#Basically what parent attribute has and method has can be used by child class basically Inherited
class Fish(Animal):
    def __init__(self):
        #Normalize the super at the top of init, also used only this when you add a new attribute/s
        super().__init__()

    #Method Overriding with Extension, basically inherited the method then add another
    #Two Method Overriding with extension is this and actually replace the breathe method completely
    def breathe(self):
        super().breathe()
        print("Doing it underwater ")

    def swim(self):
        print("Moving in water")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_of_eyes)