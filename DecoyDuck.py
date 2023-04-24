# E22MCAG0026
# Sachin Kumar
from Duck import Duck
from fly_no_way import FlyNoWay
from Quack import Quack

class DecoyDuck(Duck):
    def __init__(self):
        super().__init__(FlyNoWay(), Quack())

    def display(self):
        print("I'm decoy duck")
