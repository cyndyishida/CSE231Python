###################################################
# Instructional  Python file v outline inheritance 
# author: Cyndy Ishida
####################################################

##
# Car base/parent class, no error checking
##
class Car( object ):
    def __init__( self, model, company , name = ""):
        self.__model = model
        self.__name = name
        self.__company = company

    def __repr__(self):
        return "This car is: {} model, and is made um : {}".format(self.__model, self.__company)

    def __str__(self):
        if self.__name != "":
            car_output = "This car was named: {} by it's owner\nIt was made by the company: {}\nIt is an: {} model.\n".format(self.__name,self.__company , self.__model)
        else: 
            car_output = "This car was made by the company: {}\nIt is an: {} model.\n".format(self.__company, self.__model)

        return car_output

##
# Tesla Car, no error checking =
##
class Tesla( Car ):
    def __init__( self, model, voltage , name = "" ):
        Car.__init__(self, model , "Tesla", name)   # REALLY IMPORTANT LINE 
        self.__volt = voltage 
    
    def __str__(self):
        tesla_output = Car.__str__(self)
        tesla_output += "It has {} volt power.".format(self.__volt)
        return tesla_output




##
# Ford car 
##
class Ford( Car ):
    def __init__(self,model, year = 0, name = "" ):
        Car.__init__(self,model, "Ford", name )
        self.__year = year

    
    def __str__(self):
        ford_output = Car.__str__(self)
        if self.__year != 0:
            ford_output += "This car was made in year: {}".format(self.__year)
            if self.__year < 1980:
                ford_output  += "Wow, Whata classic!"

        return ford_output




'''
def dfsTraversal (edges, complete, node):
    if complete[node]:
        return 0
    count = 1
    complete[node] = 1
    for i in range(len(edges[node])):
        count += dfsTraversal(edges, complete, edges[node][i])
    return count






n, m = [int(i) for i in input().split()]


complete = [0 for i in range(n)]

edges = [[] for i in range(n)]


for j in range(m):
    u, v = [int(i) for i in input().split()]
    edges[u].append(v)
    edges[v].append(u)

journey = 0
went_to = 0
for k in range(n):
    if not complete[k]:
        count = dfsTraversal(edges, complete, k)
        journey +=  (went_to * count ) 
        went_to += count



print(journey)
'''












from itemgetter import itemgetter 

class Edge( object ):
    def __init__(self, s, d, w):
        self.s = s
        self.d = d
        self.w = w


class subset(object):
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank





def find ( subsets, i ):
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)

    return subsets[i].parent


def Union(subsets, x , y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)
    if subsets[xroot].rank < subsets[yroot].rank :
        subsets[xroot].paren = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1


def edgeComparison(a, b):
    return a[2] > b[2] 



v, e = [int(i ) for i in input().split()]


edges = []
for k in range(e):
    s, d, w = [int(i ) for i in input().split()]
    edge = (s,d,w)
    edges.append(edges)


edges= sorted(edges , key = itemgetter(2))


mst = [i for i in range(v)]
mstSize = 0


subsets = [] 
for k in range(v):
    parent, rank = [int(i ) for i in input().split()]
    subset = subset(parent, rank)
