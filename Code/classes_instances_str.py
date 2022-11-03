# Example class init function where errors are catched and raised.


class House:
	def __init__(self, location, price):
		if location not in ["Amsterdam", "Utrecht", "Maastrict"]:
			raise ValueError("Given city is not supported.")

		self.location = location
		self.price = price
		
	def __str__(self):
		return f"{house.location} for {house.price}"


def get_house():
	location = input("City: ")
	price = input("Price: ")
	return House(location, price)


def main():
    house = get_house()  
    print(house)


if __name__ == "__main__":
    main()

