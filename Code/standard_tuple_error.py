"""
Example standard implementation with a tuple.
Gives an error as tuples are immutable.
"""


def get_house():
    location = input("City: ")
    price = int(input("Price: "))
    return (location, price)


def main():
    house = get_house()
    if house[0] == "Amsterdam" and house[1] < 500:
        house[1] = 1000

    print(f"{house[0]} for {house[1]}")


if __name__ == "__main__":
    main()
