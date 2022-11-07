"""
Example class init function with __str__ overloaded.
"""


class House:
    def __init__(self, location, price):
        if location not in ["Amsterdam", "Utrecht", "Maastricht"]:
            raise ValueError("Given city is not supported.")

        self.location = location
        self.price = price

    def __str__(self):
        return f"{self.location} for {self.price}"


def get_house():
    location = input("City: ")
    price = input("Price: ")
    return House(location, price)


def main():
    house = get_house()
    print(house)


if __name__ == "__main__":
    main()
