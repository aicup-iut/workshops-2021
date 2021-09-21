from collections import deque
 
class Graph:
    def __init__(self, adjac_lis):
        self.adjac_lis = adjac_lis
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        H = {
            'A': 10,
            'B': 15,
            'C': 5,
            'D': 5,
			'E':10,
			'F':0
        }
 
        return H[n]
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a list of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
        #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # pres_dis has present distances from start to all other nodes
        # the default value is +infinity
        pres_dis = {}
        pres_dis[start] = 0
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or pres_dis[v] + self.h(v) <= pres_dis[n] + self.h(n):
                    n = v
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's par
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    pres_dis[m] = pres_dis[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update par data and poo data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if pres_dis[m] >= pres_dis[n] + weight:
                        pres_dis[m] = pres_dis[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None
adjac_lis = {
    'A': [('B', 10), ('C', 12), ('D', 5)],
    'B': [('A', 10),('E',11)],
    'C': [('A', 12),('D',6),('E',11),('F',8)],
    'D':[('A',5),('C',6),('F',14)],
    'E':[('B',11),('C',11)],
    'F':[('C',8),('D',14)]
}
graph1 = Graph(adjac_lis)
graph1.a_star_algorithm('A', 'F')