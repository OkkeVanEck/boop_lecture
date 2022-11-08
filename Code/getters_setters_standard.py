"""
Example of getting and setting without decorators.
"""


class House:
    def __init__(self, location, price):
        if location not in ["Amsterdam", "Utrecht", "Maastricht"]:
            raise ValueError("Given city is not supported.")

        self.location = location
        self.price = price


def get_house():
    location = input("City: ") # Enter "Amsterdam"
    price = int(input("Price: "))
    return House(location, price)


def main():
    house = get_house()
    print(house.location) # Prints "Amsterdam"
    house.location = "Eindhoven"
    print(house.location) # Prints "Eindhoven"


if __name__ == "__main__":
    main()

