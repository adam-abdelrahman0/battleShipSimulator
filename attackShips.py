
def attackShip(row, col, arr):
  #meant to check if there is a skipped space between two checkered hits
  if (row > 1):
    if (arr[row - 2][col] == "o"):
      arr[row - 1][col] = "o"
  

  return arr