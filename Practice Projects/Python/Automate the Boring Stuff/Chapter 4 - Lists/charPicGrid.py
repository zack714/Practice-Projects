#the goal of this program is to shift this heart upwards with nested loops.

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#go to the last list, append the 0th value, go up to the penultimate list, append the 0th value, and so on

#X originally ranged from (0,9)! This caused an out of bounds error!
for x in range(0,6):
    #move up along y
    for y in range(8,-1,-1):
        #print("x = "+str(x)+ ", y = "+str(y))
        print(grid[y][x],end="")
    print()

