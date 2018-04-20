import numpy as np
import sys
np.set_printoptions(threshold=np.nan)

sys.setrecursionlimit(2000)

#########################################
# changed: add cordinated in initialization ################################
class cell:
    def __init__(self, char, y, x):
        self.char = char
        self.visited = False
        self.frontier = False
        self.y = y
        self.x = x
        self.cost = 0
        self.distance = 0
        self.path_visited = False
        self.parent = None

class maze:
    def __init__(self, file):
        #########Get the length and width of a maze
        #########Attribute width,length
        
        self.length = 0
        with open(file, 'r') as in_file:
            for line in in_file:
                self.length += 1
        self.width = len(line)
        
        #########Create a maze matrix in 1d
        self.cell_matrix = []
        with open(file,'r') as matrix:
            for line in matrix:  
                for char in line:
                    if char == '%': self.cell_matrix.append(cell('%'))
                    if char == ' ': self.cell_matrix.append(cell(' '))
                    if char == 'P': self.cell_matrix.append(cell('P'))
                    if char == '.': self.cell_matrix.append(cell('.'))
        self.cell_matrix = np.array(self.cell_matrix)
        self.cell_matrix = self.cell_matrix.reshape([self.length,self.width])
        
        
        #########Here is the solution matrix, initially is the cell_matrix
        self.solution_matrix = self.cell_matrix
        #print(self.solution_matrix.shape[0])
        #print(len(self.cell_matrix))
        
        
        #########Here is checking the end_row and end_col and assign the attribute
        for i in range(0,self.cell_matrix.shape[0]):
            for j in range(0,self.cell_matrix.shape[1]):
                if self.cell_matrix[i][j].char == '.':
                    end_row = i
                    end_col = j
        
                if self.cell_matrix[i][j].char == 'P':
                    start_row = i
                    start_col = j
        
        self.end_row = end_row
        self.end_col = end_col
        self.start_row = start_row
        self.start_col = start_col       
        #########Solution cost
        self.solution_cost = 0





#######################################################################
# A search 
#######################################################################
def A_search():
	# expand the one more step of frontier
	# check whether the cell is included in frontier list or not
	nodes_expand = 0
	while MazeCell[end.y*width + end.x].visited == False:
		frontier.sort( key = lambda cell_elements: (cell_elements.cost+cell_elements.distance))


		
		for i in range(0, len(frontier)):

			if(frontier[i].visited == False):
				curr = frontier[i]
				frontier[i].visited = True 
				# if the cell we currently visit is not the destination
				if(frontier[i].char != '.'):
					frontier[i].char = '~'
				
				# print "current node explored4"
				# print curr.x
				# print curr.y
				# print "\n"

				if(frontier[i].char != '.'):
					MazeCell[curr.y * width + curr.x].char = '~'
					MazeCell[curr.y * width + curr.x].visited = True
					nodes_expand += 1




				if((curr.x-1 < width) and (curr.x - 1 > 0) and (curr.y < height) and (curr.y > 0) and (check_cell_fontier(MazeCell[curr.y*width + (curr.x-1)]))):
					addcell = MazeCell[curr.y*width + (curr.x-1)]
					addcell.frontier = True
					addcell.cost = curr.cost + 1					
					addcell.distance = Manhatten_distance(addcell, end)
					
					frontier.append(addcell)
					MazeCell[curr.y*width + (curr.x-1)].parent = MazeCell[curr.y*width + curr.x]
					MazeCell[curr.y*width + (curr.x-1)].frontier = True


				if((curr.x+1 < width) and (curr.x + 1 > 0) and (curr.y < height) and (curr.y > 0) and (check_cell_fontier(MazeCell[curr.y*width + (curr.x+1)]))):
					addcell = MazeCell[curr.y*width + (curr.x+1)]
					addcell.frontier = True
					addcell.cost = curr.cost + 1
					
					addcell.distance = Manhatten_distance(addcell, end)
					frontier.append(addcell)
					MazeCell[curr.y*width + (curr.x+1)].parent = MazeCell[curr.y*width + curr.x]
					MazeCell[curr.y*width + (curr.x+1)].frontier = True

				



				

				if((curr.x < width) and (curr.x > 0) and (curr.y +1 < height) and (curr.y+1 > 0) and (check_cell_fontier(MazeCell[(curr.y+1)*width + curr.x]))):
					addcell = MazeCell[(curr.y+1)*width + curr.x]
					addcell.frontier = True
					addcell.cost = curr.cost + 1
					
					addcell.distance = Manhatten_distance(addcell, end)
					frontier.append(addcell)
					MazeCell[(curr.y+1)*width + curr.x].parent = MazeCell[curr.y*width + curr.x]
					MazeCell[(curr.y+1)*width + curr.x].frontier = True

				if((curr.x < width) and (curr.x > 0) and (curr.y-1 < height) and (curr.y-1 > 0) and (check_cell_fontier(MazeCell[(curr.y-1)*width + curr.x]))):
					addcell = MazeCell[(curr.y-1)*width + curr.x]
					addcell.frontier = True
					addcell.cost = curr.cost + 1
					
					addcell.distance = Manhatten_distance(addcell, end)
					frontier.append(addcell)
					MazeCell[(curr.y-1)*width + curr.x].parent = MazeCell[curr.y*width + curr.x]
					MazeCell[(curr.y-1)*width + curr.x].frontier = True

				break
	return nodes_expand


#######################################################################
# already finish the search, denote the path to the destination 
def find_path():

	# x = curr.x
	# y = curr.y
	# curr.path_visited = True

	# if(curr.char == '.'):
		

	curr = MazeCell[end.y*width+end.x]
	while (curr.x != start.x) or (curr.y != start.y):
		curr.char = '.'
		curr = curr.parent


	# if(MazeCell[y*width+x - 1].visited == True and (MazeCell[y*width+x - 1].path_visited == False)):
	# 	left_ret = find_path(MazeCell[y*width+x - 1])
	# else:
	# 	left_ret = False

	# if(MazeCell[(y-1)*width+x].visited == True and (MazeCell[(y-1)*width+x].path_visited == False)):
	# 	down_ret = find_path(MazeCell[(y-1)*width+x])
	# else:
	# 	down_ret = False
	

	# if(MazeCell[y*width+x + 1].visited == True and (MazeCell[y*width+x + 1].path_visited == False)):
	# 	right_ret = find_path(MazeCell[y*width+x + 1])
	# else:
	# 	right_ret = False
	

	# if(MazeCell[(y+1)*width+x].visited == True and (MazeCell[(y+1)*width+x].path_visited == False)):
	# 	up_ret = find_path(MazeCell[(y+1)*width+x])
	# else:
	# 	up_ret = False


	# if(right_ret or left_ret or up_ret or down_ret):
	# 	curr.char = '.'
	# 	return True
	# else:
	# 	return False
		
	



#######################################################################
# check whether a cell is in frontier or not
def check_cell_fontier(curr_cell):
	if(((curr_cell.char == ' ') or (curr_cell.char == '.')) and (curr_cell.frontier == False)):
		return True
	else:
		return False
#######################################################################
# calculate Manhatten_distance between two cells
def Manhatten_distance(cell1, cell2):
	return (abs(cell1.x - cell2.x) + abs(cell1.y - cell2.y))



###########################################################################
####################start executing here
# txt = open("medium_maze.txt")
txt = open("open_maze.txt")
# txt = open("open_maze.txt")
maze = txt.read().splitlines()
MazeCell = []
height = len(maze)
width = len(maze[0])
txt.close()

# find start and end cell
for i in range(0,height):
	for j in range(0,width):
		newCell = cell(maze[i][j], i, j)
		MazeCell.append(newCell)
		if(newCell.char == 'P'):
			start = newCell
		if(newCell.char == '.'):
			end = newCell


# print the original maze
print("\n Original maze: ")
for i in range(0, height):
	print(maze[i])

print end.x
print end.y

# create frontier list, which is also the cells that expanded
# start.visited = true
start.cost = 0
start.distance = Manhatten_distance(start, end)
frontier = [start]
# why??????????????????????????????????????????????????????????
# global path_cost = 0
# path, should replace ' ' by '.' when visited

path_cost = 0
nodes_expanded = A_search()

print "finish A_search"

find_path()

MazeCell[start.y *  width + start.x].char = 'P'
print("\n solution:")
for i in range(0, height):
	cur_row = []
	for j in range(0, width):
		cur_row.append(MazeCell[i * width + j].char)
		if (MazeCell[i * width + j].char == '.'):
			path_cost +=1
	cur_row = ''.join(cur_row)
	print(cur_row)

print("\n path cost:")
print path_cost

print("\n nodes expanded:")
print nodes_expanded











