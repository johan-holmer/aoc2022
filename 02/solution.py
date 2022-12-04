def parse_input(path: str) -> list[str]:
    o = []
    with open(path) as f:
        for line in f:
            o.append("".join([char.strip() for char in line.split(" ")]))
    return o


def part1(input: list[str]) -> int:
    results = {
        "AY": 8,
        "AX": 4,
        "AZ": 3,
        "BY": 5,
        "BX": 1,
        "BZ": 9,
        "CY": 2,
        "CX": 7,
        "CZ": 6,
    }
    return sum([results[round] for round in input])


def part2(input: list[str]) -> int:
    results = {
        "AY": 4,
        "AX": 3,
        "AZ": 8,
        "BY": 5,
        "BX": 1,
        "BZ": 9,
        "CY": 6,
        "CX": 2,
        "CZ": 7,
    }
    return sum([results[round] for round in input])


inp = parse_input("input_ex.txt")
inp = parse_input("input.txt")
print(inp)
print(part1(inp))
print(part2(inp))
