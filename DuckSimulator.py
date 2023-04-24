# E22MCAG0026
# Sachin Kumar
from RubberDuck import RubberDuck
from MallardDuck import MallardDuck
from RedHeadDuck import RedHeadDuck
from DecoyDuck import DecoyDuck



class DuckSimulator:
    @staticmethod
    def main():
        print("Welcome to the Duck Simulator!")
        duck_options = ["Rubber Duck", "Mallard Duck", "Red Head Duck", "Decoy Duck"]
        duck_choice = int(input("Please select a duck (enter 1-4):\n1. Rubber Duck\n2. Mallard Duck\n3. Red Head Duck\n4. Decoy Duck\n"))

        if duck_choice == 1:
            duck = RubberDuck()
        elif duck_choice == 2:
            duck = MallardDuck()
        elif duck_choice == 3:
            duck = RedHeadDuck()
        elif duck_choice == 4:
            duck = DecoyDuck()
        else:
            print("Invalid input!")
            return
        duck.display()
        duck.perform_fly_behavior()
        duck.perform_quack_behavior()
        print("Thank you for trying the Duck Simulator!")
# Test the Simulator
DuckSimulator.main()
