% proj inputs/initial_graph.txt inputs/initial_scenario.txt
include "globals.mzn";
% constants
int: N; % No. of agents
int: V; % No. of vertices
int: E; % No. of edges

int: MaxMoves = E*2; %V^3; 
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
var 2..MaxMoves: minspan;

% fill 1st move
constraint Moves[1,..] = INITIAL_POSITIONS;

% no cycles/no rows repeat
constraint forall(i in 1..minspan) ( alldifferent( [ Moves[i,j] | j in AgentsRange ]) ); 

% no agents in the same node simultaneously
constraint forall(j in AgentsRange, i in 1..minspan ) ( alldifferent( [ Moves[i,j] ]) ); 

% after minspan, all positions dont change, therefore reaching thr goal
constraint forall(i in minspan..MaxMoves) ( Moves[i,..] == GOAL); 


constraint forall(i in 2..minspan, j in AgentsRange) (
        (Moves[i,j] == Moves[i - 1,j])
        \/ (((exists(k in EdgesRange) ( (Moves[i,j] == EDGES[k, 1]  /\ Moves[i - 1,j] == EDGES[k, 2])))
        \/ (exists(k in EdgesRange) ((Moves[i,j] == EDGES[k, 2]  /\ Moves[i - 1,j] == EDGES[k, 1]))))
        /\ (not(exists(k in [Moves[i - 1, l] | l in AgentsRange]) ( Moves[i,j] == k))))
        %/\ ([ Moves[i,j] - Moves[i-1, l] != 0 | l in AgentsRange ])
);


solve minimize minspan;

output [if j == 1 then "i=\(i - 1)    " ++ "\(j):" ++ show(Moves[i,j]) ++ "    "
                elseif j == N then "\(j):" ++ show(Moves[i,j]) ++ "\n"
                else  "\(j):" ++ show(Moves[i,j])  ++ "    " endif 
                | i in 1..fix(minspan), j in AgentsRange];

% "Initial positions: \(INITIAL_POSITIONS)\n" ++            
%             "Goal positions: \(GOAL)\n"] ++ 
%             ["No. of moves: \(minspan - 1)\n"] ++
% https://stackoverflow.com/questions/58502580/printing-part-of-an-array-in-minizinc