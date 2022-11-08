"""
Example OOP structure without class definition.
"""


class House:
    ...


def get_house():
    house = House()
    house.location = input("City: ")
    house.price = int(input("Price: "))
    return house


def main():
    house = get_house()
    if house.location == "Amsterdam" and house.price < 500:
        house.price = 1000

    print(f"{house.location} for {house.price}")


if __name__ == "__main__":
    main()
