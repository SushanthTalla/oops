# Abstraction is a process of hiding the implementation details 
# ABC is pre defined abstract class 

from abc import ABC , abstractmethod

class Animal(ABC):

    @abstractmethod

    def eat(self):

        pass

class Tiger(Animal):

    def eat(self):

        print("eat Non-veg")

class cow(Animal):

    def eat(self):

        print("eat Veg")

t=Tiger()

t.eat()

c=cow()

c.eat()