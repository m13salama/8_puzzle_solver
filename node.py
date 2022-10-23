import copy
from itertools import chain

goal = [[0,1,2],[3,4,5],[6,7,8]]

class node:
    #list that saves the children of given state
    children = []
    #The intial state
    state = []
    
    # function that takes 2d array and validate it  
    def ValidateInput(self,intial):
        for i in range(3):
            for j in range(3):
                try:
                    intial[i][j] = int(intial[i][j])
                except:
                    return False
                

        set = {intial[0][0]}
        for i in range(3):
            for j in range(3):
                if intial[i][j] >= 0 and intial[i][j] <= 8:
                    set.add(intial[i][j])
                else:
                    return False
        
        if len(set) == 9:
            return intial
        else:
            return False
        
    #function that convert string to 2d array to facilitate the calculation on it
    def strTO2dArray(self,str):
        array =[]
        str = str.replace("["," ")
        str = str.replace("]"," ")
        str = str.replace(" ","")
        str = str.split(",")
        str = self.to_matrix(str)
        array = [list( map(int,i) ) for i in str]
        return array

    def to_matrix(self,l):
      return [l[i:i+3] for i in range(0, len(l), 3)]
   
    # function that takes the intial array and return true if it can be solved and return false if it can't be true
    def isSolvable(self,state):
        counter = 0
        array = [9]
        array = list(chain.from_iterable(state))
        for i in range(9):
             for j in range(i+1,9):
                 if array[i] > 0 and array[j] > 0 and array[i] > array[j]:
                     counter += 1
        
        if counter%2 == 1:
            return False
        else :
            return True


    # function that takes any state and return list of its children 
    def findingChildren(self,state):
        row = 0
        col = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    row = i
                    col = j

        self.children.clear()

         # move up
        if row != 2:
            child = copy.deepcopy(state)
            temp = child[row + 1][col]
            child[row + 1][col] = child[row][col]
            child[row][col] = temp
            child = str(child)
            self.children.append(child)

        # move down
        if row != 0:
            child = copy.deepcopy(state)
            temp = child[row - 1][col]
            child[row - 1][col] = child[row][col]
            child[row][col] = temp
            child = str(child)
            self.children.append(child)

        # move right
        if col != 0:
            child = copy.deepcopy(state)
            temp = child[row][col - 1]
            child[row][col - 1] = child[row][col]
            child[row][col] = temp
            child = str(child)
            self.children.append(child)
            

        # move left
        if col != 2:
            child = copy.deepcopy(state)
            temp = child[row][col + 1]
            child[row][col + 1] = child[row][col]
            child[row][col] = temp
            child = str(child)
            self.children.append(child)

