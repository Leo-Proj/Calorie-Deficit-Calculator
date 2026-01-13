from meals import Meals


def start_menu():
    cal = 0
    meals = Meals()
    print(f"Welcome! Your total calorie intake for the day is {cal}.")
    print("What would you like to input?")
    print("1. Breakfast\n2. Lunch \n3. Dinner\n4. Snack\n5. Exit")
    selection = input("Please select the corresponding number: ")
    if selection == "1":
        print("Breakfast selected.")
        meals.Breakfast()
    elif selection == "2":
        print("Lunch selected.")
    elif selection == "3":
        print("Dinner selected.")
    elif selection == "4":
        print("Snack selected.")
    elif selection == "5":
        print("Exiting...")
        exit()
    else:
        print("Not a valid input.")


start_menu()
