from loguru import logger


def main():
    """
    https://adventofcode.com/2022/day/1
    """
    day = "1"
    part = "1"

    logger.info(f"Day {day} part {part}")
    #fileInputName = "day" + day + "exampleinput.txt"
    fileInputName = "day" + day + "input.txt"

    # load input
    result = ""
    logger.info(f"Working with file: {fileInputName}")

    elvesCalories = [0]

    with open(fileInputName, "r") as inputFile:
        curIdx = 0
        for line in inputFile.readlines():
            if line.strip():
                elvesCalories[curIdx] += int(line)
            else:
                curIdx += 1
                elvesCalories.append(0)

    result = max(elvesCalories)

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
