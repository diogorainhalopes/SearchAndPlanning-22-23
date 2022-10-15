#!/usr/bin/python

#run without calling python
#C:\> assoc .py=Python
#C:\> ftype Python="C:\python310\python.exe %1 %*"

# todo: 

import sys
import os
import random
from parse_graph import parse_graph
from parse_scenario import parse_scenario
from parse_solution import parse_solution

MZ = "minizinc"
MODEL = "model.mzn"
SOLVER = "Chuffed"
TEMP_SOLUTION = "temp_solution.txt"

def main():

    graph = parse_graph(sys.argv[1])
    scenario = parse_scenario(sys.argv[2])
    os.system(f"{MZ} --solver {SOLVER} {MODEL} {graph} {scenario} -p 16 > {TEMP_SOLUTION}")
    parse_solution(f"{TEMP_SOLUTION}")
    os.remove(f"{TEMP_SOLUTION}")
            
if __name__ == "__main__":
    main()

