introduction = """Hello, this is a temperature calculator program that
converts Celsius degrees to Fahrenheit and vice versa
"""
print(introduction)

get_degree = input ("What type of degree you want to convert? (Celsius/Fahrenheit) ")
get_degree = get_degree.lower()

if get_degree =="celsius":
    celsius_degree = input("Enter the celsius degree: ")
    celsius_to_fahrenheit = (celsius_degree*1.8) + 32
    print(f"That is {celsius_to_fahrenheit} Fahrenheit")
    
