#!/usr/bin/python

#run without calling python
#C:\> assoc .py=Python
#C:\> ftype Python="C:\python310\python.exe %1 %*"

# todo: 

import sys
import os
import parse_graph as pg
import parse_scenario as ps
import parse_minspan as pm
import signal


MZ = "minizinc"
MODEL = "model.mzn"
SOLVER = "Chuffed"
TEMP_SOLUTION = "temp_solution.txt"

def signal_handler(sig, frame):
    os.remove(f"{TEMP_SOLUTION}")
    sys.exit(0)

def parse_solution(solution_temp):
    temp = False
    try:
        #print("Parsing solution...\n")
        fp = open(f"{solution_temp}",'r',encoding = 'utf-8')
        lines = fp.readlines()
        
        for line in lines:
            if(line[0] == "="):
                ps.max_ms +=1
                temp = True
                fp = open("data/minspan.dzn","r+")
                fp.truncate(0)
                fp.close()
                break
            
            if line[0] == "-":
                break
            print(f"{line}", end = '')
                             
    finally:    
        fp.close()
    return temp
    

def main():
    retry = True
    graph = pg.parse_graph(sys.argv[1])
    scenario = ps.parse_scenario(sys.argv[2])
    signal.signal(signal.SIGINT, signal_handler)
    while(retry):
        ms = pm.parse_minspan()
        os.system(f"{MZ} --solver {SOLVER} {MODEL} {graph} {scenario} {ms} > {TEMP_SOLUTION}")
        retry = parse_solution(f"{TEMP_SOLUTION}")
    os.remove(f"{TEMP_SOLUTION}")
    signal.pause()
            
if __name__ == "__main__":
    main()

