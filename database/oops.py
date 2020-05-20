class Animal:
    #class attributes
    tail = "brown"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def catsound(self):
        print("meowww.........")
    def dogsound(self):
        print("bowwwwwww......")
class Dog(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,name,age)

dog = Dog("puppy",4)

dog.dogsound()
