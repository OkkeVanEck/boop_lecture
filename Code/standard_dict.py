# Example standard implementation with tuples.
# Gives an error as tuples are immutable.


def get_house():
	location = input("City: ")
	price = input("Price: ")
	return {"location": location, "price": price}


def main():
    house = get_house()
    if house["location"] == "Amsterdam" and house["price"] < 500:
    	house["price"] = 1000
    
    print(f"{house['location']} for {house['price']}")


if __name__ == "__main__":
    main()

