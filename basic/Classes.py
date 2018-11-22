class Dog():


    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + "sitting.")


mydog = Dog("uu",6)
mydog.name = "uuuuu"
mydog.sit()

class SmallDog(Dog):
    def __init__(self,name,age):
        super().__init__(name,age)
        self.bar = 10

    def sit(self):
        print("你真帅")

smallDog = SmallDog("wyy",10)
smallDog.sit()