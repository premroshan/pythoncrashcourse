class Dog:
    """a simple attempt to model a dog"""
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie',6)
your_dog = Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()

print(f"Your dog's name is {your_dog.name}")
print(f"Your dog's is {your_dog.age} years old")

your_dog.sit()
your_dog.roll_over()