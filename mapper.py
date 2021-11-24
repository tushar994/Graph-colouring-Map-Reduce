#!/usr/bin/env python3
"""mapper.py"""

import sys

def check_if_least(vertice, graph,C):
    # print("checking ", vertice)
    for j in graph[vertice]:
        if(j<vertice and j in C):
            return 0
    return 1

def remove_connect(vertice,C,graph):
    return_arr = C.copy()
    return_arr.remove(vertice)
    for j in graph[vertice]:
        if(j in return_arr):
            return_arr.remove(j)
    return return_arr

# this function takes the graph, all the vertices, and gives you a MIS
def find_MIS(graph, all_vertices):
    I = []
    C = []
    flag = 1
    index = 0
    for vertices in all_vertices:
        C.append(vertices)
    while(flag):
        # print(C)
        if(index >= len(C)):
            index = 0
        if(C==[]):
            break
        if(check_if_least(C[index],graph,C)):
            I.append(C[index])
            C = remove_connect(C[index],C,graph)
        index+=1
    # print(I)
    # print(C)
    return I
        


graph = {}
all_vertices = set()
flag = 0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    if(flag == 0):
        for i in words:
            all_vertices.add(i)
            graph[i] = []
        flag = 1
    else:
        if(words[0] not in graph.keys()):
            graph[words[0]] = [words[1]]
        else:
            if(words[1] not in graph[words[0]]):
                graph[words[0]].append(words[1])
        if(words[1] not in graph.keys()):
            graph[words[1]] = [words[0]]
        else:
            if(words[0] not in graph[words[1]]):
                graph[words[1]].append(words[0])
        all_vertices.add(words[0])
        all_vertices.add(words[1])
# so now we have taken the input

index = 0
while(1):
    index +=1
    I = find_MIS(graph,all_vertices)
    for i in I:
        print(index,"\t", i)
    for i in I:
        all_vertices.remove(i)
        del graph[i]
    if(len(all_vertices)==0):
        break




