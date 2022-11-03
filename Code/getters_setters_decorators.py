# Example of getting and setting without decorators.


class House:
	def __init__(self, location, price):
		if location not in ["Amsterdam", "Utrecht", "Maastrict"]:
			raise ValueError("Given city is not supported.")

		self._location = location
		self.price = price

		@property
		def location(self):
			return self._location
			
		@location.setter
		def location(self, location):
			if location not in ["Amsterdam", "Utrecht", "Maastrict"]:
				raise ValueError("Given city is not supported.")
			return self._location = location


def get_house():
	location = input("City: ") # Enter "Amsterdam"
	price = input("Price: ")
	return House(location, price)


def main():
    house = get_house()  
    print(house.location) # Prints "Amsterdam"
	house.location = "Eindhoven" # Raises ValueError


if __name__ == "__main__":
    main()
