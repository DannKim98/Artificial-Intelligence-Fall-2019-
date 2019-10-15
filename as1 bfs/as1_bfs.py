#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 
#Points: 2


def traverse(tree, init):    	
	queue = [init]
	traversed = []
	while queue:
		'''
			Student fixes the loopy path from here to the end of this function
		'''
		node = queue.pop(0)
		traversed.append(node)
		leaves = tree[node]
		# leaves.sort() #Alphabetical ordered first, but you sent the massage
		for leaf in leaves:
			if leaf not in traversed and leaf not in queue:
				queue.append(leaf)
	return traversed


#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [init]
	parents = {init: None} #value is a parent of key
	if init == goal:
		return "No kidding, pls"
	while queue:
		'''
			You implement the path finder from here
		'''
		node = queue.pop(0)
		traversed.append(node)
		if node == goal:
			path = [node]
			while True:
				if node == init:
					break
				path.insert(0, parents.get(node))
				node = parents.get(node)
			return path
		leaves = tree[node]
		#leaves.sort() #Alphabetical ordered first, but you sent the massage
		for leaf in leaves:
			if leaf not in traversed and leaf not in queue:
				parents[leaf] = node
				queue.append(leaf)
	return "No such path exists"
 
