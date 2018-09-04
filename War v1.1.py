import random

cardNames = {2 : "Двойка", 3 : "Тройка", 4 : "Четверка", 5 : "Пятерка", 6 : "Шестерка",
             7 : "Семерка", 8 : "Восьмерка", 9 : "Девятка", 10 : "Десятка", 11 : "Валет",
             12 : "Дама", 13 : "Король", 14 : "Туз"}

class Card:
    def __init__(self, value, name):
        self.value = value
        self.name = name

class Deck:
    def __init__(self, numberOfCards):
        self.cardlist = []
        if numberOfCards == 36:
            generationStart = 6
        elif numberOfCards == 52:
            generationStart = 2
        for i in range(generationStart, 15):
            cardName = cardNames[i]
            self.cardlist.append(Card(i, cardName + " Червей"))
            self.cardlist.append(Card(i, cardName + " Бубей"))
            self.cardlist.append(Card(i, cardName + " Треф"))
            self.cardlist.append(Card(i, cardName + " Пик"))

def generateDeck():
    x = input("Сколько карт в колоде? (36 или 52) ")
    if x.isdigit():
        x = int(x)
        if x == 36 or x == 52:
            newDeck = Deck(x)
            return newDeck
        print("Ошибка!")
        return generateDeck()
    print("Ошибка!")
    return generateDeck()

def askPlayerNumber():
    x = input("Число игроков? (от 2 до 8) ")
    if x.isdigit():
        x = int(x)
        if x >= 2 and x <= 8:
            return x
        print("Ошибка!")
        return askPlayerNumber()
    print("Ошибка!")
    return askPlayerNumber()

def getCard(hand):
    x = hand[0]
    return x

def getCardName(hand):
    x = hand[0]
    return x.name

def getCardValue(hand):
    x = hand[0]
    return x.value

def removeACard(hand):
    hand.pop(0)
    return hand

def isWar(value, warriors):
    #print(warriors) #debug
    #print("len(warriors) = " + str(len(warriors))) #debug
    n = 0
    for j in range(0, len(warriors)):
        if not originalDeck.cardlist[warriors[j]]:
            continue
        if getCardValue(originalDeck.cardlist[warriors[j]]) == value:
            n += 1
    #print("n = " + str(n)) #debug
    if n > 1:
        return True
    return False

def getWarParticipants(value, warriors):
    participants = []
    for j in range(0, len(warriors)):
        if not originalDeck.cardlist[warriors[j]]:
            continue
        if getCardValue(originalDeck.cardlist[warriors[j]]) == value:
            participants.append(j)
    return participants

def getRoundWinner(value, contenders):
    for j in range(0, len(contenders)):
        if not originalDeck.cardlist[contenders[j]]:
            continue
        if getCardValue(originalDeck.cardlist[contenders[j]]) == value:
            return contenders[j]

def isGameOver():
    n = 0
    for i in range(0, players):
        if originalDeck.cardlist[i]:
            n += 1
    return bool(n == 1)

def getGameWinner():
    for i in range(0, players):
        if originalDeck.cardlist[i]:
            return i

def tieBreaker():
    print("Достигнут лимит кругов!")
    mostCards = 0
    for i in range(0, players):
        if not originalDeck.cardlist[i]:
            continue
        if len(originalDeck.cardlist[i]) > mostCards:
            mostCards = len(originalDeck.cardlist[i])
            gameWinner = i
        print("У игрока " + str(i + 1) + " осталось " + str(len(originalDeck.cardlist[i])) + " карт")
    print("\nИгрок " + str(gameWinner + 1) + " победил!")
            
originalDeck = generateDeck()
players = askPlayerNumber()

random.shuffle(originalDeck.cardlist)
length = len(originalDeck.cardlist)
originalDeck.cardlist = [originalDeck.cardlist[i * length // players: (i + 1) * length // players] for i in range(players)]

allPlayers = []
for i in range(0, players):
    allPlayers.append(i)

skip = False

roundCounter = 0

#print(allPlayers) #debug

while True:
    if not skip:
        print('\nВведите "+" чтобы начать новый круг')
        print('Введите "Карты [номер игрока]" чтобы узнать число карт')
        print('Введите "Пропустить" чтобы пропустить игру до конца')
        userInput = str(input())
    if "Пропустить" in userInput and len(userInput) == 10:
        userInput = "+"
        skip = True
    if ("Карты " in userInput and len(userInput) == 7 and userInput[6].isdigit() 
        and int(userInput[6]) > 0 and int(userInput[6]) <= len(allPlayers)):
        print(len(originalDeck.cardlist[int(userInput[6]) - 1])) 
    if userInput == "+":
        highestValue = 0
        table = []

        for i in range(0, players):
            if not originalDeck.cardlist[i]:
                continue
            print("Игрок " + str(i + 1) + " сбрасывает карту: " + getCardName(originalDeck.cardlist[i]))
            #print(str(getCardValue(originalDeck.cardlist[i]))) #debug
            if getCardValue(originalDeck.cardlist[i]) > highestValue:
                highestValue = getCardValue(originalDeck.cardlist[i])
            table.append(getCard(originalDeck.cardlist[i]))
        
        firstWar = True
        cancelWar = False
        #print("highest: " + str(highestValue)) #debug

        while True:

            if firstWar:
                z = allPlayers
            else:
                z = warParticipants

            if isWar(highestValue, z) and not cancelWar:
                print("\nСпор!\n")
                if firstWar:
                    warParticipants = getWarParticipants(highestValue, z)
                    for i in range(0, len(warParticipants)):
                        if not originalDeck.cardlist[warParticipants[i]]:
                            print("Спор не состоялся!")
                            cancelWar = True
                highestValue = 0
                #print(warParticipants) #debug
                if firstWar:
                    for i in range(0, players):
                        if not originalDeck.cardlist[i]:
                            continue
                        originalDeck.cardlist[i] = removeACard(originalDeck.cardlist[i])
                else:
                    for i in range(0, len(warParticipants)):
                        if not originalDeck.cardlist[warParticipants[i]]:
                            continue
                        originalDeck.cardlist[warParticipants[i]] = removeACard(originalDeck.cardlist[warParticipants[i]])

                for i in range(0, len(warParticipants)):
                    if cancelWar:
                        break
                    if not originalDeck.cardlist[warParticipants[i]]:
                        print("У игрока " + str(warParticipants[i] + 1) + " не осталось карт для спора")
                        continue
                    print("Игрок " + str(warParticipants[i] + 1) + " сбрасывает карту: " + getCardName(originalDeck.cardlist[warParticipants[i]]))
                    if getCardValue(originalDeck.cardlist[warParticipants[i]]) > highestValue:
                        highestValue = getCardValue(originalDeck.cardlist[warParticipants[i]])
                    table.append(getCard(originalDeck.cardlist[warParticipants[i]]))
                firstWar = False
                #print("highest value (war): " + str(highestValue)) #debug
            else:
                #print("new highest: " + str(highestValue)) #debug
                winner = getRoundWinner(highestValue, z)
                print("\nИгрок " + str(winner + 1) + " выигрывает раунд!\n")
                originalDeck.cardlist[winner].extend(table)
                if not firstWar:
                    for i in range(0, len(warParticipants)):
                        if not originalDeck.cardlist[warParticipants[i]]:
                            continue
                        originalDeck.cardlist[warParticipants[i]] = removeACard(originalDeck.cardlist[warParticipants[i]])
                else:
                    for i in range(0, players):
                        if not originalDeck.cardlist[i]:
                            continue
                        originalDeck.cardlist[i] = removeACard(originalDeck.cardlist[i])
                break
    if isGameOver():
        print("Игра окончена!")
        print("Игрок " + str(getGameWinner() + 1) + " победил!")
        break

    if userInput == "+":
        roundCounter += 1
        #print(str(roundCounter)) #debug

    if roundCounter == 2000:
        tieBreaker()
        break

input()
