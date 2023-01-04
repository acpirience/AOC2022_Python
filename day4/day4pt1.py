from loguru import logger


def section_include_section(left, right):
    if left[0] <= right[0] and right[1] <= left[1]:
        return True
    if right[0] <= left[0] and left[1] <= right[1]:
        return True
    return False


def main():
    """
    https://adventofcode.com/2022/day/4
    """
    day = "4"
    part = "1"

    logger.info(f"Day {day} part {part}")
    # fileInputName = "day" + day + "exampleinput.txt"
    fileInputName = "day" + day + "input.txt"

    # load input
    result = ""
    logger.info(f"Working with file: {fileInputName}")

    result = 0

    with open(fileInputName, "r") as inputFile:
        for line in inputFile.readlines():
            left, right = line.strip().split(",")
            left = [int(x) for x in left.split("-")]
            right = [int(x) for x in right.split("-")]
            if section_include_section(left, right):
                result += 1

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
