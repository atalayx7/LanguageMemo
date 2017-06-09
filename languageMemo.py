from game import mainGame


def addnewWord():
    whichLang = int(input("1.English - German\n2.Turkish - English\n3.German - Turkish\nSelection : "))

    if whichLang == 1:
        senditToFile("EnglishGerman")
    elif whichLang == 2:
        senditToFile("TurkishEnglish")
    elif whichLang == 3:
        senditToFile("GermanTurkish")


def senditToFile(theLangs):
    newWord = input("Word : ")
    newWord2 = input("The meaning" + " : ")
    theLangs += '.txt'
    with open(theLangs, 'a') as theFile:
        theFile.write(newWord + " : " + newWord2 + "\n")


def listheWords():
    whichLanguage = int(
        input("1.English - German\n2.Turkish - English\n3.German - Turkish\nSelection : "))

    if whichLanguage == 1:
        listIt("EnglishGerman")
    elif whichLanguage == 2:
        listIt("TurkishEnglish")
    elif whichLanguage == 3:
        listIt("GermanTurkish")


def listIt(theChoice):
    theChoice += '.txt'
    with open(theChoice, 'r') as theFile:
        displayIt = theFile.read()
        print(displayIt)


def let_thegameStart():
    langforGame = int(input("1.English - German\n2.Turkish - English\n3.German - Turkish\nSelection : "))

    if langforGame == 1:
        mainGame("EnglishGerman.txt")
    elif langforGame == 2:
        mainGame("TurkishEnglish.txt")
    elif langforGame == 3:
        mainGame("GermanTurkish.txt")


def display_theLanguages(game_language):
    game_language += '.txt'
    with open(game_language, 'r') as fh:
        theList = fh.readlines()


def main():
    while True:

        menuPref = int(input("\n1. Add New Word\n2. Display the words\n3. Let the game start\n4. Exit\nSelection : "))
        if menuPref == 1:

            addnewWord()  # Add new word

        elif menuPref == 2:
            listheWords()  # Display the words

        elif menuPref == 3:
            let_thegameStart()  # start the game

        elif menuPref == 4:
            print("BYE...")

            break  # exit
        else:
            print("Invalid selection, try again...")  # invalid input
            continue


if __name__ == '__main__':
    main()
