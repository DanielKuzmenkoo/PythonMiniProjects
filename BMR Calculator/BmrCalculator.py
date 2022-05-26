introduction = """Hello, this is a program that calculates your BMR
and also can calculate your BF% to help your weight loss journey.
"""
print(introduction)

get_unit = input("Which unit you would like to work with? (imperial/metric)")
get_unit = get_unit.lower()

if get_unit == "metric":
    user_age = input ("Enter your age here: ")
    user_height = input("Enter your height in inches ")
    user_weight = input ("Enter your weight in pounds ")
    
