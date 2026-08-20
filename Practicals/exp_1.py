#Write a Python program that takes a list of temperatures in Celsius as input and converts each to Fahrenheit and Kelvin, using appropriate variables, data types and formatted output.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Celsius =", celsius)
print("Fahrenheit =", fahrenheit)
print("Kelvin =", kelvin)