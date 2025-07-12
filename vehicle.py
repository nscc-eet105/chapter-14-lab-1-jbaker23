#My name is Jacob Baker and this Chapter 14 Lab 1 done on July 12
class Vehicle:

    def __init__(self, speed):
        self.speed = 0

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

    def display_speed(self):
        print(f"Current speed: {self.speed}")


