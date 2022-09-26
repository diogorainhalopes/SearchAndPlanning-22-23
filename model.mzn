include "alldifferent.mzn";

int: N;
int: V;
int: E;

set of int: AgentsRange = 1..N;
set of int: VertexRange = 1..V;
set of int: EdgesRange = 1..E;

array[AgentsRange] of VertexRange: POSITIONS;
array[AgentsRange] of VertexRange: GOAL;
array[EdgesRange, 1..2] of int: EDGES;

solve satisfy;

output [ show(POSITIONS) ++ "\n" ++ show(GOAL) ++ "\n" ++ show2d(EDGES)];