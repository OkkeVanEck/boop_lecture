"""
Example class init function where errors are raised.
"""


class House:
    def __init__(self, location, price):
        if location not in ["Amsterdam", "Utrecht", "Maastricht"]:
            raise ValueError("Given city is not supported.")

        self.location = location
        self.price = price


def get_house():
    location = input("City: ")
    price = int(input("Price: "))
    return House(location, price)


def main():
    house = get_house()
    print(f"{house.location} for {house.price}")


if __name__ == "__main__":
    main()
