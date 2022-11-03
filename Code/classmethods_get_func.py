# Example of getting and setting without decorators.


class House:
	def __init__(self, location, price):
		if location not in ["Amsterdam", "Utrecht", "Maastrict"]:
			raise ValueError("Given city is not supported.")

		self.location = location
		self.price = price

	@classmethod
	def get(cls):
		location = input("City: ")
		price = input("Price: ")
		return House(location, price)


def main():
    house = House.get() 
    print(f"House is in {house.location}")


if __name__ == "__main__":
    main()

