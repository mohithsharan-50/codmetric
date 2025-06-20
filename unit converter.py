def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
def km_to_miles(km):
    return km * 0.621371
def miles_to_km(miles):
    return miles / 0.621371
def kg_to_pounds(kg):
    return kg * 2.20462
def pounds_to_kg(pounds):
    return pounds / 2.20462

conversions = {
    '1': ('Celsius to Fahrenheit', celsius_to_fahrenheit, '°C', '°F'),
    '2': ('Fahrenheit to Celsius', fahrenheit_to_celsius, '°F', '°C'),
    '3': ('Kilometers to Miles', km_to_miles, 'km', 'miles'),
    '4': ('Miles to Kilometers', miles_to_km, 'miles', 'km'),
    '5': ('Kilograms to Pounds', kg_to_pounds, 'kg', 'lbs'),
    '6': ('Pounds to Kilograms', pounds_to_kg, 'lbs', 'kg')
}

def main():
    while True:
        print("\n--- Unit Converter ---")
        for key in sorted(conversions.keys()):
            print(f"{key}. {conversions[key][0]}")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Goodbye!")
            break
        elif choice in conversions:
            try:
                value = float(input(f"Enter value in {conversions[choice][2]}: "))
                result = conversions[choice][1](value)
                print(f"{value:.2f} {conversions[choice][2]} = {result:.2f} {conversions[choice][3]}")
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid choice. Please try again.")

main()
