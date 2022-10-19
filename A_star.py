from asyncio.windows_events import NULL
import heapq
from operator import truediv
from pickle import FALSE, TRUE
import re
import copy

def A_star_search(initial_state,goal_state):
    
    cost = heuristic_manhattan(initial_state,goal_state)
    frontier = []
    heapq.heappush(frontier,(cost,initial_state))
    explored = set()

    while(len(frontier) != 0):
    
        cost,state = heapq.heappop(frontier)
        print(cost,state)
        explored.add(str(state))
        if(state == goal_state):
            return state

        g = cost - heuristic_manhattan(state,goal_state)
        g+=1
        children = get_children(state) 
        print(children) 
        for i in range (len(children)):
            if((In_frontier(frontier,children[i]) == FALSE) and not(str(children[i]) in explored)):
                cost = g + heuristic_manhattan(children[i],goal_state)
                heapq.heappush(frontier,(cost,children[i]))

            


    return NULL 

def In_frontier(frontier,state):
    for i in range (len(frontier)):
        cost,cur_state = frontier[i]
        if(cur_state == state): return TRUE

    return FALSE    


def get_children(state):
    temp_state = copy.deepcopy(state)
    res = []
    for i in range(3):
        for j in range(3):
            if(state[i][j] == 0):
                if(i-1 >=0): 
                    temp = temp_state[i-1][j]
                    temp_state[i-1][j] = 0
                    temp_state[i][j] = temp
                    res.append(temp_state)
                    temp_state = copy.deepcopy(state)

                if(i+1 < 3): 
                    temp = temp_state[i+1][j]
                    temp_state[i+1][j] = 0
                    temp_state[i][j] = temp
                    res.append(temp_state)
                    temp_state = copy.deepcopy(state)

                if(j-1 >=0): 
                    temp = temp_state[i][j-1]
                    temp_state[i][j-1] = 0
                    temp_state[i][j] = temp
                    res.append(temp_state)
                    temp_state = copy.deepcopy(state)    

                if(j+1 < 3): 
                    temp = temp_state[i][j+1]
                    temp_state[i][j+1] = 0
                    temp_state[i][j] = temp
                    res.append(temp_state)
                    temp_state = copy.deepcopy(state)

                return res       

def heuristic_manhattan(state,goal_state):
    res =0
    for i in range(3):
        for j in range(3):
            if(state[i][j] == 0): res += (i-0) + (j-0)
            if(state[i][j] == 1): res += (i-0) + abs(j-1)
            if(state[i][j] == 2): res += (i-0) + abs(j-2)
            if(state[i][j] == 3): res += abs(i-1) + (j-0)
            if(state[i][j] == 4): res += abs(i-1) + abs(j-1)
            if(state[i][j] == 5): res += abs(i-1) + abs(j-2)
            if(state[i][j] == 6): res += abs(i-2) + (j-0)
            if(state[i][j] == 7): res += abs(i-2) + abs(j-1)
            if(state[i][j] == 8): res += abs(i-2) + abs(j-2)
    return res


       

initial_state = [[1,2,5],
                 [3,4,0],
                 [6,7,8]]              
                 
                 
goal_state = [[0,1,2],
              [3,4,5],
              [6,7,8]]



# print(heuristic_manhattan(initial_state,goal_state))
print(A_star_search(initial_state,goal_state))

# A_star_search(initial_state,goal_state)