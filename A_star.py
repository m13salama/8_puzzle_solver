from cmath import sqrt
import heapq
from operator import truediv
from pickle import FALSE, TRUE
import re
import copy
import math
from typing import final

#this class is used to solve 8 puzzle game with A* method with two heuristic(manhattan - euclidean)
class A_star_search:

    #initialize the global variables and goal state
    def __init__(self):
        
        self.goal_state = [[0,1,2],
                           [3,4,5],
                           [6,7,8]]

        self.heuristic = ""  
        self.depth_of_search_tree = 0 
        self.number_of_expanded_nodes=0    
        self.parent = []
        self.set_heuristic("manhattan")      

    # check if the state is in frontier or not
    def In_frontier(self,frontier,state):
        for i in range (len(frontier)):
            cost,g,cur_state = frontier[i]
            if(cur_state == state): return TRUE

        return FALSE    


    # get all the children of any state
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

    # this function is used to set the heuristic used to solve the A*
    def set_heuristic(self,type):
        if(type != "manhattan" and type != "euclidean"): 
            print("ERROR!")
            exit()
        self.heuristic = type

    # return the current used heuristic 
    def get_heuristic(self):
        return self.heuristic

    # chehck which heuritic is used and get the cost depend on that
    def working_heuristic(self,state):
        res = 0
        if(self.get_heuristic() == "manhattan"): res = self.heuristic_manhattan(state)
        elif(self.get_heuristic() == "euclidean"): res = self.heuristic_euclidean(state)
        return res

    # get the cost of heuristic using manhattan
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

    # get the cost of heuristic using euclidean
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

    # this function is used to get the final path and return array of string
    def get_final_path(self):
        final_state = []
        cur_state = self.goal_state
        while(cur_state != 0):
            final_state.append(str(cur_state))
            cur_state = self.get_parent(cur_state)
        return final_state
            
    # this function is used to get the parent of a state 
    def get_parent(self,state):  
        for i in range(len(self.parent)):
            s,p = self.parent[i]
            if(state == s): return p     

    # this function is used to solve the 8 puzzle game use the given heuristic
    def solve(self,initial_state):
        
        cost = self.working_heuristic(initial_state)
        g=0

        # to store the states
        frontier = []
        heapq.heappush(frontier,(cost,g,initial_state))
        self.parent.append((initial_state,0))

        # store the nodes expanded
        explored = set()

        while(len(frontier) != 0):
            
            # pop the first state in the frontier(the lowest cost)
            cost,g,state = heapq.heappop(frontier)
            explored.add(str(state))

            # check if the current state is the goal state
            if(state == self.goal_state):
                self.number_of_expanded_nodes = len(explored)
                return self.get_final_path()

            g+=1
            if(g > self.depth_of_search_tree): self.depth_of_search_tree = g

            # get all the children of the current state 
            children = self.get_children(state)  

            # check for all child if it's not explored and not in the frontier then add it to the frontier
            for i in range (len(children)):
                if((self.In_frontier(frontier,children[i]) == FALSE) and not(str(children[i]) in explored)):
                    cost = g + self.working_heuristic(children[i])
                    self.parent.append((children[i],state))
                    heapq.heappush(frontier,(cost,g,children[i]))
        
        return []


