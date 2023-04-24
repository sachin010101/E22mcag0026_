# E22MCAG0026
# Sachin Kumar
from abc import ABC, abstractmethod
from fly_behavior import FlyBehavior
from QuackBehavior import QuackBehavior

class Duck(ABC):
    def __init__(self, fly_behavior, quack_behavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    @abstractmethod
    def display(self):
        pass

    def perform_fly_behavior(self):
        self.fly_behavior.fly()

    def perform_quack_behavior(self):
        self.quack_behavior.quack()
