def parse_input(path: str) -> list[str]:
    with open(path) as f:
        return [line.strip() for line in f.readlines()]


def part1(input: list[str]) -> int:
    c = 0
    for rucksack in input:
        mid = len(rucksack) // 2
        for char in rucksack[:mid]:
            if char in rucksack[mid:]:
                c += ord(char) - 96 if char.islower() else ord(char) - 38
                break
    return c


# Assuming that input is always multiple of 3
def part2(input: list[str]) -> int:
    c = 0
    for idx in range(0, len(input), 3):
        for char in input[idx]:
            if char in input[idx + 1] and char in input[idx + 2]:
                c += ord(char) - 96 if char.islower() else ord(char) - 38
                break
    return c


# inp = parse_input("input_ex.txt")
inp = parse_input("input.txt")
# print(inp)
print(part1(inp))
print(part2(inp))
