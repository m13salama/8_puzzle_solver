from cmath import sqrt
import heapq
from operator import truediv
from pickle import FALSE, TRUE
import re
import copy
import math
from typing import final

class A_star_search:
    def __init__(self):
        
        self.goal_state = [[0,1,2],
                           [3,4,5],
                           [6,7,8]]

        self.heuristic = ""  
        self.depth_of_search_tree = 0 
        self.number_of_expanded_nodes=0    
        self.parent = []
        self.set_heuristic("manhattan")      

    def In_frontier(self,frontier,state):
        for i in range (len(frontier)):
            cost,g,cur_state = frontier[i]
            if(cur_state == state): return TRUE

        return FALSE    


    def get_children(self,state):
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

    def set_heuristic(self,type):
        if(type != "manhattan" and type != "euclidean"): 
            print("ERROR!")
            exit()
        self.heuristic = type

    def get_heuristic(self):
        return self.heuristic

    def working_heuristic(self,state):
        res = 0
        if(self.get_heuristic() == "manhattan"): res = self.heuristic_manhattan(state)
        elif(self.get_heuristic() == "euclidean"): res = self.heuristic_euclidean(state)
        return res

    def heuristic_manhattan(self,state):
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

    def heuristic_euclidean(self,state):    
        res =0
        for i in range(3):
            for j in range(3):
                if(state[i][j] == 0): res += math.sqrt((i-0)**2 + (j-0)**2)
                if(state[i][j] == 1): res += math.sqrt((i-0)**2 + (j-1)**2)
                if(state[i][j] == 2): res += math.sqrt((i-0)**2 + (j-2)**2)
                if(state[i][j] == 3): res += math.sqrt((i-1)**2 + (j-0)**2)
                if(state[i][j] == 4): res += math.sqrt((i-1)**2 + (j-1)**2)
                if(state[i][j] == 5): res += math.sqrt((i-1)**2 + (j-2)**2)
                if(state[i][j] == 6): res += math.sqrt((i-2)**2 + (j-0)**2)
                if(state[i][j] == 7): res += math.sqrt((i-2)**2 + (j-1)**2)
                if(state[i][j] == 8): res += math.sqrt((i-2)**2 + (j-2)**2)
        return res  

    def get_final_path(self):
        final_state = []
        cur_state = self.goal_state
        while(cur_state != 0):
            final_state.append(str(cur_state))
            cur_state = self.get_parent(cur_state)
        return final_state
            

    def get_parent(self,state):  
        for i in range(len(self.parent)):
            s,p = self.parent[i]
            if(state == s): return p     

    def solve(self,initial_state):
        
        cost = self.working_heuristic(initial_state)
        g=0
        frontier = []
        heapq.heappush(frontier,(cost,g,initial_state))
        self.parent.append((initial_state,0))
        explored = set()

        while(len(frontier) != 0):
            
            cost,g,state = heapq.heappop(frontier)
            # print("current state : ",state)
            explored.add(str(state))
            if(state == self.goal_state):
                self.number_of_expanded_nodes = len(explored)
                return self.get_final_path()

            g+=1
            if(g > self.depth_of_search_tree): self.depth_of_search_tree = g
            children = self.get_children(state) 
            # print("children of the current state to into the frontier: ") 
            for i in range (len(children)):
                if((self.In_frontier(frontier,children[i]) == FALSE) and not(str(children[i]) in explored)):
                    cost = g + self.working_heuristic(children[i])
                    self.parent.append((children[i],state))
                    # print(children[i], "cost : " , cost)
                    heapq.heappush(frontier,(cost,g,children[i]))
        
        return []


# initial_state = [[8,7,6],
#                 [2,3,4],
#                 [5,0,1]]              
                
# test = A_star_search()                
# test.set_heuristic("manhattan")
# ss =test.solve(initial_state)
# print("final path : ",ss)
# print("length : " , len(ss))

# print("number of nodes expanded : ", test.number_of_expanded_nodes)
# print("search depth : ", test.depth_of_search_tree)

# print("final path : ", test.get_final_path())
