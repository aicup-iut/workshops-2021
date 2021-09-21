class Graph(object):
    def __init__(self,adjc_list):
        self.adjc_list = adjc_list
    def get_neighbors(self,v):
        return self.adjc_list[v]
    def h(self,n):
       H = {
            'A': 10,
            'B': 15,
            'C': 5,
            'D': 5,
			'E':10,
			'F':0
        }
       return H[n]
    def a_star_algorithm(self,start,stop):
        
        open_list = set([start])
        close_list = set([])
        
        #present distance from start node to current node
        present_distance = {}
        present_distance[start] = 0
        # parents 
        parents ={}
        parents[start] =start
        while len(open_list)>0:
            n = None
            for v in open_list:
                if n == None or present_distance[v] + self.h(v) <= present_distance[n] + self.h(n):
                    n = v
            if n == None:
                print("Masir vojod nadasht!")
                return None
            if n == stop:
                reconst_path = []
                while  parents[n]!=n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start)
                reconst_path.reverse()
                print("masir peyda shod {}".format(reconst_path))
                return reconst_path
            for (m,weight) in self.get_neighbors(n):
                if m not in open_list and m not in close_list:
                    open_list.add(m)
                    parents[m] = n
                    present_distance[m] = present_distance[n] + weight
                else:
                    if present_distance[m] >= present_distance[n] + weight:
                        present_distance[m] = present_distance[n] + weight
                        parents[m] = n
                        if m in close_list:
                            close_list.remove(m)
                            open_list.add(m)
            open_list.remove(n)
            close_list.add(n)
        print("masir vojod nadasht!")
        return None 
adjac_lis = {
    'A': [('B', 10), ('C', 12), ('D', 5)],
    'B': [('A', 10),('E',11)],
    'C': [('A', 12),('D',6),('E',11),('F',8)],
    'D':[('A',5),('C',6),('F',14)],
    'E':[('B',11),('C',11)],
    'F':[('C',8),('D',14)]
}
graph = Graph(adjac_lis)
graph.a_star_algorithm('A','F')            




