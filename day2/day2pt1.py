from loguru import logger


def main():
    """
    https://adventofcode.com/2022/day/2
    """
    day = "2"
    part = "1"

    logger.info(f"Day {day} part {part}")
    # fileInputName = "day" + day + "exampleinput.txt"
    fileInputName = "day" + day + "input.txt"

    # load input
    result = ""
    logger.info(f"Working with file: {fileInputName}")

    # Opponent
    # A, B, C => Rock, Paper, Scissors

    # me
    # X = Rock = 1; Y = Paper = 2, Z = Scissors = 3

    playValues = {"X": 1, "Y": 2, "Z": 3}
    winLosses = {
        "AX": 3,
        "AY": 6,
        "AZ": 0,
        "BX": 0,
        "BY": 3,
        "BZ": 6,
        "CX": 6,
        "CY": 0,
        "CZ": 3,
    }

    result = 0

    with open(fileInputName, "r") as inputFile:
        for line in inputFile.readlines():
            line = line.strip().replace(" ", "")
            result += winLosses[line] + playValues[line[1]]

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
