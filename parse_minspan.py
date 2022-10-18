#!/usr/bin/python
import os
import parse_scenario as ps
OUTPUT_FILENAME = "data/minspan.dzn"


def parse_minspan():
    os.makedirs(os.path.dirname(OUTPUT_FILENAME), exist_ok=True)
    ms = open(f"{OUTPUT_FILENAME}",'w',encoding = 'utf-8')
    ms.write(f"minspan={ps.max_ms};\n")
    ms.close()
    return f"{OUTPUT_FILENAME}"
