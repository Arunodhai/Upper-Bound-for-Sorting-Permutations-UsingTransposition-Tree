# -*- coding: utf-8 -*-
"""Algo D FINAL

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qwkUR1nHU3V0YPLJGtyJ2JTKvWoJytyF
"""

import networkx as nx
import numpy as np
import math
from collections import Counter


global dist
dist = [[0 for x in range(300)] for y in range(300)]
global vis
vis = [300]
global dis
dis = [300]
global distsum
distsum = [300]
global distcount
distcount = [300]
global C
C={}




G = nx.Graph()


def create_TT():
  edges=[]
  node_count = int(input("Enter the number of vertices in the Transposition tree "))
  for i in range(1,(node_count+1)): #add the vertices
    G.add_node(i)
  print("Enter the edges ")
  for i in range(1,node_count): #add the edges
    t = tuple(map(int,input().split()))
    G.add_edge(*t)  
    edges.append(list(t))

  adjacency_matrix = nx.to_numpy_array(G)
  bfs(adjacency_matrix, node_count)


# function to create a Transposition tree
def checkStar(adjacency_matrix, node_count, count):

    vertexD1 = 0
    vertexDn_1 = 0

    for i in range(0, node_count):

        degreeI = 0
        for j in range(0, node_count):
            if (adjacency_matrix[i][j]==1):
                degreeI = degreeI + 1

        if (degreeI == 1):
            vertexD1 = vertexD1 + 1

        elif (degreeI == count - 1):
            vertexDn_1 = vertexDn_1 + 1


    return (vertexD1 == (count - 1) and
              vertexDn_1 == 1)


def bfs(adjacency_matrix, node_count):
  dist = [[0 for x in range(300)] for y in range(300)]
  tno = node_count
  for x in range(1,tno+1): #bfs is done from every vertex in order to obtain the shortest path from every vertex to every other vertex in the tree.
      dis = [0 for y in range(300)]
      vis = [0 for y in range(300)]
      queue = []
      queue.append(x)
      vis[x] = 1
      dis[x] = 0
      while (not (len(queue)==0)):
          tmp = queue[0]
          queue.pop(0)
          for y in range(1,tno+1):
              
              if ((adjacency_matrix[tmp-1][y-1] or adjacency_matrix[y-1][tmp-1]) and not (vis[y])):
                  vis[y] = 1
                  dis[y] = dis[tmp] + 1
                  queue.append(y)
              elif ((adjacency_matrix[tmp-1][y-1] or adjacency_matrix[y-1][tmp-1]) and vis[y] and dis[y] > dis[tmp] + 1):
                  dis[y] = dis[tmp] + 1

      for y in range(1,tno+1):
          if (vis[y] and (dist[x][y] == 0 or dist[x][y] > dis[y])):
              dist[x][y] = dis[y]

  distsum = [0 for x in range(300)]

  for x in range(1,tno+1):  #finding the distance-sum of each vertex.
      for y in range(1, tno+1):
          distsum[x] = distsum[x] + dist[x][y]
  
          
    
  algoD(adjacency_matrix, node_count,distsum,dist)
 
    
global s_nodelistD

def algoS(adjacency_matrix, node_count,distsum,dist,nodecount_temp):

  
  s_nodelistD=[]

  max1 = max(distsum)         #finding the node having maximum distance sum
  sourceNode = distsum.index(max1)
  Ecc = 0
  for x in range(1,nodecount_temp+1):       #finding the maximum eccentricity
      Ecc = max(Ecc, dist[sourceNode][x])
      
  
  #print("Ecc : ",Ecc)
  for x in range(1,nodecount_temp+1):
    for y in range(1,nodecount_temp+1):
       if (dist[x][y] == Ecc) :
          s_nodelistD.append(x)
          
  
  return (list(set(s_nodelistD)))



def algoD(adjacency_matrix, node_count,distsum,dist):

   gamma=0
   count=0
   nodecount_temp=node_count
  
   if (checkStar(adjacency_matrix, nodecount_temp,node_count)):    #checks if the given tree is a star graph.
        gamma = gamma + 3 * (node_count - 1) // 2
        print("\nIs a star graph.")

   else:
        no=node_count
        while (no > 0):

      
          S=algoS(adjacency_matrix, node_count,distsum,dist,nodecount_temp)
      

          max1 = max(distsum) 
          sourceNode = distsum.index(max1)
          diam = 0
          for x in range(1,nodecount_temp+1): #finding the diameter
              diam = max(diam, dist[sourceNode][x])

          
          if(len(S)%2==0):
              gamma=math.floor(gamma+(len(S)*(diam-(1/2))))

              tno=nodecount_temp
              for y in S :
                  distsum[y]=0
                  for x in range(1,tno+1):  #making all its entries invalid in the distance matrix, updating the distsum and degree_count
                      if (not (x == y) and not (distsum[x] == 0)):
                          if (x < y):
                              distsum[x] = distsum[x] - dist[x][y]
                          else:
                              distsum[x] = distsum[x] - dist[x][y]

                  for x in range(1,tno+1):
                        dist[y][x] = 0
                        dist[x][y] = 0
                        adjacency_matrix[y-1][x-1] = 0
                        adjacency_matrix[x-1][y-1] = 0


              no = no - len(S)
              node_count=node_count-len(S)
              C.clear()
              S.clear()

          else :
            gamma=math.floor(gamma+(len(S)*((diam-(1/2))-(1/2))))

            tno=nodecount_temp
            for y in S :
                distsum[y]=0
                for x in range(1,tno+1):  #making all its entries invalid in the distance matrix, updating the distsum and degree_count
                    if (not (x == y) and not (distsum[x] == 0)):
                        if (x < y):
                            distsum[x] = distsum[x] - dist[x][y]
                        else:
                            distsum[x] = distsum[x] - dist[x][y]

                for x in range(1,tno+1):
                      dist[y][x] = 0
                      dist[x][y] = 0
                      adjacency_matrix[y-1][x-1] = 0
                      adjacency_matrix[x-1][y-1] = 0



            no = no - len(S)
            node_count=node_count-len(S)
            C.clear()
            S.clear()
                  

          

          if (checkStar(adjacency_matrix, nodecount_temp,node_count)):    #checks if the given tree is a star graph.
            gamma = gamma + 3 * (node_count - 1) // 2
            break


   print("\nUPPERBOUND :",gamma)
   return


create_TT()