import math


class XOGame:
    def start(self):
        self.fieldR = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]
        self.fieldC = [["7", "4", "1"], ["8", "5", "2"], ["9", "6", "3"]]
        self.fieldD = [["7", "5", "3"], ["9", "5", "1"]]
        self.field = self.fieldR

    def playGame(self):
        self.start()
        self.gameCycle()


    def UI_showField(self):
        for row in self.field:
            print(row)

    def markPlace(self, matrix, place, mark):
        for row in matrix:
            if place in row:
                row[row.index(place)] = mark
        return matrix

    def turn(self, place, mark):
        self.field = self.markPlace(self.field, place, mark)
        self.fieldR = self.markPlace(self.fieldR, place, mark)
        self.fieldC = self.markPlace(self.fieldC, place, mark)
        self.fieldD = self.markPlace(self.fieldD, place, mark)

    def gameCycle(self):
        boolTurn = True
        turnPlayer = "O"
        while True:
            self.UI_showField()
            if self.checkWin(turnPlayer):
                print("!!!!! YOU WON !!!!!")
                return False
            if boolTurn:
                turnPlayer = "X"
            else:
                turnPlayer = "O"
            self.turnInput(turnPlayer)
            boolTurn = not boolTurn

    def turnInput(self, mark):
        yourTurn = input("SELECT PLACE ")
        self.turn(yourTurn, mark)

    def checkWin(self, mark):
        if self.checkRows(self.fieldR, mark) or self.checkRows(self.fieldC, mark) or self.checkRows(self.fieldD, mark):
            return True
        else:
            return False

    def checkRows(self, matrix, mark):
        for row in matrix:
            ifWin = bool(math.floor(row.count(mark) / 3))
            if ifWin:
                return ifWin
        return False


game = XOGame()
game.playGame()
