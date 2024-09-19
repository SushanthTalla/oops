# Process of wrapping 'Data' and 'Methods' together into a single unit or class

class Car:
    def __init__(self, make, model):

        self.make = make
        self.model = model
        

    def display_info(self):

        print(f"{self.make} {self.model}")


my_car = Car ("BMW" , "XM series") 

my_car.display_info()

# Output: BMW XM series




     