"""
Example inheritance.
"""


class House:
    def __init__(self, location, price):
        if location not in ["Amsterdam", "Utrecht", "Maastricht"]:
            raise ValueError("Given city is not supported.")

        self.location = location
        self.price = price


class Apartment(House):
    def __init__(self, location, price, kind):
        super().__init__(location, price)

        if kind not in ["studio", "loft", "duplex"]:
            raise ValueError("Apartment type is invalid.")

        self.kind = kind


def main():
    house = House("Amsterdam", 750)  # Creates House
    apartment1 = Apartment("Amsterdam", 750, "studio")  # Creates Apartment
    apartment2 = Apartment("Amsterdam", 750, "micro")  # ValueError Apartment
    apartment3 = Apartment("Eindhoven", 350, "studio")  # ValueError House


if __name__ == "__main__":
    main()
