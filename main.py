import convert_functions as cf
import csv 

def main():
    while True:
        inputuser = input("Choice: ").strip().lower()
        match inputuser:
            case "1":
                print("Chosen option 1: Temperature conversion")
                seq1()
            case "2":
                print("Chosen option 2: File I/O")
                seq2()
            case "3":
                print("Chosen option 2_1: File I/O conversion 2")
                seq2_1()
            case "4":
                print("Chosen option 2_1_Excel: File I/O conversion 3")
                seq2_1_Excel()
            case "5":
                print("Chosen option 2_1_Excel_CSV : File I/O conversion 4")
                seq2_1_Excel_CSV()
            case "6":
                print("Chosen option 2_1_Excel_CSV : File I/O conversion 5")
                seq_CSV()
            case _:
                print("\nNo selected, exiting the program. Goodbye!")
                break
            

def seq1():
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


def seq2():
    print("\nFile I/O conversion is not implemented yet.")
    # Create a file and write names to it, then read the file and print greetings
    with open("names.txt", "w") as file:
        for i in range(3):
            name = input(f"Enter le nom numero {i + 1}: ").strip()
            file.write(f"{name}\n")
    with open("names.txt", "r") as file:
        lines = file.readlines()
        for line in sorted(lines):
            print(f"Hello, {line.strip()}!")

def seq2_1():
    print("\nFile I/O conversion 2 is not implemented yet.")
    names = []
    with open("names.txt") as file :
        for line in file :
            names.append(line.strip())
        for name in sorted(names) :
            print(f"Hello, {name}!")
        print(names)
            
def seq2_1_Excel():
    print("\nFile I/O conversion 2 is not implemented yet.")
    students = []
    with open("names.csv") as file :
        for line in file :
            name, city = line.strip().split(",")
            student = {}
            student["name"] = name
            student["city"] = city
            students.append(student)   
        for student in sorted(students, key =get_city_student) :
            print(f"{student['name']} vit à {student['city']}.")

def get_name_student(student):
    return student["Nom"]

def get_city_student(student):
    return student["Ville"]

def seq2_1_Excel_CSV():
    print("CSV mode")
    students = []
    with open("names.csv") as file :
        reader = csv.DictReader(file)
        for row in reader :
            students.append({"Nom": row["name"], "Ville": row["home"],"Loisir" :row["hobby"]})
    for student in sorted(students, key =get_name_student) :
            print(f"{student['Nom']} vit à {student['Ville']} et aiment la {student["Loisir"]}")

def seq_CSV():
    name = input("What's your name ? ")
    home = input("What's your home ? ")
    
    with open("students.csv","a") as file :
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name" : name, "home" : home})    
        
        


if __name__ == "__main__":
    main()
