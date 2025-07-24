#My name is Jacob Baker and this Chapter 14 Lab 1 done on July 12. I am revising the code on July 24
class Vehicle:

    def __init__(self):
        self.__speed = 0

    def accelerate(self):
        self.__speed += 1

    def decelerate(self):
        self.__speed -= 1

    def display_speed(self):
        print(f"Current speed: {self.__speed}")


