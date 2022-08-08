graph = {
    "S": {"A": 2, "B": 1,"G": 9},
    "A": {"C": 2, "D": 3},
    "B": {"D": 2, "E": 4},
    "C": {"G": 4},
    "D": {"G": 4},
    "E": {},
    "G": {}
}

heuristicSLD={
    "S": 6,
    "A": 0,
    "B": 6,
    "C": 4,
    "D": 1,
    "E": 10,
    "G": 0  
    }

class graphProblem:

    def __init__(self,initial,goal,graph):
        self.initial=initial
        self.goal=goal
        self.graph=graph

    def actions(self,state):
        return list(self.graph[state].keys())

    def result(self,state,action):
        return action

    def goal_test(self,state):
        return state == self.goal

    def path_cost(self,cost_so_far,state1,action,state2):
        return cost_so_far + self.graph[state1][state2]
        

class Node:
    def __init__(self,state,parent=None,action=None,path_cost=0,count=0):
        self.state=state
        self.parent=parent
        self.action=action
        self.path_cost=path_cost
        self.count=count

    def expand(self,graphProblem):
        return [self.child_node(graphProblem,action)
                for action in graphProblem.actions(self.state)]
        

    def child_node(self,graphProblem,action):
        next_state=graphProblem.result(self.state,action)        
        return Node(next_state,self,action,
                    graphProblem.path_cost(self.path_cost,self.state,action,next_state))

    def path(self):        
        node, path_back = self, []       
        
        while node:            
            path_back.append(node)            
            node = node.parent
            self.count=self.count+1
        
        return list(reversed(path_back))

    def solution(self):        
        return [node.action for node in self.path()[1:]]

gp=graphProblem("S","G",graph)
def best_first_search(gp,f):
    node=Node(gp.initial)
    frontier=[]
    explored=set()
    child=list()
    frontier.append(node)
    while frontier:
        if len(frontier)==0:  return "Failure"
        city=frontier.pop(0)
    #    print("Current city : "+city.state)
        if(gp.goal_test(city.state)): 
            return city 
        else: 
            explored.add(city.state)
        #    print(explored)
            child=city.expand(gp)
            for i in child:
                if i.state not in explored and child not in frontier:
                    frontier.append(i)
                    frontier.sort(key=f)
        #    for i in frontier:
        #        print(i.state)

def gbfs(gp,f):return best_first_search(gp,f)
gbfsresult=gbfs(gp,f=lambda node:heuristicSLD[node.state])
print("gbfs Path :",gbfsresult.solution(),"path cost:",gbfsresult.path_cost)
print()
def astar(gp,f):return best_first_search(gp,f)
astarresult=astar(gp,f=lambda node:(node.path_cost+heuristicSLD[node.state]))
print("astar Path :",astarresult.solution(),"path cost:",astarresult.path_cost)
print()
#print(astarresult.count)
#print(gbfsresult.count)

if(gbfsresult.count<astarresult.count):
   print("gbfs search cost is minimal")

if(gbfsresult.path_cost>astarresult.path_cost):
   print("gbfs is not optimal")
print()
def ucs(gp,f):return best_first_search(gp,f)
ucsresult=ucs(gp,f=lambda node:node.path_cost)
print("ucs path :",ucsresult.solution(),"path cost:",ucsresult.path_cost)

