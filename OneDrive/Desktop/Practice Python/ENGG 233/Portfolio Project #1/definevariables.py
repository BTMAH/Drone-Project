def main():
    cars = {
        1: {"type_of_car": "Buggati", "top_speed": 431, 
        "fuel_capacity": 100, "fuel_efficiency": 3.1},
        2: {"type_of_car": "Martin", "top_speed": 402,
        "fuel_capacity": 90, "fuel_efficiency": 6.8},
        3: {"type_of_car": "Ferrari", "top_speed": 350,
        "fuel_capacity": 85, "fuel_efficiency": 6.4}
    }
drivers = {
    1: {"recklessness": 1.1},
    2: {"recklessness": 1.2},
    3: {"recklessness": 1.3},
}


print("1 = Bugatti Veyron")
print("2 = Aston Martin")
print("3 = Ferrari")

# get the car selection
car_number = int(input("Choose a car (1, 2, or 3): "))
    if car_number not in cars:
        print("Invalid input. Please select either (1, 2, or 3)")
    return
# get the driver selection
# get the race distance
# get the road condition
#