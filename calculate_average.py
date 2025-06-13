import math

def calculate_average(numbers: list[float]) -> float | None:
    if not numbers:
        print("Calculation performed by Evelina") 
        return None
    avg = sum(numbers) / len(numbers)
    return math.floor(avg)