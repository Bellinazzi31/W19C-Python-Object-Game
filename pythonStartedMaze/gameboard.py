from random import randint
class GameBoard:
    def __init__(self):
        self.winningRow = 0
        self.winningColumn = 2
        self.coins=0
        self.board = [
            [" * ", " * ", "   ", " * ", " * "," * ", " * ", " * ", " * ", " * "],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * ",
            ],
            [
                " * ",
                "   ",
                " * ",
                "   ",
                "   ",
                "   ",
                " * ",
                " * ",
                "   ",
                " * ",
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                " $ ",
                "   ",
                "   ",
                " $ ",
                "   ",
                " * ",
            ],
            [
                " * ",
                " $ ",
                "   ",
                "   ",
                " * ",
                " * ",
                "   ",
                "   ",
                " * ",
                " * ",
            ],
            [
                " * ",
                "   ",
                " * ",
                " * ",
                "   ",
                " $ ",
                " * ",
                " $ ",
                "   ",
                " * ",
            ],
            [
                " * ",
                " $ ",
                "   ",
                "   ",
                "   ",
                " * ",
                "   ",
                " $ ",
                "   ",
                " * ",
            ],
             [
                " * ",
                "   ",
                " * ",
                " * ",
                "   ",
                " * ",
                " $ ",
                " * ",
                "   ",
                " * ",
            ],
            [
                " * ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                "   ",
                " $ ",
                " $ ",
                " * ",
            ],
            [" * ", " * ", " * ", " * ", " * "," * ", " * ", "   ", " * ", " * " ]
        ]

    def printBoard(self, playerRow, playerColumn):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == playerRow and j == playerColumn:
                    print(" P ", end="")
                else:
                    print(self.board[i][j], end="")
            print("")
        

    def checkMove(self, testRow, testColumn):
        if self.board[testRow][testColumn].find("*") != -1:
            print("Can't move there!")
            return False
        return True

    # TODO
    # Return True if the player is in the winning column and row
    # Return False otherwise
    def checkWin(self, playerRow, playerColumn):
        if playerRow== self.winningRow and playerColumn == self.winningColumn:
            return True
        return False
    def checkLose(self,playerRow, playerColumn):
        if self.board[playerRow][playerColumn]==" # ":
            return True
        return False
    def collectCoins(self,playerRow, playerColumn):
        if self.board[playerRow][playerColumn]==" $ ":
            self.board[playerRow][playerColumn]="   "
            self.coins=self.coins+1

    def randomEnemies(self,row,col):
        for i in range(len(self.board)):
            for j in range (len(self.board[i])):
                if self.board[i][j]==" # ":
                    self.board[i][j]="   "
        enemies = 0
        while enemies < 10:
            i=randint(1,8) #enemies to be between the borders
            j=randint(1,8)
            if self.board[i][j]=="   " and (i != row or j!=col):
                self.board[i][j]=" # "
                enemies = enemies +1