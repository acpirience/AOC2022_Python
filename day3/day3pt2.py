from loguru import logger


def common_letters(first, second):
    common = ""
    for car in first:
        if car in second and car not in common:
            common += car
    return common


def main():
    """
    https://adventofcode.com/2022/day/3
    """
    day = "3"
    part = "2"

    logger.info(f"Day {day} part {part}")
    # fileInputName = "day" + day + "exampleinput.txt"
    fileInputName = "day" + day + "input.txt"

    # load input
    result = ""
    logger.info(f"Working with file: {fileInputName}")

    result = 0

    with open(fileInputName, "r") as inputFile:
        group = []
        for line in inputFile.readlines():
            group.append(line.strip())
            if len(group) == 3:
                car = common_letters(
                    common_letters(group[0], group[1]),
                    common_letters(group[1], group[2]),
                )
                if ord("a") <= ord(car) <= ord("z"):
                    result += ord(car) - ord("a") + 1
                else:
                    result += ord(car) - ord("A") + 1 + 26
                group = []

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
