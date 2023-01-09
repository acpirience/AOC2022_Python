from loguru import logger
from collections import deque


def parse_stack(stack):
    len_tot = ((len(stack[0]) - 1) // 4) + 1
    storage = [[] for x in range(len_tot)]
    for line in stack:
        for i in range(len_tot):
            if ((i * 4) + 1) < len(line) and line[(i * 4) + 1] != " ":
                storage[i].append(line[(i * 4) + 1])

    return storage


def play_instruction(instruction, storage):
    instruction_parts = instruction.split(" ")
    nb = int(instruction_parts[1])
    stack_from = int(instruction_parts[3]) - 1
    stack_to = int(instruction_parts[5]) - 1

    for _ in range(nb):
        x = storage[stack_from].pop()
        storage[stack_to].append(x)

    return storage


def main():
    """
    https://adventofcode.com/2022/day/5
    """
    day = "5"
    part = "1"

    logger.info(f"Day {day} part {part}")
    # fileInputName = "day" + day + "exampleinput.txt"
    fileInputName = "day" + day + "input.txt"

    # load input
    logger.info(f"Working with file: {fileInputName}")

    stack = deque()
    instructions = []

    with open(fileInputName, "r") as inputFile:
        for line in inputFile.readlines():
            if line.lstrip().startswith("["):
                stack.appendleft(line.rstrip())
            elif line.startswith("move"):
                instructions.append(line.rstrip())

    storage = parse_stack(stack)

    for instruction in instructions:
        storage = play_instruction(instruction, storage)

    result = "".join([x[-1] for x in storage])

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
