def parse_input(path: str) -> None:
    o = []
    with open(path) as f:
        for line in f:
            r = [[int(x.strip()) for x in y.split("-")] for y in line.split(",")]

            o.append(
                [tuple(range(r[0][0], r[0][1] + 1)), tuple(range(r[1][0], r[1][1] + 1))]
            )
    return o


def part1(input: None) -> int:
    c = 0
    for pair in input:
        if all(el in pair[0] for el in pair[1]) or all(el in pair[1] for el in pair[0]):
            c += 1
    return c


def part2(input: None) -> int:
    c = 0
    for pair in input:
        if any(el in pair[0] for el in pair[1]) or all(el in pair[1] for el in pair[0]):
            c += 1
    return c


inp = parse_input("input_ex.txt")
inp = parse_input("input.txt")
print(inp)
print(part1(inp))
print(part2(inp))
