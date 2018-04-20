import numpy as numpy
import sys
import copy
from copy import deepcopy

LEFT = 1
RIGHT = 2
UP = 3
DOWN = 4

##############################################
# python couldn't detect wrong attribute name when assigning in a function!
# but it even cares about Chinese in comment when interprete???
##############################################

#############################################
# class defined here
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

class step:
	def __init__(self, inputCell):
		self.node = inputCell
		self.unexplored = []
		self.huristic = None
		self.cost = None
		self.path = []
		self.edge = None


class edge:
	def __init__(self, cell1, cell2):
		self.node1 = cell1
		self.node2 = cell2
		self.cost = 0
		self.path = []
		self.repeat = False


##################################################
# find cost of each edge
def find_cost(cur):

	for i in range(0,len(MazeCell)):
		MazeCell[i].visited = False
		MazeCell[i].frontier = False
		MazeCell[i].cost = 0
		MazeCell[i].distance = 0
		MazeCell[i].path_visited = False
		

	A_ret = A_star_search(cur.node1, cur.node2)

	findpath_ret = find_path(cur.node1, cur.node2, cur)
	# print "A_cost:", A_ret
	# print "findPath ret:", findpath_ret 


###################################################
# A_star_search
def A_star_search(startCell, endCell):
	frontier = []
	startCell.frontier = True
	MazeCell[startCell.y*width + startCell.x].frontier = True 
	frontier.append(startCell)

	while MazeCell[endCell.y*width + endCell.x].visited == False:
		# print "enter A- while loop"


		frontier.sort(key = lambda cell_elements: (cell_elements.cost+cell_elements.distance))
		
		# print"enter A_start-while loop"
		# for i in range(0, len(frontier)):

		# 	print i , "in frontier:"
		# 	print frontier[i].x , " ",frontier[i].y
			
		# 	print frontier[i].visited
				
		if(frontier[0].visited == True):
			print "ERROR - this frontier (",frontier[0].x,",",frontier[0].y,") has already been visited"

		frontier[0].visited = True
		# remove the visited node from frontier list
		
		curr = frontier.pop(0)

		MazeCell[curr.y * width + curr.x].visited = True
		
		# shouldn't need nodex_expanded in this case

		if(within_boundary(curr.x-1, curr.y) and (check_frontier(MazeCell[curr.y*width + (curr.x - 1)]))):
			# print "add to frontier:", curr.x-1," ",curr.y
			# print within_boundary(curr.x, curr.y-1)
			# print check_frontier(MazeCell[(curr.y-1) *width + curr.x])
			# addcell.frontier = True
			MazeCell[curr.y*width + (curr.x-1)].frontier = True
			# addcell.cost = curr.cost + 1

			MazeCell[curr.y*width + (curr.x-1)].cost = curr.cost+1
			MazeCell[curr.y*width + (curr.x-1)].parent = MazeCell[curr.y*width + curr.x]
			addcell = MazeCell[curr.y*width + (curr.x-1)]
			addcell.distance = Manhatten_distance(addcell, endCell)
			frontier.append(addcell)

		if(within_boundary(curr.x+1, curr.y) and (check_frontier(MazeCell[curr.y*width + (curr.x + 1)]))):
			# print "add to frontier:", curr.x+1," ",curr.y
			# addcell.frontier = True
			MazeCell[curr.y*width + (curr.x+1)].frontier = True
			# addcell.cost = curr.cost + 1

			MazeCell[curr.y*width + (curr.x+1)].cost = curr.cost+1
			MazeCell[curr.y*width + (curr.x+1)].parent = MazeCell[curr.y*width + curr.x]
			addcell = MazeCell[curr.y*width + (curr.x+1)]
			addcell.distance = Manhatten_distance(addcell, endCell)
			frontier.append(addcell)


		if(within_boundary(curr.x, curr.y+1) and (check_frontier(MazeCell[(curr.y+1) *width + curr.x]))):
			# print "add to frontier:", curr.x," ",curr.y+1
			# addcell.frontier = True
			MazeCell[(curr.y+1) *width + curr.x].frontier = True
			# addcell.cost = curr.cost + 1

			MazeCell[(curr.y+1)*width + curr.x].cost = curr.cost+1
			MazeCell[(curr.y+1)*width + curr.x].parent = MazeCell[curr.y*width + curr.x]
			addcell = MazeCell[(curr.y+1) *width + curr.x]
			addcell.distance = Manhatten_distance(addcell, endCell)
			frontier.append(addcell)


		if(within_boundary(curr.x, curr.y-1) and (check_frontier(MazeCell[(curr.y-1) *width + curr.x]))):
			# print "add to frontier:", curr.x," ",curr.y-1
			# print within_boundary(curr.x, curr.y-1)
			# print check_frontier(MazeCell[(curr.y-1) *width + curr.x])
			# addcell.frontier = True
			MazeCell[(curr.y-1)*width + curr.x].frontier = True
			# addcell.cost = curr.cost + 1

			MazeCell[(curr.y-1)*width + curr.x].cost = curr.cost+1
			MazeCell[(curr.y-1)*width + curr.x].parent = MazeCell[curr.y*width + curr.x]
			addcell = MazeCell[(curr.y-1)*width + curr.x]
			addcell.distance = Manhatten_distance(addcell, endCell)
			frontier.append(addcell)
		# break

# want to check whether the cost used in A* for the goal is equal to the return value in find_path
	return MazeCell[endCell.y*width + endCell.x].cost


###################################################

def find_path(startCe, endCe, cur_edge):
	curr = MazeCell[endCe.y * width + endCe.x]

	while(startCe.y != curr.y) or (startCe.x != curr.x):
		# print "enter find_path-while loop1"
		if(curr.x == (curr.parent.x -1)) and (curr.y == curr.parent.y):
			cur_edge.path.insert(0, LEFT)

		elif (curr.x == (curr.parent.x +1)) and (curr.y == curr.parent.y):
			cur_edge.path.insert(0, RIGHT)

		elif (curr.x == curr.parent.x ) and (curr.y == curr.parent.y-1):
			cur_edge.path.insert(0, UP)

		elif (curr.x == curr.parent.x) and (curr.y == curr.parent.y +1):
			cur_edge.path.insert(0, DOWN)

		else:
			print "ERROR-couldn't find parent cell"
			break

		cur_edge.cost += 1
		curr = curr.parent
		if(cur_edge.cost != len(cur_edge.path)):
			print "ERROR - the path is not correct"
	return len(cur_edge.path)
		

####################################################
# 
def within_boundary(x, y):
	return ((x < width) and (x >= 0) and (y < height) and (y >= 0))

####################################################
#
def check_frontier(curr_cell):
	return (MazeCell[curr_cell.y*width + curr_cell.x].frontier == False) and (curr_cell.char != '%')

#######################################################################
# calculate Manhatten_distance between two cells
def Manhatten_distance(cell1, cell2):
	return (abs(cell1.x - cell2.x) + abs(cell1.y - cell2.y))

########################################################################
# in case the variable is not hashable
# self-define a function to compare two goals
def same(cell1, cell2, disjoint_dict):
	root1 = root(cell1, disjoint_dict)
	root2 = root(cell2, disjoint_dict)
	return (root1.x == root2.x) and (root1.y == root2.y)

##########################################################################
# 
def root(cell, disjoint_dict):
	if disjoint_dict[cell] == cell:
		return cell
	else:
		return root(disjoint_dict[cell], disjoint_dict)

##########################################################################
#
def draw_dots(curr_edge, ascii_code):
	curr = curr_edge.node1
	for i in range(0, len(curr_edge.path)-1):
		if(curr_edge.path[i] == UP) :
			if (MazeCell[(curr.y-1)*width + curr.x].char == " "):
				MazeCell[(curr.y-1)*width + curr.x].char = "."
			curr = MazeCell[(curr.y-1)*width + curr.x]
		elif (curr_edge.path[i] == DOWN) :
			if (MazeCell[(curr.y+1)*width + curr.x].char == " "):
				MazeCell[(curr.y+1)*width + curr.x].char = "."
			curr = MazeCell[(curr.y+1)*width + curr.x]
		elif(curr_edge.path[i] == LEFT) :
			if (MazeCell[curr.y*width + curr.x-1].char == " "):
				MazeCell[curr.y*width + curr.x-1].char = "."
			curr = MazeCell[curr.y*width + curr.x-1]
		elif(curr_edge.path[i] == RIGHT) :
			if (MazeCell[curr.y*width + curr.x+1].char == " "):
				MazeCell[curr.y*width + curr.x+1].char = "."
			curr = MazeCell[curr.y*width + curr.x+1]
	MazeCell[curr_edge.node2.y * width + curr_edge.node2.x].char = chr(ascii_code)
#####################################################
#
def form_mst(sub_unexplored):
	disjoint = {elem : elem for elem in sub_unexplored}
	sub_mst = []
	sub_edges = []
	mst_cost = 0
	for i in range(0, len(sub_unexplored)):
		for j in range(i+1, len(sub_unexplored)):
			# print "checking the ", i, j
			# print "the coordinates are: (" , goals[i].x,",", goals[i].y, ") (",goals[j].x ,",",goals[j].y, ")"
			temp_edge = edge(sub_unexplored[i], sub_unexplored[j])
			find_cost(temp_edge)
			sub_edges.append(temp_edge)

	sub_edges.sort(key = lambda elem: elem.cost)
# print (disjoint[edges[1].node1] == disjoint[edges[2].node2])
	for i in range(0, len(sub_edges)):
		if (same(sub_edges[i].node1, sub_edges[i].node2, disjoint) != True):
			
			disjoint[root(sub_edges[i].node2, disjoint)] = root(sub_edges[i].node1, disjoint)
			
			sub_mst.append(sub_edges[i])
	# for i in range(0,len(sub_mst)):
	# 	print "this is ", i , "in sub_edges", "cordinate ", sub_edges.node1.x, " ", sub_edges.node1.y
	for i in range(0, len(sub_mst)):
		mst_cost += sub_mst[i].cost
	return mst_cost

def check_repeat_node(corX, corY, node_list):
	for elem in node_list:
		if (corX == elem.x) and (corY == elem.y):
			return True
	return False


#####################################################
#
nodes_expand = 0
def traverse():
	nodes_expand = 0
	start_step = step(start)
	node_explored = []

	start_step.unexplored = goals
	start_step.cost = 0;
	start_step.path = []
	start_step.huristic = form_mst(start_step.unexplored)
	print "289: the mst of the whole is:", start_step.huristic
	Priority_Q.append(start_step)
	# Priority_Q.sort(key = lambda elem: elem.cost+elem.huristic)

	while (len(Priority_Q[0].unexplored) > 1) :
		parent_step = Priority_Q.pop(0)

		exploring = parent_step.unexplored
		# if(parent_step.node != start):
		# 	final_path.append(parent_step.edge)
		print "297: the parent node is", parent_step.node.x, " ", parent_step.node.y

		for j in range(0, len(exploring)):
			cur_step = None
			if(exploring[j].x != parent_step.node.x)or(exploring[j].y != parent_step.node.y):
				# print "300 checking the children node:", exploring[j].x, " ", exploring[j].y
				cur_step = step(exploring[j])
				# cur_step.unexplored = exploring
	
				for t in range(0, len(exploring)):
					if(exploring[t].x != parent_step.node.x) or (exploring[t].y != parent_step.node.y):

						cur_step.unexplored.append(exploring[t])
		
				cur_step.edge = edge(parent_step.node, cur_step.node)
				find_cost(cur_step.edge)
				cur_step.cost = parent_step.cost+cur_step.edge.cost
				cur_step.huristic = form_mst(cur_step.unexplored)

				for i in range(0, len(parent_step.path)):
					cur_step.path.append(parent_step.path[i])
				
				if parent_step.edge:
					cur_step.path.append(parent_step.edge)

				Priority_Q.append(cur_step)
				nodes_expand += len(cur_step.path)
		Priority_Q.sort(key = lambda elem: elem.cost+elem.huristic)
	last = Priority_Q.pop(0)
	# for i in range(0, len(last.path)):

	# 	final_path[i] = last.path[i]

	for i in range(0, len(last.path)):
		final_path.append(last.path[i])
	print "nodes_expand:", nodes_expand
	return last.cost



####################################################
# main function
txt = open("tiny.txt")
maze = txt.read().splitlines()
MazeCell = []
height = len(maze)
width = len(maze[0])
txt.close()

global start
goals = []
# find the start cell and all the goals
for i in range(0,height):
	for j in range(0,width):
		newCell = cell(maze[i][j], i, j)
		MazeCell.append(newCell)
		if(newCell.char == 'P'):
			start = newCell
		if(newCell.char == '.' or newCell.char == 'P'):
			goals.append(newCell)

# print the original maze
print("\n Original maze: ")
for i in range(0, height):
	print(maze[i])

for i in range(0, len(goals)):
	print "the", i, " th coordinates is:", goals[i].x," " ,goals[i].y


#########################################
global final_path
final_path = []
Priority_Q = []
node_sequence = []

total_cost = traverse()






# print"371:", len(final_path)
# for i in range(0, len(final_path)):

# 	print "node1:", final_path[i].node1.x, " ", final_path[i].node1.y
# 	print "node2:", final_path[i].node2.x, " ", final_path[i].node2.y
# 	print " "





###########################################################
# total cost
ascii = 48

print "total cost is:" , total_cost
# print the path
for i in range(0,len(final_path)):
	draw_dots(final_path[i], ascii)
	ascii += 1
	if(ascii == 58):
		ascii += 7

print("\n solution:")
for i in range(0, height):
	cur_row = []
	for j in range(0, width):
		cur_row.append(MazeCell[i * width + j].char)
	cur_row = ''.join(cur_row)
	print(cur_row)












