class Node:
    def __init__(self, val):
        self.val = val
        self.neighbours = []
        self.visited = False


def detectRoute(node_a, node_b):
    detectRoute.routeFound = False

    def dfs(node):
        if not detectRoute.routeFound: # for early termination
            # base case: null node
            if not node: 
                return

            # process current node 
            print(node.val, node_b.val)
            if node == node_b:
                detectRoute.routeFound = True
            node.visited = True

            # check all neighbours
            for n in node.neighbours:
                if not n.visited:
                    dfs(n)

    dfs(node_a)
    return detectRoute.routeFound

def setupGraph():
    node_a = Node(5)
    node_b = Node(1)
    node_c = Node(7)
    node_d = Node(4)
    node_e = Node(6)
    node_f = Node(9)
    node_g = Node(2)

    node_a.neighbours.append(node_b)
    node_b.neighbours.extend([node_a, node_d, node_e])
    node_c.neighbours.append(node_b)
    node_d.neighbours.append(node_g)
    node_e.neighbours.extend([node_c, node_f])
    node_f.neighbours.extend([node_d, node_e])

    return [node_a, node_b, node_c, node_d, node_e, node_f, node_g]

if __name__ == "__main__":
    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_a, node_d) == True

    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_a, node_c) == True

    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_d, node_e) == False

    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_a, node_g) == True

    node_a, node_b, node_c, node_d, node_e, node_f, node_g = setupGraph()
    assert detectRoute(node_g, node_b) == False
    
