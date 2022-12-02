def parse_input(path: str) -> list:
    with open(path) as f:
        o = [
            [int(i.strip()) for i in group.split("\n")]
            for group in f.read().split("\n\n")
        ]
    return o


def part1(input: list) -> int:
    return max(map(sum, input))


def part2(input: list) -> int:
    cal_list = list(map(sum, input))
    cal_list.sort(reverse=True)
    return sum(cal_list[:3])


# inp = parse_input("input_ex.txt")
inp = parse_input("input.txt")
print(inp)
print(part1(inp))
print(part2(inp))
