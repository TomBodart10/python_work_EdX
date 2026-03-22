from function1 import converter 

def main():
    temp_celsius = float(input("Enter a temperature in Celsius: "))
    temp_fahrenheit = converter(temp_celsius)
    print(f"{temp_celsius} degrees Celsius is equal to {temp_fahrenheit} degrees Fahrenheit.")

if __name__ == "__main__":
    main()
