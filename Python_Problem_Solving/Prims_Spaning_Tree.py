
'''
https://practice.geeksforgeeks.org/problems/minimum-spanning-tree/1
'''
#User function Template for python3
import heapq
class Solution:
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        #code here
        heap = []
        visited = [0]*V
        mst_wt = 0
        edges = 0
        heapq.heappush(heap,[0,0])
                        #w,d
        while edges < V:
            pq = heapq.heappop(heap)
            current_node = pq[1]
            current_node_wt = pq[0]
            if visited[current_node] == 1:
                continue
            visited[current_node] = 1
            mst_wt += current_node_wt
            edges += 1
            for node in adj[current_node]:
                adj_node = node[0]
                adj_wt = node[1]
                if visited[adj_node] != 1:
                    heapq.heappush(heap,[adj_wt,adj_node])
                    
        return mst_wt


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends
