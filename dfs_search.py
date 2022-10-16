import node_class

# initialState = [[1, 7, 2],
# [4, 0, 5],
# [6, 3, 8]]

# initialState = [[0, 1, 3],
# [4, 2, 5],
# [6, 7, 8]]

# initialState = [[0, 8, 5],
# [2, 1, 3],
# [4, 6, 7]]

class dfs:
    state = []
    def __init__(self, state):
        self.state = state
        # print(self.state)

    def solve(self):
        expanded=[]
        stack = [[self.state]]
        while stack:
            # print(len(expanded))
            path = stack[-1]
            stack.pop(-1)
            node1 = path[-1]
            if node1 in expanded:
                continue
            
            expanded.append(node1)
            
            if node1 == node_class.goal:
                print("done\n")
                return path
            else :
                temp = node_class.node(node1)
                temp.findingChildren()
                for nodes in temp.children:
                        if nodes in expanded:
                            continue
                        if nodes == node_class.goal:
                            print("done\n")
                            path2 = path.copy()
                            path2.append(nodes)
                            return path2
                        path2 = path.copy()
                        path2.append(nodes)
                        stack.append(path2)


## Testing ##

# result = dfs(initialState)
# test = result.solve()
# print(test)
# print(len(test))