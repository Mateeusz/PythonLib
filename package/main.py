
class Item():

    name = "name";
    quantity = 0;

    def __init__(self, _name, _quantity):
        self.name = _name
        self.quantity = _quantity

    def __str__(self):
        print("Produkt: ", self.name , " Ilość: ", self.quantity + " sztuk.")


class Generator():

    partyType = ["urodziny", "kolacja", "obiad"]
    productList =[]
    formFile = []
    parameters = ["nie określono","1(domyślnie)"]

    def loadFromFile(self, name):
        with open(name) as f:
            self.formFile = f.readlines()

            self.formFile = [x.strip() for x in self.formFile]

    def generateList(self, _partyType):
        #print(self.formFile, _partyType, self.formFile.__len__())
        temp = self.formFile.__len__()
        self.parameters[0] = _partyType

        for i in range (self.formFile.__len__()):
            # print(i)

            if(self.formFile[i] == _partyType):
                print("Typ imprezy: ", self.formFile[i])
                temp = i
            if(i > temp and self.formFile[i] != "==="):
                print(self.formFile[i])
                item = Item(self.formFile[i].split( )[0], self.formFile[i].split( )[1])
                self.productList.append(item)

    def refreshQuantity(self, guestNumber):
        self.parameters[1] = guestNumber
        for i in range(self.productList.__len__()):
            self.productList[i].quantity = int(self.productList[i].quantity)*int(guestNumber)

    def printList(self):
        print("...imprezy:",self.parameters[0],", Ilość gości:",self.parameters[1])
        for i in range(self.productList.__len__()):
            print("Produkt:", self.productList[i].name, ", Ilość:", self.productList[i].quantity, "szt.")



