import random

a = {}
exitCondition = True
counter = 0

def randomZero():
    print("randomZero press 'q' for quit")
    for i in a:
        theQ0 = input(a[i] + " : ? ")
        if theQ0 == 'q':
            global exitCondition
            exitCondition = False

        elif theQ0.lower() == i.lower():

            print("+1 point")
            global counter
            counter += 1
        else:

            counter = 0

        return


def randomOne():
    print("randomOne press 'q' for quit")
    for i in a:
        theQ1 = input(i + " : ? ")
        if theQ1 == 'q':
            global exitCondition
            exitCondition = False
        elif theQ1.lower() == a[i].lower():

            print("+1 point")
            global counter
            counter += 1
        else:

            counter = 0

        return


def randomNumber():
    randomNum = random.randint(0, 1)
    if randomNum == 0:
        randomZero()
    elif randomNum == 1:
        randomOne()
    else:
        print("Something did wrong...")


def state(theFileName):
    with open(theFileName, 'r') as fh:
        fh = fh.readlines()
        randNum = random.randint(0, len(fh) - 1)
        chosen = fh[randNum]

        splitLine = chosen.rstrip("\n").split(':')

        splitLine[0] = splitLine[0].replace(" ", "")  # removes the space insof ' Eis'
        splitLine[1] = splitLine[1].replace(" ", "")  # removes the space ins of 'Dondurma '

        a[splitLine[0]] = "".join(splitLine[1])

    return


def scoreTable():
    print("Congratulations You got 10 points!")


def mainGame(fileName):
    while exitCondition == True:
        if counter == 10:
            scoreTable()
            break
        state(fileName)
        randomNumber()
        a.clear()
    else:
        print("BYE...")


if __name__ == '__main__':
    mainGame()
