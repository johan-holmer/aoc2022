def parse_input(path: str) -> str:
    with open(path) as f:
        return f.readline().strip("\n")


def part1(input: str) -> int:
    for idx, _ in enumerate(input):
        if idx > 3:
            test_marker = input[idx - 4 : idx]
            if len(set([char for char in test_marker])) == len(test_marker):
                return idx


def part2(input: str) -> int:
    for idx, _ in enumerate(input):
        if idx > 13:
            test_marker = input[idx - 14 : idx]
            if len(set([char for char in test_marker])) == len(test_marker):
                return idx


inp = parse_input("input_ex.txt")
inp = parse_input("input.txt")
print(inp)
print(part1(inp))
print(part2(inp))
