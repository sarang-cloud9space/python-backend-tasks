def multiply(a, b=1):
    return a*b
print(multiply(5))
print(multiply(5, 2))

def average(*numbers):
    return sum(numbers) / len(numbers) if numbers else 0
print(average(1, 2, 3, 4, 5))
# print(average('a', 'b', 'c'))  # This will raise an error since you can't sum strings

def build_user(name, **details):
    user = {'name': name}
    user.update(details)
    return user
print(build_user("Alice", age=30, city="New York"))

def create_product(name, price, *tags, discount=0, **metadata):
    product = {
        'name': name,
        'price': price - discount,
        'tags': tags,
        'discount': discount,
        'metadata': metadata
    }
    return product
print(create_product(
    "Keyboard",
    2000,
    "wireless",
    "mechanical",
    discount=200,
    category="electronics",
))
print(create_product("Mouse", 500))
print(create_product("Monitor", 5000, "4K", "IPS", warranty=2)) 

prices = [100, 200, 300]


def add_tax(price):
    return price * 1.18


taxed_prices = map(add_tax, prices)

print(list(taxed_prices))

prices = [100, 200, 300]

taxed_prices = list(map(lambda price: price * 1.18, prices))

print(taxed_prices)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(
    filter(lambda number: number % 2 == 0, numbers)
)

print(even_numbers)

numbers = [40, 10, 30, 20]

result = sorted(numbers)

print(result)
print(numbers)

employees = [
    {"name": "Amit", "salary": 50000},
    {"name": "Priya", "salary": 70000},
    {"name": "Rahul", "salary": 40000}
]

result = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

for employee in result:
    print(employee["name"], employee["salary"])