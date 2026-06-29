# tool: celsius_to_fahrenheit
# description: Converts a temperature from Celsius to Fahrenheit
# author: @bitbox
# example: celsius_to_fahrenheit "100" → "212.0"


def run(*args) -> str:
    celsius = float(args[0])
    fahrenheit = celsius * 9 / 5 + 32
    return str(fahrenheit)
