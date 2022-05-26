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

elif get_degree == "fahrenheit":
fahrenheit_degree = input("Enter the fahrenheit degree: ")
fahrenheit_to_celsius = (fahrenheit_degree-32)/1.8
print(f"that is {fahrenheit_to_celsius} celsius")
