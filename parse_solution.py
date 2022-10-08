# should send to temporary directory?
def parse_solution(solution_temp):
    try:
        #print("Parsing solution...\n")
        fp = open(f"{solution_temp}",'r',encoding = 'utf-8')
        lines = fp.readlines() # skip GOAL line
        
        for line in lines:
            if line[0] == "-":
                break
            print(f"{line}", end = '')
                             
    finally:    
        fp.close()
