from fileinput import close
import node

class bfs:
    number_of_expanded_nodes = 0
    depth_of_search_tree = 0
    state = []

    def get_path(self,parent,goal):
        if(self.state == goal):
            return []
        
        father_node = parent[goal]
        path = [goal]
        while father_node != self.state:
            path.append(father_node)
            father_node = parent[father_node]
        path.append(father_node)
        return path
    
    def write_path_file(self,path):
        worker_file = open("asserts/bfs_path.txt","w")
        for i in range(len(path)):
            temp = path.pop()
            worker_file.write(f'{i+1} {temp} \n')
        worker_file.close()
    
    def solve(self,state):
        self.state = str(state)
        expanded={''}
        frontier = {self.state}
        queue = [[self.state,0]]
        parentMap = {self.state:self.state}
        while queue:
            # print(len(expanded))
            temp_depth = queue.pop(0)
            node1 = temp_depth[0]
            depth = temp_depth[1]
            frontier.remove(node1)
            if node1 in expanded:
                continue
            
            if node1 == str(node.goal):
                print("done\n")
                self.number_of_expanded_nodes = len(expanded)-1
                self.depth_of_search_tree = depth
                path = self.get_path(parentMap,str(node.goal))
                written_path = path.copy()
                self.write_path_file(written_path)
                return path

            expanded.add(node1)
            temp = node.node()
            temp.findingChildren(temp.strTO2dArray(node1))
            for nodes in temp.children:
                if not(nodes in expanded) and not(nodes in frontier):
                    queue.append([nodes,depth+1])
                    frontier.add(nodes)
                    parentMap[nodes] = node1
        # failure to get path
        return []