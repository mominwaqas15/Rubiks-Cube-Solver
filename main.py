import json
from cube import RubiksCube
from solver import IDA_star, build_heuristic_db

MAX_MOVES = 5

cube = RubiksCube(n=2)
cube.show()

actions = [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]
h_db = build_heuristic_db(
    cube.stringify(),
    actions,
    max_moves=MAX_MOVES
)

print('\n----------------- After scrambling the cube ---------------\n')
cube.shuffle(
    l_rot=MAX_MOVES if MAX_MOVES < 5 else 5,
    u_rot=MAX_MOVES
)
cube.show()
print('\n--------------- Solving -----------------\n')
solver = IDA_star(h_db)
moves = solver.run(cube.stringify())

print("Number of moves required to solve the cube:", len(moves))

for m in moves:
    if m[0] == 'h':
        cube.horizontal_twist(m[1], m[2])
    elif m[0] == 'v':
        cube.vertical_twist(m[1], m[2])
    elif m[0] == 's':
        cube.side_twist(m[1], m[2])
    print("\n\nAfter move -> ", m, "the state of the cube is as following:\n\n")    
    cube.show()
