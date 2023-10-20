import Clipboard


def atClass(arr):
    clipboard = Clipboard.Clipboard(arr[0], int(arr[1]), float(arr[2]), int(arr[3]))
    return clipboard


def readfileToClipboardList(nameFile):
    myArray = []

    fo = open(nameFile, "r")
    for line in fo:
        tmp = []
        if len(line.split()) == 4:
            for nbr in line.split():
                tmp.append(nbr)
            clipboard = atClass(tmp)
            myArray.append(clipboard)
        else:
            priceTmp = int(line.split()[0])
            myArray.append(priceTmp)

    return myArray


def writeToFile(arr):

    with open("output.txt", 'w') as file:
        if arr is None:
            file.write("no clipboards")
            return 0
        for j in arr:
            file.write(str(j) + " ")


def sortByStorage(tablets):
    tablets = sorted(tablets, key=lambda x: x.sStorage)

    i = len(tablets) - 1
    maxStorageWithThisMoney = tablets[i].sStorage
    tmpTablets = []

    while maxStorageWithThisMoney == tablets[i].sStorage and i >= 0:
        tmpTablets.append(tablets[i])
        i = i - 1

    return tmpTablets


def sortByRating(tablets):
    tablets = sorted(tablets, key=lambda x: x.sRating)
    i = len(tablets) - 1
    maxRatingWithThisMoney = tablets[i].sRating
    tmpTablets = []

    while maxRatingWithThisMoney == tablets[i].sRating and i >= 0:
        tmpTablets.append(tablets[i])
        i = i - 1

    return tmpTablets


def checkTabletsName(tablets):
    tmpTablets = []
    for i in range(len(tablets)):
        if tablets[i].sName == 'Samsung' or tablets[i].sName == 'Asus':
            tmpTablets.append(tablets[i])
    if len(tmpTablets) != 0:
        return tmpTablets[len(tmpTablets) - 1]

    return tablets[len(tablets) - 1]


def solution(arr, money):
    tablets = []

    for i in range(len(arr)):
        if arr[i].sPrice < money:
            tablets.append(arr[i])

    if len(tablets):
        tablets = sortByStorage(tablets)
        print(tablets)
        if len(tablets) == 1:
            return tablets[0]

        tablets = sortByRating(tablets)
        print(tablets)
        if len(tablets) == 1:
            return tablets[0]
        print(checkTabletsName(tablets))
        return checkTabletsName(tablets)


def dataToList(clipboard):
    if clipboard is None:
        return None
    dataList = [clipboard.sName, clipboard.sStorage, clipboard.sRating, clipboard.sPrice]
    return dataList


tablet = readfileToClipboardList('inputSmallestPrice.txt')
if len(tablet) > 0:
    price = tablet[len(tablet) - 1]
    tablet.pop(len(tablet) - 1)
    writeToFile(dataToList(solution(tablet, price)))
