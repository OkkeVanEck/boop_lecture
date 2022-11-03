# Example class instance implementation.


class House:
	valid_cities = ["Amsterdam", "Utrecht", "Maastrict"]
	
	@classmethod
	def is_valid(cls, city):
		if city in valid_cities:
			return True
		else:
			return False


def main():
    city = "Amsterdam"
    print(is_valid(city)) # Prints "True"
    
    city = "Eindhoven"
    print(is_valid(city)) # Prints "False"


if __name__ == "__main__":
    main()

