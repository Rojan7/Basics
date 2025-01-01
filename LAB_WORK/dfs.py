import pprint
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
def DFS(G,start,goal):
    #initialize a stack
    stack = list()
    #initialize a dictionary to reconstruct the path
    prev = dict()
    #initialize a set to keep track of visited vertices
    visited = set()
    #push the starting state into the stack
    stack.append(start)
    #set the previous state to ""
    prev[start]=""
    #repeat until the stack is not empty
    while(stack):
        #pop a state from the stack
        popped_state = stack.pop()
        #mark the popped state as visited
        visited.add(popped_state)
        #return if the popped state is the goal state
        if popped_state == goal:
            return True,prev
        #push all the chimekis of popped state if they
        #are not already in the stack and if they are not already visited
        for chimeki in G[popped_state]:
            if chimeki not in stack and chimeki not in visited:
                stack.append(chimeki)
                prev[chimeki] = popped_state #this is for reconstructing the path
    return False,prev

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
goal_found,previous = DFS(G,start,goal)
compute_cost(G,previous,goal)  
if goal_found:
    path = reconstruct_path(G,previous,goal)
    print(path)
else :
    print("Goal not found")
