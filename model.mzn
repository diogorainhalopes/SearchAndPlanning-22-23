% proj inputs/initial_graph.txt inputs/initial_scenario.txt
include "globals.mzn";
% constants
int: N; % No. of agents
int: V; % No. of vertices
%int: E; % No. of edges
int: MAXLEN;
int: minspan;
%E*3; %V^3; 
% https://people.cs.rutgers.edu/~kb572/pubs/parallel_push_swap.pdf
%  It shows that a cubic number of moves as a function of the number of graph
% vertices is sufficient and that the decision problem can be
% solved in polynomial time

% functions


% sets
set of int: AgentsRange = 1..N;
set of int: VertexRange = 1..V;
set of int: EdgesRange = 1..MAXLEN;
set of int: MovesRange = 0..minspan;

% input arrays 
array[AgentsRange] of VertexRange: INITIAL_POSITIONS;
array[AgentsRange] of VertexRange: GOAL;
array[VertexRange, EdgesRange] of int: EDGES;

% vars
array[MovesRange, AgentsRange] of var VertexRange: Moves;
%var minspan..MaxMoves: obj;

constraint assert(N < V, "More vertices than agents are required to move");

constraint 
        (Moves[0,..] == INITIAL_POSITIONS) /\ (Moves[minspan,..] == GOAL)
        /\
        (forall(i in 0..minspan) ( alldifferent( [ Moves[i,j] | j in AgentsRange ]))) % all agents in diff
        /\
        forall(i in 1..minspan, j in AgentsRange) (
                (Moves[i,j] == Moves[i - 1, j])
                \/ 
                (( exists(k in EdgesRange) ( Moves[i, j] == EDGES[Moves[i - 1, j], k] ))
                 /\ 
                (not(exists(k in [Moves[i - 1, l] | l in AgentsRange]) ( Moves[i, j] == k))))
        )
        /\
        (forall(i in 1..minspan) (Moves[i,..] != Moves[i - 1,..]) ) % all rows diff
;

solve satisfy;

output [if j == 1 /\ j != N
                then "i=\(i)    " ++ "\(j):" ++ show(Moves[i,j]) ++ "  "
        elseif j == 1 /\ j == N
                then "i=\(i)    " ++ "\(j):" ++ show(Moves[i,j]) ++ "\n"
        elseif j == N 
                then "\(j):" ++ show(Moves[i,j]) ++ "\n"
        else  
                "\(j):" ++ show(Moves[i,j])  ++ "  " 
        endif 
        | i in 0..fix(minspan), j in AgentsRange];
