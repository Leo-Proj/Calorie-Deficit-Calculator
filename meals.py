cal = 0


class Meals:
    def __init__(self, debug=False):
        self.__debug = debug

    def Breakfast(self, cal):
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")
        return cal

    def Lunch(self, cal):
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")
        return cal

    def Dinner(self, cal):
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")
        return cal

    def Snack(self, cal):
        intake = int(input("Calorie intake? "))
        cal += intake
        print(f"Your total calories is: {cal}")
        return cal
