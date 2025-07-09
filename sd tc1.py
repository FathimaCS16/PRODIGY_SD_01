def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Main program
print("Temperature Converter")
print("Available units: Celsius, Fahrenheit, Kelvin")

temp = float(input("Enter the temperature value: "))
unit = input("Enter the original unit (Celsius/Fahrenheit/Kelvin): ").strip().lower()

if unit == "celsius":
    fahrenheit = celsius_to_fahrenheit(temp)
    kelvin = celsius_to_kelvin(temp)
    print(f"\n{temp}°C is:")
    print(f"{fahrenheit:.2f}°F")
    print(f"{kelvin:.2f}K")

elif unit == "fahrenheit":
    celsius = fahrenheit_to_celsius(temp)
    kelvin = fahrenheit_to_kelvin(temp)
    print(f"\n{temp}°F is:")
    print(f"{celsius:.2f}°C")
    print(f"{kelvin:.2f}K")

elif unit == "kelvin":
    celsius = kelvin_to_celsius(temp)
    fahrenheit = kelvin_to_fahrenheit(temp)
    print(f"\n{temp}K is:")
    print(f"{celsius:.2f}°C")
    print(f"{fahrenheit:.2f}°F")

else:
    print("Invalid unit entered. Please use Celsius, Fahrenheit, or Kelvin.")
