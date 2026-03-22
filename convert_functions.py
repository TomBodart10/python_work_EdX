def convert_c_to_k(temp_celsius):
    temp_kelvin = temp_celsius + 273.15
    return temp_kelvin

def convert_k_to_c(temp_kelvin):
    temp_celsius = temp_kelvin - 273.15
    return temp_celsius

def convert_c_to_f(temp_celsius):
    temp_fahrenheit = (temp_celsius * 9/5) + 32
    return temp_fahrenheit 

def convert_f_to_c(temp_fahrenheit):
    temp_celsius = (temp_fahrenheit - 32) * 5/9
    return temp_celsius
