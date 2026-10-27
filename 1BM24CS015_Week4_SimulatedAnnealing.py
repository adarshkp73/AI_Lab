import random
import math

def get_conflicts(state):
    """Counts the number of mutually attacking pairs of queens."""
    conflicts = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def simulated_annealing(n):
    # Start with a random state
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_cost = get_conflicts(current)
    
    # Annealing parameters
    T = 1.0          # Initial temperature
    cooling_rate = 0.995
    
    while current_cost > 0 and T > 0.0001:
        # Pick a random neighbor (move one random queen to a random row)
        col = random.randint(0, n - 1)
        row = random.randint(0, n - 1)
        
        neighbor = list(current)
        neighbor[col] = row
        neighbor_cost = get_conflicts(neighbor)
        
        # Calculate change in cost (we want to minimize conflicts)
        dE = neighbor_cost - current_cost
        
        # Accept if it's better, or probabilistically if it's worse
        if dE < 0 or random.random() < math.exp(-dE / T):
            current = neighbor
            current_cost = neighbor_cost
            
        # Cool down the system
        T *= cooling_rate
        
    return current if current_cost == 0 else None

# --- Execution ---
N = 8
solution = None

# Restart if it cools down completely without finding a solution
while solution is None:
    solution = simulated_annealing(N)

print(f"Solved {N}-Queens: {solution}")
