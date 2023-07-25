"""
Write a program which prompts the user for a Celsius
temperature, convert the temperature to Fahrenheit,
and print out the converted temperature.

"""

celsius = float(input("Enter temperature in degrees Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"The temperature in Fahrenheit is: {fahrenheit}")
