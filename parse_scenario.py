OUTPUT_FILENAME = "data/scenario.dzn"

def read_positions(pos):
    p = ""
    index = 0
    for i in range(0,len(pos)):
        if pos[i] == ' ':
            index = i+1
            break
    while (index < len(pos)):
        p += pos[index]
        index += 1
    return p

def parse_scenario(initial_scenario):
    try:
        print("Parsing initial scenario configuration...")
        fp = open(f"{initial_scenario}",'r',encoding = 'utf-8')
        scenario = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
        
        N = fp.readline().strip()
        while(N[0] == "#"): 
            N = fp.readline().strip()    
                    
        scenario.write(f"N={N};\n")
        
        fp.readline() # skip START line
        
        scenario.write(f"INITIAL_POSITIONS=[") 
        for _ in range(int(N)):
            pos = fp.readline().strip()
            if _ == int(N)-1: 
                scenario.write(f"{read_positions(pos)}];\n")
            else: 
                scenario.write(f"{read_positions(pos)}, ")
            
        fp.readline() # skip GOAL line

        scenario.write(f"GOAL=[") 
        for _ in range(int(N)):
            pos = fp.readline().strip()
            if _ == int(N)-1: 
                scenario.write(f"{read_positions(pos)}];\n")
            else: 
                scenario.write(f"{read_positions(pos)}, ")

                             
    finally:    
        fp.close()
        scenario.close()
    return f"{OUTPUT_FILENAME}"
