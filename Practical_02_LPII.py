import heapq

# Define the goal state
goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    return sum(abs(state.index(i) // 3 - goal_state.index(i) // 3) +
               abs(state.index(i) % 3 - goal_state.index(i) % 3)
               for i in state if i != 0)

# Function to generate next possible states
def generate_next_states(state):
    zero_index = state.index(0)
    next_states = []
    for move in [-3, 3, -1, 1]:
        if 0 <= zero_index + move < 9 and \
           abs(zero_index // 3 - (zero_index + move) // 3) + \
           abs(zero_index % 3 - (zero_index + move) % 3) == 1:
            new_state = state[:]
            new_state[zero_index], new_state[zero_index + move] = \
            new_state[zero_index + move], new_state[zero_index]
            next_states.append(new_state)
    return next_states

# Function to print the puzzle state
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(*state[i:i+3])
    print()

# Function to solve the 8-puzzle problem using A* algorithm
def solve_8_puzzle(initial_state):
    # Initialize the frontier with the initial state
    frontier = [(manhattan_distance(initial_state), initial_state, 0)]
    explored = set()  # Set to keep track of explored states
    while frontier:
        # Pop the state with the lowest cost from the frontier
        _, state, cost = heapq.heappop(frontier)
        # Check if the current state is the goal state
        if state == goal_state:
            print("Solution found!")
            print_puzzle(state)
            return cost  # Return the cost of reaching the goal state
        explored.add(tuple(state))  # Add the current state to explored set
        print(f"Current state (cost = {cost}):")
        print_puzzle(state)
        # Generate next possible states from the current state
        for next_state in generate_next_states(state):
            # Check if the next state is not already explored
            if tuple(next_state) not in explored:
                # Calculate the priority based on the Manhattan distance heuristic and the cost
                heapq.heappush(frontier, (manhattan_distance(next_state) + cost + 1, next_state, cost + 1))
    return None  # Return None if no solution is found

# Define the initial state of the puzzle
initial_state = [1, 3, 4, 8, 6, 2, 7, 0, 5]

print("Initial state:")
print_puzzle(initial_state)

# Solve the 8-puzzle problem
solution_cost = solve_8_puzzle(initial_state)

# Print the solution cost if a solution is found, otherwise print "No solution found"
if solution_cost is not None:
    print(f"Minimum number of moves: {solution_cost}")
else:
    print("No solution found")
