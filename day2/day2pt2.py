from loguru import logger

# Opponent
# A, B, C => Rock, Paper, Scissors

# me
# Rock = 1; Paper = 2, Scissors = 3
# X => need to lose (0), Y => need to draw (3), Z => need to win (6)
playValues = {"A": 1, "B": 2, "C": 3}
outcomeValues = {"X": 0, "Y": 3, "Z": 6}
winPlay = {"A": "B", "B": "C", "C": "A"}
loosePlay = {"A": "C", "B": "A", "C": "B"}


def calcPlay(opponent, outcome):
    match outcome:
        case "Y":
            return playValues[opponent]
        case "X":
            return playValues[loosePlay[opponent]]
        case "Z":
            return playValues[winPlay[opponent]]


def main():
    """
    https://adventofcode.com/2022/day/2
    """
    day = "2"
    part = "2"

    logger.info(f"Day {day} part {part}")
    # fileInputName = "day" + day + "exampleinput.txt"
    fileInputName = "day" + day + "input.txt"

    # load input
    result = ""
    logger.info(f"Working with file: {fileInputName}")

    result = 0

    with open(fileInputName, "r") as inputFile:
        for line in inputFile.readlines():
            line = line.strip().replace(" ", "")
            opponent, outcome = line[0], line[1]
            result += outcomeValues[outcome] + calcPlay(opponent, outcome)

    logger.info(f"Day {day} part {part} result: {result}")


if __name__ == "__main__":
    main()
