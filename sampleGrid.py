enemyGrid = []

randomRow = 0
randomCol = 0
direction = 0 #1 is north, 2 is south, 3 is east, 4 is west


for i in range(0,10): #temporary grid of "o"'s
  enemyGrid.append(["-" for j in range(0, 10)])

enemyGrid[1][0] = "3"
enemyGrid[2][0] = "3"
enemyGrid[3][0] = "3"


enemyGrid[2][2] = "5"
enemyGrid[3][2] = "5"
enemyGrid[4][2] = "5"
enemyGrid[5][2] = "5"
enemyGrid[6][2] = "5"

enemyGrid[8][1] = "4"
enemyGrid[8][2] = "4"
enemyGrid[8][3] = "4"
enemyGrid[8][4] = "4"

enemyGrid[0][5] = "E"
enemyGrid[0][6] = "E"
enemyGrid[0][7] = "E"

enemyGrid[5][6] = "2"
enemyGrid[6][6] = "2"