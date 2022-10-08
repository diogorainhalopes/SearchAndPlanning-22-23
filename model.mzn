% proj inputs/initial_graph.txt inputs/initial_scenario.txt
include "globals.mzn";
% constants
int: N; % No. of agents
int: V; % No. of vertices
int: E; % No. of edges
int: minspan;
int: MaxMoves;
%E*3; %V^3; 
% https://people.cs.rutgers.edu/~kb572/pubs/parallel_push_swap.pdf
%  It shows that a cubic number of moves as a function of the number of graph
% vertices is sufficient and that the decision problem can be
% solved in polynomial time

% funtions


% sets
set of int: AgentsRange = 1..N;
set of int: VertexRange = 1..V;
set of int: EdgesRange = 1..E;
set of int: MovesRange = 1..MaxMoves;

% input arrays 
array[AgentsRange] of VertexRange: INITIAL_POSITIONS;
array[AgentsRange] of VertexRange: GOAL;
array[EdgesRange, 1..2] of int: EDGES;

% vars
array[MovesRange, AgentsRange] of var VertexRange: Moves;
var minspan..MaxMoves: obj;
constraint assert(N < V, "More vertices than agents are required to move");

constraint 
        (Moves[1,..] = INITIAL_POSITIONS)
        /\
        (forall(i in 1..obj) ( alldifferent( [ Moves[i,j] | j in AgentsRange ]))) % all agents in diff
        /\
        forall(i in 2..obj, j in AgentsRange) (
                (Moves[i,j] == Moves[i - 1,j])
                \/ 
                (((exists(k in EdgesRange) ( (Moves[i,j] == EDGES[k, 1]  /\ Moves[i - 1,j] == EDGES[k, 2])))
                        \/ (exists(k in EdgesRange) ((Moves[i,j] == EDGES[k, 2]  /\ Moves[i - 1,j] == EDGES[k, 1]))))
                /\ 
                (not(exists(k in [Moves[i - 1, l] | l in AgentsRange]) ( Moves[i,j] == k))))
                %/\ ([ Moves[i,j] - Moves[i-1, l] != 0 | l in AgentsRange ])
        )
        /\
        (forall(i in 2..obj) (Moves[i,..] != Moves[i-1, ..]) ) % all rows diff
        /\
        (forall(i in obj..MaxMoves) ( Moves[i,..] == GOAL)) % final position
;

solve
        :: seq_search([
                %int_search([EDGES[i,j] | i in EdgesRange, j in 1..2 ], input_order, indomain_split),
                int_search( [obj], first_fail, indomain_min),
                %int_search([ Moves[i,j] | i in 1..minspan, j in AgentsRange ], most_constrained, indomain),
        ])
        minimize obj;

output [if j == 1 /\ j != N
                then "i=\(i - 1)    " ++ "\(j):" ++ show(Moves[i,j]) ++ "  "
        elseif j == 1 /\ j == N
                then "i=\(i - 1)    " ++ "\(j):" ++ show(Moves[i,j]) ++ "\n"
        elseif j == N 
                then "\(j):" ++ show(Moves[i,j]) ++ "\n"
        else  
                "\(j):" ++ show(Moves[i,j])  ++ "  " 
        endif 
        | i in 1..fix(obj), j in AgentsRange];
