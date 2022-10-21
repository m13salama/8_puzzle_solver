from cmath import sqrt
import heapq
from operator import truediv
from pickle import FALSE, TRUE
import re
import copy
import math
from typing import final

class A_star_search:
    goal_state = [[0,1,2],
                  [3,4,5],
                  [6,7,8]]

    heuristic = ""  
    search_depth = 0 
    number_of_steps=0    
    parent = []      

    def In_frontier(frontier,state):
        for i in range (len(frontier)):
            cost,g,cur_state = frontier[i]
            if(cur_state == state): return TRUE

        return FALSE    


    def get_children(self, state):
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

    def set_heuristic(type):
        if(type != "manhattan" and type != "euclidean"): 
            print("ERROR!")
            exit()
        A_star_search.heuristic = type

    def get_heuristic():
        return A_star_search.heuristic

    def working_heuristic(state):
        res = 0
        if(A_star_search.get_heuristic() == "manhattan"): res = A_star_search.heuristic_manhattan(state)
        elif(A_star_search.get_heuristic() == "euclidean"): res = A_star_search.heuristic_euclidean(state)
        return res

    def heuristic_manhattan(self, state):
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

    def heuristic_euclidean(self, state):    
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

    def get_final_path():
        final_state = []
        cur_state = A_star_search.goal_state
        while(cur_state != 0):
            final_state.insert(0,str(cur_state))
            cur_state = A_star_search.get_parent(cur_state)
        return final_state
            

    def get_parent(state):  
        for i in range(len(A_star_search.parent)):
            s,p = A_star_search.parent[i]
            if(state == s): return p     

    def solve(initial_state):
        
        cost = A_star_search.working_heuristic(initial_state)
        g=0
        frontier = []
        heapq.heappush(frontier,(cost,g,initial_state))
        A_star_search.parent.append((initial_state,0))
        explored = set()

        while(len(frontier) != 0):
            
            cost,g,state = heapq.heappop(frontier)
            print("current state : ",state)
            explored.add(str(state))
            if(state == A_star_search.goal_state):
                return state,len(explored),cost

            g+=1
            if(g > A_star_search.search_depth): A_star_search.search_depth = g
            children = A_star_search.get_children(state) 
            print("children of the current state to into the frontier: ") 
            for i in range (len(children)):
                if((A_star_search.In_frontier(frontier,children[i]) == FALSE) and not(str(children[i]) in explored)):
                    cost = g + A_star_search.working_heuristic(children[i])
                    A_star_search.parent.append((children[i],state))
                    print(children[i], "cost : " , cost)
                    heapq.heappush(frontier,(cost,g,children[i]))


        

    


        

initial_state = [[1,2,5],
                [3,4,0],
                [6,7,8]]              
                
                
A_star_search.set_heuristic("manhattan")
res , number_of_nodes_expanded ,cost = A_star_search.solve(initial_state)
print("number of nodes expanded : ", number_of_nodes_expanded)
print("search depth : ", A_star_search.search_depth)
print("cost : ", cost)
print("final path : ", A_star_search.get_final_path())
