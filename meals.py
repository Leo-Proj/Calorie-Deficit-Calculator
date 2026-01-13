cal = 0


class Meals:
    def __init__(self, debug=False):
        self.__debug = debug

    def Breakfast(self):
        global cal
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")

    def Lunch(self):
        global cal
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")

    def Dinner(self):
        global cal
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")

    def Snack(self):
        global cal
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")
