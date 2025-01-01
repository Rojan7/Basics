from pprint import pprint
from queue import PriorityQueue
G = {
'biratnagar' : {'itahari' : 22, 'biratchowk' : 30, 'rangeli': 25},
'itahari' : {'biratnagar' : 22, 'dharan' : 20, 'biratchowk' : 11},
'dharan' : {'itahari' : 20},
'biratchowk' : {'biratnagar' : 30, 'itahari' : 11, 'kanepokhari' :10},
'rangeli' : {'biratnagar' : 25, 'kanepokhari' : 25, 'urlabari' : 40},
'kanepokhari' : {'rangeli' : 25, 'biratchowk' : 10, 'urlabari' : 12},
'urlabari' : {'rangeli' : 40, 'kanepokhari' : 12, 'damak' : 6},
'damak' : {'urlabari' : 6}
}
h = {
'biratnagar' : 46,
'itahari' : 39,
'dharan' : 41,
'biratchowk' : 29,
'rangeli' : 28,
'kanepokhari' : 17,
'urlabari' : 6,
'damak' : 0
}
def aStar (G,h,start,goal):
    #initialize a priority queue
    PQ = PriorityQueue()
    #initialize a prev dict
    prev = dict()
    #initialize a visited set
    visited = set()
    #enqueue the initial state into the priority queue
    # we use the format (fscore,(start,gScore))
    PQ.put((0+h[start],(start,0)))
    # we set the prev of start to " "
    prev[start] = ""
    #re[eat until the priority queue is empty
    while (not PQ.empty()):
        #dequeue a state from the priority queue
        outStateFscore,(outState,outStateGscore) = PQ.get() 
        #mark the state as visited
        visited.add(outState)
        #return if the state is the goal state
        if outState == goal:
            return True,prev,outStateFscore
        for chimeki in G[outState]:
            chimekiGscore = outStateGscore + G[outState][chimeki] 
            chimekiFscore = chimekiGscore + h[chimeki]
            if chimeki not in visited:
                PQ.put((chimekiFscore,(chimeki,chimekiGscore)))
                prev[chimeki] = outState
    return False,prev,-1 
def reconstruct_path(G,previous,goal):
    path = goal
    while previous[goal] != "":
        path =previous[goal]+'->'+path
        goal = previous[goal]
    return path
def compute_cost(G,previous,goal):
    cost = 0
    while previous[goal] != "":
        cost += G[previous[goal]][goal]
        goal = previous[goal]
    print(cost)

start = 'biratnagar'
goal = 'damak'
goal_found,previous,fscore = aStar(G,h,start,goal)
if goal_found:
    path = reconstruct_path(G,previous,goal)
    compute_cost(G,previous,goal)
    print(path)
else :
    print("Goal not found")

