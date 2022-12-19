from loguru import logger


def main():
    """
    https://adventofcode.com/2022/day/1
    """
    day = "1"
    part = "1"

    logger.info(f"Day {day} part {part}")
    fileInputName = "day" + day + "exampleinput.txt"
    #    fileInputName ="day" + day + "input.txt"

    # load input
    result = ""
    logger.info(f"Working with file: {fileInputName}")

    with open(fileInputName, "r") as inputFile:
        for line in inputFile.readlines():
            pass

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
