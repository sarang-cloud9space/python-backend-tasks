def calculate():
    price = 100
    print(price)


calculate()
print(price)

tax_rate = 18


def calculate_tax(price):
    return price * tax_rate / 100


print(calculate_tax(1000))

count = 10


def update_count():
    count = 20
    print(count)


update_count()
print(count)

count = 10


def update_count():
    global count
    count = 20


update_count()
print(count)

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count

    print(inner())
    print(inner())


outer()

def make_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))