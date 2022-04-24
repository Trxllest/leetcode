"""There is an undirected star graph consisting of n nodes labeled from 1 to n.
 A star graph is a graph where there is one center node and exactly n - 1 edges 
 that connect the center node with every other node.
You are given a 2D integer array edges where each edges[i] = [ui, vi] 
indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.
"""

"""Input: edges = [[1,2],[2,3],[4,2]]
   Output: 2
"""

class Solution:
    def findCenter(self, edges):
        x,y = edges[0][0],edges[0][1]
        if x==edges[1][0] or x ==edges[1][1]:
            return x
        return y
