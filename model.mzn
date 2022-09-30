% proj inputs/initial_graph.txt inputs/initial_scenario.txt
include "globals.mzn";
% constants
int: N; % No. of agents
int: V; % No. of vertices
int: E; % No. of edges

int: MaxMoves = V^3; 
% https://people.cs.rutgers.edu/~kb572/pubs/parallel_push_swap.pdf
%  It shows that a cubic number of moves as a function of the number of graph
% vertices is sufficient and that the decision problem can be
% solved in polynomial time

% funtions


% sets
set of int: AgentsRange = 1..N;
set of int: VertexRange = 1..V;
set of int: EdgesRange = 1..E;
set of int: MovesRange = 0..MaxMoves;



% input arrays 
array[AgentsRange] of VertexRange: INITIAL_POSITIONS;
array[AgentsRange] of VertexRange: GOAL;
array[EdgesRange, 1..2] of int: EDGES;

% vars
% array[AgentsRange] of var VertexRange: positions;
array[MovesRange, AgentsRange] of var VertexRange: Moves;

var 0..MaxMoves : size = card({ Moves[i, j] | i in MovesRange, j in AgentsRange }) div 3;


% fill 1st move
constraint forall(i in AgentsRange) (
    if INITIAL_POSITIONS[i] > 0 then Moves[0,i] = INITIAL_POSITIONS[i] else true endif );

% no overlap in agents/ in-rows
constraint forall (i in MovesRange) (
                   alldifferent( [ Moves[i,j] | j in AgentsRange ]) ); 

constraint forall (i in MovesRange) (
    if Moves[i,j] > 0 then Moves[


% all different rows? prevent cycles "row(Moves, i)""
% constraint alldifferent( Moves); 


solve minimize size;

output [ "Initial positions: \(INITIAL_POSITIONS)\n" ++
            "Goal positions: \(GOAL)\n"] ++ 
            ["No. of moves: \(size)\n"] ++
            [if j == 1 then "i=\(i)\t" ++ "\(j):" ++ show(Moves[i,j]) ++ "\t"
                elseif j == N then "\(j):" ++ show(Moves[i,j]) ++ "\n"
                else  "\(j):" ++ show(Moves[i,j])  ++ "\t" endif 
                | i in 0..fix(10 - 1), j in AgentsRange]; % replace 10 for "size"
            


% https://stackoverflow.com/questions/58502580/printing-part-of-an-array-in-minizinc