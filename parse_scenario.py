import os

OUTPUT_DIR = "outputs"
OUTPUT_FILENAME = os.path.join(OUTPUT_DIR,'scenario.dzn')

def parse_scenario(initial_scenario):
    try:
        fp = open(f"{initial_scenario}",'r',encoding = 'utf-8')
        scenario = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
        N = fp.readline().strip()
        scenario.write(f"N={N};\n")
        
        fp.readline() # skip START line
        
        scenario.write(f"POSITIONS=[") 
        for _ in range(int(N)):
            pos = fp.readline().strip()
            if _ == int(N)-1: 
                scenario.write(f"{pos[2]}];\n")
            else: 
                scenario.write(f"{pos[2]}, ")
            
        fp.readline() # skip GOAL line

        scenario.write(f"GOAL=[") 
        for _ in range(int(N)):
            pos = fp.readline().strip()
            if _ == int(N)-1: 
                scenario.write(f"{pos[2]}];\n")
            else: 
                scenario.write(f"{pos[2]}, ")

        print("Parsing initial scenario configuration...")
                             
    finally:    
        fp.close()
        scenario.close()
    return "outputs/scenario.dzn"
