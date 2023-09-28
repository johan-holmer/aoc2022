from copy import deepcopy


def parse_input_stacks(path: str) -> list[list]:
    with open(path) as f:
        r = [[i for i in group.split("\n")] for group in f.read().split("\n\n")][0]

        nbr_stacks = int(r[-1][-2])
        length_string = len(r[0])
        stacks = [[] for _ in range(nbr_stacks)]

        for idx in range(len(r) - 2, -1, -1):
            for pos in range(1, length_string, 4):
                char = r[idx][pos]
                if char != " ":
                    stacks[(pos - 1) // 4].append(char)

    return stacks


def parse_input_instructions(path: str) -> list[list]:
    with open(path) as f:
        r = [[i for i in group.split("\n")] for group in f.read().split("\n\n")][1]

        instructions = []

        for line in r:
            inst_line = []
            for nbr in line.split(" "):
                if nbr.isdigit():
                    inst_line.append(int(nbr))
            instructions.append(inst_line)
    return instructions


def part1(stacks_input: list[list], instructions: list[list]) -> str:
    stacks = deepcopy(stacks_input)

    for instruction in instructions:
        nbr_crates = instruction[0]
        from_stack = instruction[1] - 1
        to_stack = instruction[2] - 1

        for _ in range(nbr_crates):
            stacks[to_stack].append(stacks[from_stack].pop())

    return "".join([line[-1] for line in stacks])


def part2(stacks_input: list[list], instructions: list[list]) -> str:
    stacks = deepcopy(stacks_input)
    for instruction in instructions:
        nbr_crates = instruction[0]
        from_stack = instruction[1] - 1
        to_stack = instruction[2] - 1

        stacks[to_stack].extend(
            stacks[from_stack][len(stacks[from_stack]) - nbr_crates :]
        )

        for _ in range(nbr_crates):
            stacks[from_stack].pop()

    return "".join([line[-1] for line in stacks])


inp_stacks = parse_input_stacks("input.txt")
inp_instructions = parse_input_instructions("input.txt")
# inp = parse_input("input.txt")
print(inp_stacks)
print(inp_instructions)
print(part1(inp_stacks, inp_instructions))
print(part2(inp_stacks, inp_instructions))
# print(part2(inp))
