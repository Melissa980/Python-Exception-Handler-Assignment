# Question 2 Task 1 

def get_servings():
    while True:
        try:
            original_servings = int(input("Enter the number of servings the recipe is originally for: "))
            desired_servings = int(input("Enter the number of servings you wish to make: "))
            return original_servings, desired_servings
        except ValueError:
            print("Please enter a valid number for servings.")


# Question 2 Task 2

def calculate_adjustment(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        return adjustment_factor
    except ZeroDivisionError:
        print("Error: Original servings cannot be zero.")


# Question 2 Task 3
def display_adjusted_quantities(original_servings, desired_servings):
    try:
        adjustment_factor = desired_servings / original_servings
        print(f"Adjustment Factor: {adjustment_factor:.2f}")
    except ZeroDivisionError:
        print("Error: Original servings cannot be zero.")
    finally:
        print("\nEnjoy your cooking!")


def main():
    print("Welcome to the Recipe Ratio Adjuster!")
    original_servings, desired_servings = get_servings()
    adjustment_factor = calculate_adjustment(original_servings, desired_servings)
    display_adjusted_quantities(original_servings, desired_servings)
if __name__ == "__main__":
    main()