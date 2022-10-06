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

def main():
    if(len(sys.argv) != 3):
        sys.exit("Usage: proj initial_graph.txt initial_scenario.txt")
    graph = parse_graph(sys.argv[1])
    scenario = parse_scenario(sys.argv[2])
    os.system(f"minizinc --solver Chuffed {MODEL} {graph} {scenario} > solution_temp.txt")
    parse_solution("solution_temp.txt")
    os.remove("solution_temp.txt")
    os.system(f"type solution.txt")

if __name__ == "__main__":
    main()

