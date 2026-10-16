area = lambda length, width: length * width
print(area(5,4))

def calculate_final_price(price , discount = 0):
    final_price = price - (price * discount)/100
    return final_price
print(calculate_final_price(1000, 10))

def create_profile(name, city, role):
    profile = {
        "name": name,
        "city": city,
        "role": role
    }
    return profile
print(create_profile(role = "Developer", name = "John", city = "Nanded"))

prices = [500, 1200, 2000]

taxed_prices = list(map(lambda price: price + (price * 0.18), prices))
print(taxed_prices)

expensive_prices = list(filter(lambda price: price > 1000, prices))
print(expensive_prices)