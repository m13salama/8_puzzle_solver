from fileinput import close
import node

# initialState = [[1, 7, 2],
# [4, 0, 5],
# [6, 3, 8]]

# initialState = [[8, 6, 7],
# [2, 5, 4],
# [3, 0, 1]]

# initialState = [[6, 4, 7],
# [8, 5, 0],
# [3, 2, 1]]

# initialState = [[0, 1, 3],
# [4, 2, 5],
# [6, 7, 8]]

# initialState = [[0, 8, 5],
# [2, 1, 3],
# [4, 6, 7]]

class bfs:
    number_of_expanded_nodes = 0
    state = []
    def __init__(self, state):
        self.state = str(state)
        # print(self.state)

    def get_path(self,parent,goal):
        father_node = parent[goal]
        path = [goal]
        while father_node != self.state:
            path.append(father_node)
            father_node = parent[father_node]
        path.append(father_node)
        return path
    
    def write_path_file(self,path):
        worker_file = open("bfs_path.txt","w")
        for i in range(len(path)):
            temp = path.pop()
            worker_file.write(f'{i+1} {temp} \n')
        worker_file.close()
    
    def solve(self):
        expanded={''}
        frontier = {self.state}
        queue = [self.state]
        parentMap = {self.state:self.state}
        while queue:
            # print(len(expanded))
            node1 = queue.pop(0)
            frontier.remove(node1)
            if node1 in expanded:
                continue
            expanded.add(node1)
            
            if node1 == str(node.goal):
                print("done\n")
                self.number_of_expanded_nodes = len(expanded)
                path = self.get_path(parentMap,str(node.goal))
                written_path = path.copy()
                self.write_path_file(written_path)
                return path
            else :
                temp = node.node()
                temp.findingChildren(temp.strTO2dArray(node1))
                for nodes in temp.children:
                    if not(nodes in expanded) and not(nodes in frontier):
                        queue.append(nodes)
                        frontier.add(nodes)
                        parentMap[nodes] = node1

## Testing ##

# result = bfs(str(initialState))
# test = result.solve()
# length_ = len(test)
# for i in range(len(test)):
#     print(test.pop())
# print(length_)