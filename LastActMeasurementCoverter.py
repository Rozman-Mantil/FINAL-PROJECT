#1
def mm_to_cm(mm):
    return mm / 10

def ft_to_m(ft):
    return ft * 0.3048

def inches_to_meters(inches):
    return inches * 0.0254

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def pounds_to_kg(pounds):
    return pounds * 0.453592



#2
def display_menu():
    print("Measurement Converter Menu:")
    print("1. Millimeters to Centimeters")
    print("2. Feet to Meters")
    print("3. Kilometers to Miles")
    print("4. Celsius to Fahrenheit")
    print("5. Pounds to Kilograms")
    print("6. Inches to Meters")
    print("7. Exit")

#3
def measurement_converter():
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            mm = float(input("Enter length in millimeters: "))
            cm = mm_to_cm(mm)
            print(f"{mm} mm is equal to {cm} cm.")
        elif choice == '2':
            ft = float(input("Enter length in feet: "))
            m = ft_to_m(ft)
            print(f"{ft} ft is equal to {m} m.")
        elif choice == '3':
            km = float(input("Enter distance in kilometers: "))
            miles = km_to_miles(km)
            print(f"{km} km is equal to {miles} miles.")
        elif choice == '4':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F.")
        elif choice == '5':
            pounds = float(input("Enter weight in pounds: "))
            kg = pounds_to_kg(pounds)
            print(f"{pounds} lbs is equal to {kg} kg.")
        elif choice == '6':
            inches = float(input("Enter length in inches: "))
            meters = inches_to_meters(inches)
            print(f"{inches} inches is equal to {meters} meters.")
        elif choice == '7':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

# Run the measurement converter program
measurement_converter()


