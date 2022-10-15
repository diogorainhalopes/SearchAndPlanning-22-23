#!/usr/bin/python
import parse_scenario as ps
OUTPUT_FILENAME = "data/minspan.dzn"


def parse_minspan():
    ms = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
    ms.write(f"minspan={ps.max_ms};\n")
    ms.close()
    return f"{OUTPUT_FILENAME}"
