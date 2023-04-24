# E22MCAG0026
# Sachin Kumar
from abc import ABC, abstractmethod


class QuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass
