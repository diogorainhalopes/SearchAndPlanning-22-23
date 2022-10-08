#!/usr/bin/python

def bfs(edges, start, goal):
    queue = [[start]]
    if start == goal:
        return queue[0]
    visited = []
    visited.append(start)
        
    vertex = 0
    while vertex < len(queue):
        current = queue[vertex]
        previous = current[-1]
        path = edges[previous]
        if goal in path:
            current.append(goal)
            return current
        for next_vertex in path:
            if next_vertex not in visited:
                npath = current
                npath.append(next_vertex)
                queue.append(npath)
                visited.append(next_vertex)
        vertex += 1

def len_bfs(edges, starts, goals):
    times = [0] * len(starts)
    for i in range(len(starts)):
        times[i] = len(bfs(edges, starts[i], goals[i]))
    return times
