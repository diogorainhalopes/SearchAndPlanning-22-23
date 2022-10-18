#!/usr/bin/python
import os
OUTPUT_FILENAME = "data/graph.dzn"

def read_nodes(edge, parse_edges):
    ed = [int(x) for x in edge.split()]
    parse_edges[ed[0]].append(ed[1])
    parse_edges[ed[1]].append(ed[0])


def parse_graph(initial_graph):
    try:
        global V
        os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)
        fp = open(f"{initial_graph}",'r',encoding = 'utf-8')
        V = fp.readline().strip()
        while(V[0] == "#"): 
            V = fp.readline().strip() 
        E = fp.readline().strip()
        edges = fp.readlines()
                
        graph = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
        graph.write(f"V={V};\n")
        #graph.write(f"E={E};\n")
        
        global parse_edges
        parse_edges = {List: [] for List in range(1, int(V)+1) } 
        for edge in edges: 
            read_nodes(edge, parse_edges)
            
        max_len = int(len(max(parse_edges.values(), key=len)))
        graph.write(f"MAXLEN={max_len};\n")
        graph.write(f"EDGES=[|\n") 
        for key, value in parse_edges.items():
            filler = 0;
            for e in value:
                if(value.index(e) == max_len-1):
                    graph.write(f"{e}")
                else:
                    graph.write(f"{e}, ")
                    filler += 1
                    
            while(filler < max_len and len(value) < max_len):
                if (filler == max_len -1  ):
                     graph.write(f"0")
                else:   
                    graph.write(f"0, ")
                filler += 1
                
            if (key == len(parse_edges)):
                graph.write('|];\n')
            else:
                graph.write('|\n')

    finally:    
        fp.close()
        graph.close()
    return f"{OUTPUT_FILENAME}"
