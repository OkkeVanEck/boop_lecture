# Example classmethod implementation without an init function.


class House:
	valid_cities = ["Amsterdam", "Utrecht", "Maastricht"]
	
	@classmethod
	def is_valid(cls, city):
		if city in valid_cities:
			return True
		else:
			return False


def main():
    city = "Amsterdam"
    city_valid = House.is_valid(city)
    print(city_valid) # Prints "True"
    
    city2 = "Eindhoven"
    city2_valid = House.is_valid(city)
    print(city2_valid) # Prints "False"


if __name__ == "__main__":
    main()

