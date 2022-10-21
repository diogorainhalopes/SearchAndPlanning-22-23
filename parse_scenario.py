import os
import parse_graph as pg
import numpy as np
from dijkstar import Graph, find_path


OUTPUT_FILENAME = "data/scenario.dzn"

def read_positions(pos):
    n = [int(x) for x in pos.split()]
    return f"{n[1]}"


def parse_scenario(initial_scenario):
    try:
        os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)
        #print("Parsing initial scenario configuration...")
        fp = open(f"{initial_scenario}",'r',encoding = 'utf-8')
        scenario = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
        
        N = fp.readline().strip()
        while(N[0] == "#"): 
            N = fp.readline().strip()    
                    
        scenario.write(f"N={N};\n")
        
        fp.readline() # skip START line
        init = [0] * int(N)
        gl = [0] * int(N)
        scenario.write(f"INITIAL_POSITIONS=[") 
        for i in range(int(N)):
            pos = fp.readline().strip()
            temp = read_positions(pos) 
            init[i] = int(temp)
            if i == int(N)-1: 
                scenario.write(f"{temp}];\n")
            else: 
                scenario.write(f"{temp}, ")
            
        fp.readline() 

        scenario.write(f"GOAL=[") 
        for i in range(int(N)):
            pos = fp.readline().strip()
            temp = read_positions(pos) 
            gl[i] = int(temp)
            if i == int(N)-1: 
                scenario.write(f"{temp}];\n")
            else: 
                scenario.write(f"{temp}, ")

        distances = np.zeros([int(pg.V), int(N)], dtype=int)
        
    
        graph = Graph ()
        for i in pg.parse_edges:
            for j in pg.parse_edges[i]:
                graph.add_edge(i, j, 1)
                
       
        
                
        for i in range(0, int(pg.V)):
            for j in range(0, int(N)):

                distances[i][j] = find_path(graph, i+1, gl[j]).total_cost
                
        scenario.write(f"TIMES=[|\n") 
        for i in range(0, len(distances)):
            for j in range(0, len(distances[i])):
                if(j == int(N)-1):
                    scenario.write(f"{distances[i][j]}|")
                else:
                    scenario.write(f"{distances[i][j]}, ")
            if(i == int(pg.V)-1):
                scenario.write(f"];\n")
            else:
                scenario.write(f"\n")
                
                
        
        times = np.zeros( len(init), dtype=int)
        for i in range(len(init)):
            times[i] = len(find_path(graph, init[i], gl[i]).nodes)
      
        global max_ms 
        max_ms = max(times)
                                       
    finally:    
        fp.close()
        scenario.close()
    return f"{OUTPUT_FILENAME}"
