def calculate_average(numbers: list[float]) -> float | None:
    if not numbers:
        print("Calculated by Evelina")  
        return None
    avg = sum(numbers) / len(numbers)
    return int(avg)  