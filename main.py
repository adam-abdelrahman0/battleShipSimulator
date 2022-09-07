import random
from sampleGrid import enemyGrid
from attackShips import attackShip

grid = []     #grid of enemy ships
enemyShips = ["2","3","4","5","E"]
alreadyShot = []

mode = input("Automated or Game-speed? (A/G) ")

moves = 0;
hits = 0;

randomRow = 0 #for later
randomCol = 0 #also for later
game = 0      #for maintinaing the game loop
seeBoard = 0;

def showBoard(board):
  for i in board:
    for j in i:
      print(j, end = " ")
    print()

for i in range(0,10): #temporary grid of "o"'s until I make the random ship generator'
  grid.append(["-" for j in range(0, 10)])

'''loop for game-speed game (played by a human)'''
while (game >= 0 and mode.lower() == "g"):
  moveReady =  input("Next move? (Y/N) ")
  if (moveReady.lower() == "n"):
    game = -10033 #this is below 0
  else:
    randomRow = random.randint(0,9)
    randomCol = random.randint(0,9)
    
    while ((randomRow + randomCol) % 2 == 0 or (alreadyShot.count(str(randomRow) + " " + str(randomCol)) > 0)):
      randomRow = random.randint(0,9)
      randomCol = random.randint(0,9)
    
    alreadyShot.append(str(randomRow) + " " + str(randomCol))
    
    print(str(randomRow) + ", " + str(randomCol))
    if (enemyShips.count(enemyGrid[randomRo vvvvvvvvvv   w][randomCol]) > 0):
      
      grid[randomRow][randomCol] = "o"

      grid = attackShip(randomRow, randomCol, grid)
      
    else:
      grid[randomRow][randomCol] = "x"
    
    moves = moves + 1 #tallies the number of moves
    
    seeBoard = input("See board? (Y/N) ")
    if (seeBoard.lower() == "y"):
      showBoard(grid);



'''automated game (plays until all ships have been shot'''

while (moves < 50 and mode.lower() == "a"): #moves can be changed
  randomRow = random.randint(0,9)
  randomCol = random.randint(0,9)
    
  while ((randomRow + randomCol) % 2 == 0 or (alreadyShot.count(str(randomRow) + " " + str(randomCol)) > 0)):
    randomRow = random.randint(0,9)
    randomCol = random.randint(0,9)

  alreadyShot.append(str(randomRow) + " " + str(randomCol))
    
  if (enemyShips.count(enemyGrid[randomRow][randomCol]) > 0):
      grid[randomRow][randomCol] = "o"
      hits = hits + 1
      grid = attackShip(randomRow, randomCol, grid)
  else:
      grid[randomRow][randomCol] = "x"
    
  moves = moves + 1 #tallies the number of moves


print("\n Board: \n")
showBoard(grid)
print("\n" + str(moves) + " moves \n")
print("Enemy board: \n")
showBoard(enemyGrid)


