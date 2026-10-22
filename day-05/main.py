import time
from functools import wraps
import asyncio
import inspect

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")

        return result

    return wrapper

@timer
def calculate_sum(n: int) -> int:
    return sum(range(1, n + 1))


result = calculate_sum(1_000_000)
print("Result:", result)

def async_timer(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = await func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.4f} seconds")

        return result

    return wrapper

@async_timer
async def fetch_data(name: str, delay: float) -> str:
    print(f"Starting {name}")

    await asyncio.sleep(delay)

    print(f"Finished {name}")
    return f"{name} data"

async def main():
    results = await asyncio.gather(
        fetch_data("Users", 2),
        fetch_data("Products", 3),
        fetch_data("Orders", 1),
    )

    print("Results:", results)


asyncio.run(main())