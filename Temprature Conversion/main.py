# Temprature Conversion

temprature = float(input("Enter the temprature: "))
unit = input("Is this temprature, Fahrenheit or Celcius? (F or C): ")

if unit == "C":
    temprature = round((9 * temprature) / 5 + 32, 1)
    unit = "F"
    print(f"The temprature in Fahrenheit is {temprature}°F")


elif unit == "F":
    temprature = round((temprature - 32) * 5 / 9, 1)
    unit = "C"
    print(f"The temprature in Celcius is {temprature}°C")


else:
    print(f"{unit} is not valid unit of measurement")


"""
Additionally,
(9 * temprature) / 5 + 32) :- Celcius to Fahranheit formula
(temprature - 32) * 5 / 9) :- Fahrenheit to Celcius formula

Shortcut to ° this sign :- Option + Shift + 8
"""