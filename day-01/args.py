def add(*harsh):
    print(harsh)
add(1, 2, 3, 4, 5)

def calculate_sum(*args):
    total = 0

    for number in args:
        total += number

    return total


print(calculate_sum(10, 20, 30))
print(calculate_sum(5, 10, 15, 20))