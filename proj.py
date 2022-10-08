#!/usr/bin/python

#run without calling python
#C:\> assoc .py=Python
#C:\> ftype Python="C:\python310\python.exe %1 %*"

import sys
import os
from parse_graph import parse_graph
from parse_scenario import parse_scenario
from parse_solution import parse_solution

MZ = "minizinc"
MODEL = "model.mzn"
SOLVER = "Chuffed"
SOLUTION = "solution.txt"
TEMP_SOLUTION = "temp_solution.txt"

def main():
    if(len(sys.argv) != 3):
        sys.exit("Usage: proj initial_graph.txt initial_scenario.txt")
    graph = parse_graph(sys.argv[1])
    scenario = parse_scenario(sys.argv[2])
    os.system(f"{MZ} --solver {SOLVER} {MODEL} {graph} {scenario} > {TEMP_SOLUTION}")
    parse_solution(f"{TEMP_SOLUTION}")
    os.remove(f"{TEMP_SOLUTION}")
    
    if sys.platform.startswith('win'):
        os.system(f"type solution.txt")
    else:
        os.system(f"cat solution.txt")
        
if __name__ == "__main__":
    main()

