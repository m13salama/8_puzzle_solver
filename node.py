import copy
class node:
    children = []
    state = []

    def __init__(self, state):
        self.state = state

  def isSolvable(self):
        counter = 0
        array = [9]
        array = list(chain.from_iterable(self.state))
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


    def findingChildren(self):
        row = 0
        col = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    row = i
                    col = j

        self.children.clear()

         # move up
        if row != 2:
            child = copy.deepcopy(self.state)
            temp = child[row + 1][col]
            child[row + 1][col] = child[row][col]
            child[row][col] = temp
            n = node(child)
            n.parent = self
            self.children.append(child)

        # move down
        if row != 0:
            child = copy.deepcopy(self.state)
            temp = child[row - 1][col]
            child[row - 1][col] = child[row][col]
            child[row][col] = temp
            # print(child)
            n = node(child)
            n.parent = self
            self.children.append(child)

        # move right
        if col != 0:
            child = copy.deepcopy(self.state)
            temp = child[row][col - 1]
            child[row][col - 1] = child[row][col]
            child[row][col] = temp
            n = node(child)
            n.parent = self
            self.children.append(child)
            

        # move left
        if col != 2:
            child = copy.deepcopy(self.state)
            child = copy.deepcopy(self.state)
            temp = child[row][col + 1]
            child[row][col + 1] = child[row][col]
            child[row][col] = temp
            n = node(child)
            n.parent = self
            self.children.append(child)
