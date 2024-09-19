# Polymorphism means the ability to take multiple forms , polymorphism can be achieved through
# 1) Method Overriding 
# 2) Method Overloading

print(5 + 5)
print("5" + "5")

# Method Overriding

class Bottle :

    def setcap(self):

        print("Hello")

class sodabottle(Bottle):
    
    def setcap(self):

        print("world")


obj = Bottle()
obj.setcap()

obj = sodabottle()    
obj.setcap()

# method overriding using more than two classes 

class Animal:
    
    def sound(self):

        return "some type of animal sound"
    
class Dog(Animal):

    def sound(self):

        return "Bark"

class Cat(Animal):

    def sound(self):

        return "Meow"

class Cow(Animal):

    def sound(self):

        return "Moo"

def animal_sound(animal):
    
    print(animal.sound())

dog = Dog()

cat = Cat()

cow = Cow()

animal_sound(dog)

animal_sound(cat)

animal_sound(cow)










        
    

    





