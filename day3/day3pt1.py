from loguru import logger


def main():
    """
    https://adventofcode.com/2022/day/3
    """
    day = "3"
    part = "1"

    logger.info(f"Day {day} part {part}")
    # fileInputName = "day" + day + "exampleinput.txt"
    fileInputName = "day" + day + "input.txt"

    # load input
    logger.info(f"Working with file: {fileInputName}")

    result = 0

    with open(fileInputName, "r") as inputFile:
        for line in inputFile.readlines():
            line = line.strip()
            length = len(line) // 2
            begin, end = line[0:length], line[length:]
            for car in begin:
                if car in end:
                    if ord("a") <= ord(car) <= ord("z"):
                        result += ord(car) - ord("a") + 1
                    else:
                        result += ord(car) - ord("A") + 1 + 26
                    break

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
