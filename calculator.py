def add(numbers: str) -> int:
    if numbers == "":
        return 0
    parts = list(map( int, numbers.split(",")))
    if len(parts) == 1:
        return int(numbers)
    else:
        return sum(parts)
