class Workouts:
    def __init__(self, debug=False):
        self.__debug = debug

    def running(self, cal):
        print("Running selected.")
        kmsRan = int(input("How many kilometers did you run? "))
        calBurned = kmsRan * 60
        cal -= calBurned
        print(f"You burned {calBurned} calories!")
        print(f"Your current calories sits at: {cal}")
        return cal
