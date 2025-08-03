import re


def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [","]
    if numbers.startswith("//"):
        delimiter_section, numbers = numbers.split("\n", 1)
        custom = delimiter_section[2:]

        if custom.startswith("["):
            delimiters = re.findall(r"\[(.*?)\]", custom)
        else:
            delimiters = [custom]

    for delimiter in delimiters:
        numbers = numbers.replace(delimiter, ",")

    numbers = numbers.replace("\n",",")
    parts = numbers.split(",")
    ints = []

    for part in parts:
        part = part.strip()
        if not part:
            continue
        try:
            num = int(part)
            ints.append(num)
        except ValueError:
            raise ValueError(f"invalid number found: {part}")

    negatives = [n for n in ints if n < 0]
    if negatives:
        raise ValueError(f"negative numbers not allowed {', '.join(map(str, negatives))}")

    return sum(n for n in ints if n <= 1000)
