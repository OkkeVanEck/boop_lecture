"""
Example class instance implementation.
"""


class House:
    def __init__(self, location, price):
        self.location = location
        self.price = price


def get_house():
    location = input("City: ")
    price = input("Price: ")
    return House(location, price)


def main():
    house = get_house()
    print(f"{house.location} for {house.price}")


if __name__ == "__main__":
    main()
