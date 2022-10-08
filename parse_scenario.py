import parse_graph as pg
import bfs

OUTPUT_FILENAME = "data/scenario.dzn"

def read_positions(pos):
    n = [int(x) for x in pos.split()]
    return f"{n[1]}"


def parse_scenario(initial_scenario):
    try:
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
            
        fp.readline() # skip GOAL line

        scenario.write(f"GOAL=[") 
        for i in range(int(N)):
            pos = fp.readline().strip()
            temp = read_positions(pos) 
            gl[i] = int(temp)
            if i == int(N)-1: 
                scenario.write(f"{temp}];\n")
            else: 
                scenario.write(f"{temp}, ")
        
        makespans = bfs.len_bfs(pg.parse_edges, init, gl)
        scenario.write(f"minspan={max(makespans)};\n")  
        if ((int(pg.V)) - int(N) <= 3): 
            scenario.write(f"MaxMoves={int(sum(makespans)* 1.5)};\n")  
        else:
            scenario.write(f"MaxMoves={int(sum(makespans))};\n")                                
    finally:    
        fp.close()
        scenario.close()
    return f"{OUTPUT_FILENAME}"
