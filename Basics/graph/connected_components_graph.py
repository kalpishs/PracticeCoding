"""
3 Components in this graph with 10 nodes

1-----3                     2 --- 9         5 ----- 7
        \                                           \
         \                                           \
          4                                           10
          /
        /
       6 ---8
"""
class Adj():
    def __init__(self,val):
        self.vertex=val
        self.next=None

class Graph():
    def __init__(self,num):
        self.V=num
        self.graph=[None]*self.V
    def add_edge(self,m,n):
        node=Adj(n)
        node.next=self.graph[m]
        self.graph[m]=node

        node=Adj(m)
        node.next=self.graph[n]
        self.graph[n]=node

    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + " :", end="")
            temp = self.graph[i]
            while temp:
                print(f"-> {temp.vertex}", end=" ")
                temp = temp.next
            print(" \n")

if __name__ == "__main__":
    V = 11

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(1, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 6)
    graph.add_edge(6, 8)
    graph.add_edge(2, 9)
    graph.add_edge(5, 7)
    graph.add_edge(7, 10)

    graph.print_agraph()