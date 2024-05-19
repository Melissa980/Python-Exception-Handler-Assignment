# Question 1 Task 1

while True:
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        break  
    except ValueError:
        print("Error: Please enter a numerical value for the temperature.")

# Question 1 Task 2

def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ZeroDivisionError:
        print("Error: Division by zero occurred during conversion.")
        return None
    except OverflowError:
        print("Error: Overflow occurred during conversion.")
        return None

celsius_temp = fahrenheit_to_celsius(fahrenheit)

# Question 1 Task 3

try:
    if celsius_temp is not None:
        print(f"The temperature in Celsius is {celsius_temp:.2f}°C.")
    else:
        print("Temperature conversion failed.")
except Exception as e:
    print("An error occurred during temperature conversion:", e)
finally:
    print("Thank you for using the weather forecast application!")
