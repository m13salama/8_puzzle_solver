import copy
class node:
    children = []
    state = []


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
   

    def isSolvable(self,state):
        counter = 0
        array = [9]
        array = list(chain.from_iterable(state))
        print(array)
        for i in range(9):
             for j in range(i+1,9):
                 if array[i] > 0 and array[j] > 0 and array[i] > array[j]:
                     counter += 1
        
        print(counter)
        if counter%2 == 1:
            return False
        else :
            return True


   
    def findingChildren(self,state):
        row = 0
        col = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    row = i
                    col = j

        self.children.clear()
        # print(row,col)

         # move up
        if row != 2:
            child = copy.deepcopy(state)
            temp = child[row + 1][col]
            child[row + 1][col] = child[row][col]
            child[row][col] = temp
            child = str(child)
            print(child)
            self.children.append(child)

        # move down
        if row != 0:
            child = copy.deepcopy(state)
            temp = child[row - 1][col]
            child[row - 1][col] = child[row][col]
            child[row][col] = temp
            child = str(child)
            print(child)
            self.children.append(child)

        # move right
        if col != 0:
            child = copy.deepcopy(state)
            temp = child[row][col - 1]
            child[row][col - 1] = child[row][col]
            child[row][col] = temp
            child = str(child)
            print(child)
            self.children.append(child)
            

        # move left
        if col != 2:
            child = copy.deepcopy(state)
            temp = child[row][col + 1]
            child[row][col + 1] = child[row][col]
            child[row][col] = temp
            child = str(child)
            print(child)
            self.children.append(child)

