#!/usr/bin/python

#run without calling python
#C:\> assoc .py=Python
#C:\> ftype Python="C:\python310\python.exe %1 %*"

import sys
import os
from parse_graph import parse_graph
from parse_scenario import parse_scenario

MZ = "minizinc"
MODEL = "model.mzn"

def main():
    graph = parse_graph(sys.argv[1])
    scenario = parse_scenario(sys.argv[2])
    os.system(f"minizinc {MODEL} {graph} {scenario} > solution.txt")

if __name__ == "__main__":
    main()

