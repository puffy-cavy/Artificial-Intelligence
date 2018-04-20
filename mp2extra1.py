from copy import deepcopy
import random

table = {'AB':1064, 'AC':673, 'AD':1401, 'AE':277, 'BA':1064, 'BC':958, 'BD':1934, 'BE':337, 'CA':673, 'CB':958, 'CD':1001, 'CE':399, 'DA':1401, 'DB':1934, 'DC':1001, 'DE':387, 'EA':277, 'EB':337, 'EC':399, 'ED':387}
alphabet_lst = ['A','B','C','D','E']
# widgets_finish = 0
q1 = []
q2 = []
shortest_table = dict.fromkeys(['AB','AC','AD','AE','BA','BC','BD','BE','CA','CB','CD','CE','DA','DB','DC','DE','EA','EB','EC','ED'])

class step:
	def __init__(self, stop):
		self.stop = stop
		self.cost = 0
		self.h = 0
		self.path = ''
		self.component_left = None

class Ucs_element:
	def __init__(self, node1, node2, cost):
		self.node1 = node1
		self.node2 = node2
		self.cost = cost
		self.path = ''

class shortest_value:
	def __init__(self,path,cost):
		self.path = path
		self.cost = cost



def min_stop_A():
	print"min_stop A* search"
	# check the utility of each stop
	# for i in range(5):
	# 	cur_stop = alphabet_lst[i]
	# 	cur_step = step(cur_stop)
	# 	cur_step.component_left = deepcopy(widgets)
	# 	# the flag will turn to 0 when there is at least one component finish in that stop
	# 	cur_step.cost = 1
	# 	# traverse the 5 widgets
	# 	for i in range(5):
	# 		if(cur_step.component_left[i][0] == cur_stop):
	# 			cur_step.component_left[i] = cur_step.component_left[i][1:]

	# 	cur_step.h = max([len(x) for x in cur_step.component_left])
	# 	cur_step.path += cur_stop
	# 	# push the current step in the priority q1
	# 	q1.append(cur_step)
	# # rearrange the priority queue
	# q1.sort(key = lambda elements: (elements.cost+elements.h))
	total_stops_expanded1 = 0
	for i in range(5):

		cur_stop = alphabet_lst[i]
		cur_step = step(cur_stop)
		cur_step.component_left = deepcopy(widgets)
		for k in range(5):
			if(cur_step.component_left[k][0] == cur_stop):
				cur_step.component_left[k] = cur_step.component_left[k][1:]
		cur_step.cost = 1
		cur_step.h = max([len(x) for x in cur_step.component_left])
		cur_step.path += cur_stop
		q1.append(cur_step)
		total_stops_expanded1 += 1
	counter = 0
	while (q1[0].component_left[0]!='' or q1[0].component_left[1]!='' or q1[0].component_left[2]!='' or q1[0].component_left[3]!='' or q1[0].component_left[4]!=''):
		parent_step = q1.pop(0)
		counter += 1
		for i in range(5):
			cur_stop = alphabet_lst[i]

			if(cur_stop != parent_step.stop):
				# the next stop should shown at the initial of the widget
				freq_lst = [0,0,0,0,0]
				for j in range(5):
					if (len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'A'):
						freq_lst[0] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'B'):
						freq_lst[1] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'C'):
						freq_lst[2] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'D'):
						freq_lst[3] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'E'):
						freq_lst[4] += 1

				if(freq_lst[i] != 0):

					cur_step = step(cur_stop)
					cur_step.component_left = deepcopy(parent_step.component_left)
					cur_step.cost = cur_step.cost = parent_step.cost+1

					for k in range(5):
						if(len(cur_step.component_left[k]) and cur_step.component_left[k][0] == cur_stop):
							cur_step.component_left[k] = cur_step.component_left[k][1:]

					cur_step.h = len(set(cur_step.component_left[0])|set(cur_step.component_left[1])|set(cur_step.component_left[2])|set(cur_step.component_left[3])|set(cur_step.component_left[4]))
					cur_step.path = parent_step.path + cur_stop

					# push the current step in the priority q1
					q1.insert(0,cur_step)
					total_stops_expanded1 += 1
					#print"105",total_stops_expanded
		q1.sort(key = lambda elements: (elements.cost+elements.h))
		if(counter % 1000 == 0):
			print "counter:", counter
			print cur_step.path
			print cur_step.component_left
	solution_step = q1.pop(0)
	print "\n"
	print "the path solution is:",solution_step.path
	print "the length of the path is:",len(solution_step.path)
	print "total stops expaneded is:", total_stops_expanded1
	return None


def ucs(start, end):
	ucs_q = []
	for i in range(5):
		cur_stop = alphabet_lst[i]
		if(cur_stop != start):
			cur_elem = Ucs_element(start, cur_stop, table[start+cur_stop])
			cur_elem.path = start+cur_stop
			ucs_q.append(cur_elem)

	ucs_q.sort(key = lambda x: x.cost)
	while(ucs_q[0].node2!= end):
		parent_elem = ucs_q.pop(0)
		for i in range(5):
			cur_stop = alphabet_lst[i]
			if(parent_elem.path.find(cur_stop)== -1):
				cur_elem = Ucs_element(start,cur_stop,parent_elem.cost+table[parent_elem.node2+cur_stop])
				cur_elem.path = parent_elem.path+cur_stop
				ucs_q.append(cur_elem)
		ucs_q.sort(key = lambda x: x.cost)
	#print "solution path from ucs:",ucs_q[0].path
	cur_table_value = shortest_value(ucs_q[0].path, ucs_q[0].cost)
	shortest_table[start+end] = cur_table_value



def min_distance_A():
	print "\n"
	print"min_distance A* search"
	stops_expanded = 0
	explored_path = []
	# check the utility of each stop
	for i in range(5):
		cur_stop = alphabet_lst[i]
		cur_step = step(cur_stop)
		cur_step.component_left = deepcopy(widgets)
		# the flag will turn to 0 when there is at least one component finish in that stop
		cur_step.cost = 0
		# traverse the 5 widgets
		for j in range(5):
			if(cur_step.component_left[j][0] == cur_stop):
				cur_step.component_left[j] = cur_step.component_left[j][1:]

		# longest_left = max([(len(x),x) for x in cur_step.component_left])[1]
		#print longest_left
		h_list = [0,0,0,0,0]
		for p in range(5):
			for k in range(len(cur_step.component_left[p])):
				if(k == 0):
					dic_key = cur_stop + cur_step.component_left[p][k]
				else:
					dic_key = cur_step.component_left[p][k-1]+cur_step.component_left[p][k]
				h_list[p] += shortest_table[dic_key].cost
		cur_step.h  = max(h_list)

		cur_step.path += cur_stop
		# push the current step in the priority q2
		q2.append(cur_step)
	# rearrange the priority queue
	q2.sort(key = lambda elements: (elements.cost+elements.h))
	counter = 0
	parent_step = q2.pop(0)
	explored_path.append(parent_step.path)
	while (parent_step.component_left[0]!='' or parent_step.component_left[1]!='' or parent_step.component_left[2]!='' or parent_step.component_left[3]!='' or parent_step.component_left[4]!=''):
		# parent_step = q2.pop(0)
		counter += 1
		# traverse the 5 stops
		for i in range(5):
			cur_stop = alphabet_lst[i]

			# the consecutive stops shouldn't be the same
			if(cur_stop != parent_step.stop):
				# the next stop should shown at the initial of the widget
				freq_lst = [0,0,0,0,0]
				for j in range(5):
					if (len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'A'):
						freq_lst[0] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'B'):
						freq_lst[1] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'C'):
						freq_lst[2] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'D'):
						freq_lst[3] += 1
					elif(len(parent_step.component_left[j]) and parent_step.component_left[j][0] == 'E'):
						freq_lst[4] += 1

				if(freq_lst[i] != 0):
					cur_step = step(cur_stop)
					cur_step.component_left = deepcopy(parent_step.component_left)

					cur_table_key = parent_step.stop + cur_stop
					cur_table_path = shortest_table[cur_table_key].path
					cur_table_cost = shortest_table[cur_table_key].cost
					cur_step.cost = parent_step.cost + cur_table_cost

					# slice the component_left list
					for t in range(1,len(cur_table_path)):
						for k in range(5):
							if(len(cur_step.component_left[k]) and cur_step.component_left[k][0] == cur_table_path[t]):
								cur_step.component_left[k] = cur_step.component_left[k][1:]
					# h
					# longest_left = max([(len(x),x) for x in cur_step.component_left])[1]
					h_list = [0,0,0,0,0]
					for p in range(5):
						for k in range(len(cur_step.component_left[p])):
							if(k == 0):
								dic_key = cur_stop + cur_step.component_left[p][k]
							else:
								dic_key = cur_step.component_left[p][k-1]+cur_step.component_left[p][k]
							h_list[p] += shortest_table[dic_key].cost
					cur_step.h  = max(h_list)

					# path
					cur_step.path = parent_step.path + cur_table_path[1:]

			# push the current step in the priority q2
			q2.insert(0,cur_step)
			#q2.append(cur_step)
			stops_expanded += 1
		# q1.sort(key = lambda elements: (elements.cost+elements.h))
		parent_step = min(q2, key = lambda x:(x.cost+x.h))
		q2.remove(parent_step)
		# print "explored_path.index(parent_step.path)",explored_path.index(parent_step.path)
		while((parent_step.path in explored_path) == True):
			parent_step = min(q2, key = lambda x:(x.cost+x.h))
			q2.remove(parent_step)
		explored_path.append(parent_step.path)
		# print"233:", parent_step.cost
		# print"234:", parent_step.path

		if(counter % 1000 == 0):
			print counter,"th, calculation:"
			print "current path explored;",parent_step.path
			print "component unfinished:",parent_step.component_left
			print "current step cost:",parent_step.cost
			print "estimate total cost:",parent_step.cost + parent_step.h
	solution_step = parent_step
	print "\n"
	print "solution path:",solution_step.path
	print "the length of the path is:", len(solution_step.path)
	print "total distance:",solution_step.cost
	print "total stops expaneded: ", stops_expanded
	# print "empty widgets left:",solution_step.component_left
	return None



#################################
# unit test: q1 initialization
# min_stop_A()
# for i in range(len(q1)):
# 	print q1[i].cost

#################################
ucs('A','B')

for i in range(5):
	for j in range(5):
		if(i!=j):
			start = alphabet_lst[i]
			end = alphabet_lst[j]
			ucs(start,end)

# min_distance_A()
# min_stop_A()

################################
# extra
widgets = ['','','','','']
def widget_generator(length):
    for i in range(5):
        while(len(widgets[i]) < length):
            new_stop = random.choice('ABCDE')
            if(len(widgets[i]) == 0):
                widgets[i]+= new_stop
            elif( new_stop != widgets[i][-1]):
                widgets[i]+= new_stop

widget_generator(5)
print widgets
# min_distance_A()
min_stop_A()
min_distance_A()
