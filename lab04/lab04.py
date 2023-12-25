from Stack import Stack

# def printMaze(maze):
# 	for row in range(len(maze)):
# 		for col in range(len(maze[0])):
# 			print("|{:<2}".format(maze[row][col]), sep='',end='')
# 		print("|")
# 	return

def solveMaze(maze, startX, startY):
    s = Stack()
    step = 1
    s.push([startX, startY])
    solution = False
    
    while not s.isEmpty() and not solution:
        x = s.peek()[0]
        y = s.peek()[1]

        if maze[x][y] == " ":
            maze[x][y] = step
            step += 1
        if maze[x][y] == "G":
            solution = True
            break

        if x > 0: # North
            x -= 1
        if maze[x][y] != " " and maze[x][y] != 'G':
            x += 1
        if maze[x][y] == " " or maze[x][y] == 'G': 
            s.push([x, y])
            continue

        if y > 0: # West
            y -= 1
        if maze[x][y] != " " and maze[x][y] != 'G':
            y += 1
        if maze[x][y] == ' ' or maze[x][y] == 'G': 
            s.push([x, y])
            continue

        if x < len(maze[0]): # South
            x += 1
        if maze[x][y] != " " and maze[x][y] != 'G':
            x -= 1
        if maze[x][y] == ' ' or maze[x][y] == 'G': 
            s.push([x, y])
            continue

        if y < len(maze): # East
            y += 1
        if maze[x][y] != " " and maze[x][y] != 'G':
            y -= 1
        if maze[x][y] == ' ' or maze [x][y] == 'G':
            s.push([x, y])
            continue

        else:
            s.pop()

    return solution
	