#!/usr/bin/python
OUTPUT_FILENAME = "data/graph.dzn"

global parse_edges
def read_nodes(edge, parse_edges):
    ed = [int(x) for x in edge.split()]
    parse_edges[ed[0]].append(ed[1])
    parse_edges[ed[1]].append(ed[0])
    
    return f"{ed[0]}, {ed[1]}"



def parse_graph(initial_graph):
    try:
        global V
        fp = open(f"{initial_graph}",'r',encoding = 'utf-8')
        V = fp.readline().strip()
        while(V[0] == "#"): 
            V = fp.readline().strip() 
        E = fp.readline().strip()
        edges = fp.readlines()
                
        graph = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
        
        graph.write(f"V={V};\n")
        graph.write(f"E={E};\n")
        graph.write(f"EDGES=[|\n") 
        
        global parse_edges
        parse_edges = {List: [] for List in range(1, int(V)+1) } 
        for edge in edges:
            if edges.index(edge) == int(E) - 1:
                graph.write(f"{read_nodes(edge, parse_edges)}|];\n")
            else:
                graph.write(f"{read_nodes(edge, parse_edges)}|\n")
        # print(parse_edges) 
    finally:    
        fp.close()
        graph.close()
    return f"{OUTPUT_FILENAME}"
