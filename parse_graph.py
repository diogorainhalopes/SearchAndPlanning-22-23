import os

OUTPUT_DIR = "outputs"
OUTPUT_FILENAME = os.path.join(OUTPUT_DIR,'graph.dzn')

def read_nodes(edge):
    e = ""
    for i in edge:
        if i == '\n' or i == '':
            return e
        if i != ' ':
            e += i
        else: e+= ", "
    return e

def parse_graph(initial_graph):
    try:
        fp = open(f"{initial_graph}",'r',encoding = 'utf-8')
        V = fp.readline().strip()
        E = fp.readline().strip()
        edges = fp.readlines()
        
        print("Parsing initial graph configuration...")
        
        graph = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
        graph.write(f"V={V};\n")
        graph.write(f"E={E};\n")
        graph.write(f"EDGES=[|\n") 
             
        for edge in edges:
            if edges.index(edge) == int(E) - 1:
                graph.write(f"{read_nodes(edge)}|];\n")
            else:
                graph.write(f"{read_nodes(edge)}|\n")
    finally:    
        fp.close()
        graph.close()
    return "outputs/graph.dzn"


