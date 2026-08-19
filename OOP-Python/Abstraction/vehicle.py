from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car Started")


class Bike(Vehicle):

    def start(self):
        print("Bike Started")


car = Car()
bike = Bike()

car.start()
bike.start()
