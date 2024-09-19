# single inheritance in object oriented programming language

class sushanth:
    def __init__(self):
        self.data = ['height','weight','color']


class charan(sushanth):
    def data(self):
        return self.data

obj=charan()
print(obj.data)   
print(obj.data) 

    # Output:

    # ['height', 'weight', 'color']

# multiple inheritance

class Ramesh:

    def __init__(self):

        self.data = ['property','Height','Nature','Color']

class jamuna:

    def data(self):

        return self.data

class sushanth(Ramesh, jamuna):
    
    def data(self):
       
        return self.data

obj=sushanth()
print(obj.data)

# Output:

# ['property', 'Height', 'Nature', 'Color']

# Multilevel inheritance

class Ramesh:

    def __init__(self):

        self.data = ['property','Height','Nature','overthinking']

class sumanth(Ramesh):

    def data(self):

        return self.data
    
class sushanth(sumanth):

    def data(self):

        return self.data

obj=sushanth()  

print(obj.data)

# output:

# ['property', 'Height', 'Nature', 'overthinking']


# Hierarchical inheritance

class Mahindra:

    str = "Mahindra Automobile Corporation"  

    print(str)

class XUV700(Mahindra ):

    str = "XUV700"

    print(str)

class XUV500(Mahindra):

    str = "XUV500"

    print(str)

class XUV400(Mahindra):

    str = "XUV400"

    print(str)

obj1= XUV700()
obj1.str
obj1.str1

obj2= XUV500()
obj2.str
obj2.str

obj3= XUV400()
obj3.str
obj3.str

# Output:

# Mahindra Automobile Corporation
# XUV700
# XUV500
# XUV400    
    





           



