N = VER = 8
HOR = 1

def show(state, N=N):
    "Print a representation of a state as an NxN grid."
    # Initialize and fill in the board.
    board = ['.'] * N**2
    for (c, squares) in state:
        for s in squares:
            board[s] = c
    # Now print it out
    for i,s in enumerate(board):
        print s,
        if i % N == N - 1: print

def direction(car):
	return HOR if car[0]+1 == car[1] else VER

def canmove(state, car, next_car):
	usedplaces = [n for a in state for n in a[1] if n not in car and a[0] != "@"]
	return True if len(set(next_car).intersection(set(usedplaces))) == 0 else False

def move(state, car, move):
	return tuple(map(sum, zip(car, move)))

def auth_pos(state, car, len_car):
	t = []
	mul = direction(car)
	for way in (-1, 1):
		next_car = move(state, car, tuple([way*mul]*len_car))
		while canmove(state, car, next_car):
			t.append(next_car)
			next_car = move(state, next_car, tuple([way*mul]*len_car))
	return t

def next_state(state, N=N):
	t = []
	for car in state:
		if car[0] != '@' and car[0] != '|':
			next_state = auth_pos(state, car[1], len(car[1]))
			if next_state:
				t.append(tuple((car[0],next_state)))
	return tuple(t)

def successors(state, N=N):
	res = {}
	new_state = next_state(state, N)
	for nstate in new_state:
		for n_pos in nstate[1]:
			res[tuple([c_state if c_state[0] != nstate[0] else (c_state[0], n_pos) for c_state in list(state)])] = tuple((nstate[0], n_pos))
	return res

# Here are the shortest_path_search and path_actions functions from the unit.
# You may use these if you want, but you don't have to.
def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def solve_parking_puzzle(start, N=N):
    """Solve the puzzle described by the starting position (a tuple 
    of (object, locations) pairs).  Return a path of [state, action, ...]
    alternating items; an action is a pair (object, distance_moved),
    such as ('B', 16) to move 'B' two squares down on the N=8 grid."""
    def is_goal(state):
    	# il peut y avoir un overlap qu'en @ et si on overlap (si len differente) alors on est a la sortie
    	car_packed = [n for a in state for n in a[1]]
    	return len(set(car_packed))!=len(car_packed)

    # show the resolution
    sol = shortest_path_search(start, successors, is_goal)
    print
    for s in sol[0::2]:
    	show(s)
    	print
    return sol[1::2]
  
# But it would also be nice to have a simpler format to describe puzzles,
# and a way to visualize states.
# You will do that by defining the following two functions:
def locs(start, n, incr=1):
    "Return a tuple of n locations, starting at start and incrementing by incr."
    return tuple(n for n in range(start, start+incr*n, incr))


def grid(cars, N=N):
    """Return a tuple of (object, locations) pairs -- the format expected for
    this puzzle.  This function includes a wall pair, ('|', (0, ...)) to 
    indicate there are walls all around the NxN grid, except at the goal 
    location, which is the middle of the right-hand wall; there is a goal
    pair, like ('@', (31,)), to indicate this. The variable 'cars'  is a
    tuple of pairs like ('*', (26, 27)). The return result is a big tuple
    of the 'cars' pairs along with the walls and goal pairs."""
    wall = [w for w in range(0,N+1)] + \
           [w for w in range(2*N-1, N*(N-1), N)] + \
           [w for w in range(2*N, N*(N-1), N)] + \
           [w for w in range(N*(N-1), N*N)]
    issue = int((N*N-1)/2)
    wall.remove(issue) # + tuple(('|', tuple(sorted(wall))))
    return tuple([('@', (issue,))] + [a for a in cars] + [('|', tuple(sorted(wall)))])

# Here we see the grid and locs functions in use:

puzzle1 = grid((
    ('*', locs(26, 2)),
    ('G', locs(9, 2)),
    ('Y', locs(14, 3, N)),
    ('P', locs(17, 3, N)),
    ('O', locs(41, 2, N)),
    ('B', locs(20, 3, N)),
    ('A', locs(45, 2))))

puzzle2 = grid((
    ('*', locs(26, 2)),
    ('B', locs(20, 3, N)),
    ('P', locs(33, 3)),
    ('O', locs(41, 2, N)),
    ('Y', locs(51, 3))))

puzzle3 = grid((
    ('*', locs(25, 2)),
    ('B', locs(19, 3, N)),
    ('P', locs(36, 3)),
    ('O', locs(45, 2, N)),
    ('Y', locs(49, 3))))

print(solve_parking_puzzle(puzzle1, 8))
print(solve_parking_puzzle(puzzle2, 8))
print(solve_parking_puzzle(puzzle3, 8))