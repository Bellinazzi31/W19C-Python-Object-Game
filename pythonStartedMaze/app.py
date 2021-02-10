import gameboard
import player

print("Welcome to the game!")
print("Instructions: ")
print("To move up: w")
print("To move down: s")
print("To move left: a")
print("To move right: d")
print("Wall = *")
print("Enemiy = #")
print("Coin = $")
print("Enemies will move randomly everytime you move")
print("Try to get to the end! Good Luck!")
print("-----------------------------")

# TODO
# Create a new GameBoard called board
board = gameboard.GameBoard()
# Create a new Player called played starting at position 3,2
player = player.Player(9, 7)

while True:
    board.randomEnemies(player.rowPosition, player.columnPosition)
    board.printBoard(player.rowPosition, player.columnPosition)
    selection = input("Make a move: ")
    # TODO
    # Move the player through the boar
    if selection == "w":
        if board.checkMove(player.rowPosition - 1 , player.columnPosition):
            player.moveUp()
            board.collectCoins(player.rowPosition, player.columnPosition)
    elif selection == 's':
        if board.checkMove(player.rowPosition + 1 , player.columnPosition):
            player.moveDown()
            board.collectCoins(player.rowPosition, player.columnPosition)
    elif selection == 'a':
        if board.checkMove(player.rowPosition, player.columnPosition - 1):
            player.moveLeft()
            board.collectCoins(player.rowPosition, player.columnPosition)
    elif selection == 'd':
        if board.checkMove(player.rowPosition, player.columnPosition + 1):
            player.moveRight()
            board.collectCoins(player.rowPosition, player.columnPosition)
    # Check if the player has won, if so print a message and break the loop!        
    if board.checkWin(player.rowPosition, player.columnPosition):
        print("You Won") 
        break
    if board.chcekLose(player.rowPosition, player.columnPosition):
        print("You Lose")
        break 
print("you collected ", board.coins, " coins")                              
    
   