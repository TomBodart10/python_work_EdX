import convert_functions as cf

def main():
    print("\n===== Welcome to the Temperature Converter! =====\n")
    print("Convertion de Celsius à Fahrenheit\n")
    temp_celsius = float(input("Enter a temperature in Celsius: "))
    temp_fahrenheit = cf.convert_c_to_f(temp_celsius)
    print(f"{temp_celsius:.2f} degrees Celsius is equal to {temp_fahrenheit:.2f} degrees Fahrenheit.")

    print("\nConversion de Fahrenheit à Celsius\n")
    temp_fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    temp_celsius = cf.convert_f_to_c(temp_fahrenheit)
    print(f"{temp_fahrenheit:.2f} degrees Fahrenheit is equal to {temp_celsius:.2f} degrees Celsius.")

    print("\nConversion de Celsius à Kelvin\n")
    temp_kelvin = cf.convert_c_to_k(temp_celsius)
    print(f"{temp_celsius:.2f} degrees Celsius is equal to {temp_kelvin:.2f} Kelvin.")

    print("\nConversion de Kelvin à Celsius\n")
    temp_kelvin = float(input("Enter a temperature in Kelvin: "))
    temp_celsius = cf.convert_k_to_c(temp_kelvin)
    print(f"{temp_kelvin:.2f} Kelvin is equal to {temp_celsius:.2f} degrees Celsius.")

if __name__ == "__main__":
    main()
