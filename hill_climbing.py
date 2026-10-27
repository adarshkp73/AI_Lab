import random

def get_conflicts(state):
    """Counts the number of mutually attacking pairs of queens."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            # Check if they share the same row or the same diagonal
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def hill_climbing(n):
    # Start with a random row position for each column
    current_state = [random.randint(0, n - 1) for _ in range(n)]
    current_conflicts = get_conflicts(current_state)
    
    while current_conflicts > 0:
        best_neighbor = list(current_state)
        best_conflicts = current_conflicts
        
        # Evaluate all possible single-queen moves (neighbors)
        for col in range(n):
            for row in range(n):
                if current_state[col] == row:
                    continue
                
                # Propose a move
                neighbor = list(current_state)
                neighbor[col] = row
                neighbor_conflicts = get_conflicts(neighbor)
                
                # Track the steepest descent (lowest conflict state)
                if neighbor_conflicts < best_conflicts:
                    best_conflicts = neighbor_conflicts
                    best_neighbor = neighbor
                    
        # If no neighbor is better, we are stuck in a local minimum/shoulder
        if best_conflicts >= current_conflicts:
            return None # Failure (requires a random restart)
            
        current_state = best_neighbor
        current_conflicts = best_conflicts
        
    return current_state

# --- Execution ---
N = 8
solution = None

# Keep restarting from new random states until a global solution is found
while solution is None:
    solution = hill_climbing(N)

print(f"Solved {N}-Queens: {solution}")
