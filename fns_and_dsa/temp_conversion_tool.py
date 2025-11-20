FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temperature = int(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")


def convert_to_celsius(fahrenheit):  
    return f"{temperature}°F is {(temperature -32) * FAHRENHEIT_TO_CELSIUS_FACTOR}°C"

def convert_to_fahrenheit(celsius):
    return f"{temperature}°C is  {temperature  * CELSIUS_TO_FAHRENHEIT_FACTOR + 32}°F"

if temperature_type == "C":
    print(convert_to_fahrenheit(temperature))
elif temperature_type == "F":
    print(convert_to_celsius(temperature))
else:
    print("Invalid temperature. Please enter a numeric value.")