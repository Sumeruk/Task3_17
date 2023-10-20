class Clipboard:

    def __init__(self, name, storage, rating, price):
        self.sName = name
        self.sStorage = storage
        self.sRating = rating
        self.sPrice = price

    def printClipboard(self):
        print(self.sName, " ", self.sStorage, " ", self.sRating, self.sPrice)

