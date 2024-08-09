import numpy as np
import matplotlib.pyplot as plt

def gillespie(reactions, initial_counts, max_time):
    counts = np.array(initial_counts, dtype=float)
    times = [0]
    states = [counts.copy()]
    
    while times[-1] < max_time:
        propensities = np.array([k * np.prod([counts[i] for i, coeff in enumerate(reactants) if coeff > 0]) for reactants, _, k in reactions])
        total_propensity = propensities.sum()
        if total_propensity == 0:
            break
        
        next_time = times[-1] + np.random.exponential(1 / total_propensity)
        times.append(next_time)
        
        reaction_index = np.random.choice(len(reactions), p=propensities / total_propensity)
        reactants, products, _ = reactions[reaction_index]
        counts -= reactants
        counts += products
        
        states.append(counts.copy())
    
    return np.array(times), np.array(states)

# Define the chemical reactions and rates based on the paper
# Each reaction: ((reactants), (products), rate)
# The reactions are simplified for demonstration purposes
reactions = [
    ((0, 0, 0, 0, 0, 1, 0, 0, 0), (0, 0, 0, 0, 0, 0, 1, 0, 0), 1),  # A + y -> z
    ((0, 1, 0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 0, 0, 0, 0, 0, 0), 1),  # B + x -> A + x
    ((0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 1, 0, 0, 0, 0, 0, 0, 0), 1),  # B + z -> A + z
    ((0, 0, 0, 1, 0, 0, 0, 0, 0), (0, 0, 0, 0, 1, 1, 1, 0, 0), 1),  # C + x + y -> z + x + y
    ((0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1), 1),  # D + x + z -> D* + x + z
    ((0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0), 1),  # D* + y -> D + R
    ((0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1), 1),  # E + x -> E* + x
    ((0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0), 1),  # E* + z -> E + R
    ((0, 0, 0, 0, 0, 0, 0, 1, 0), (0, 0, 0, 0, 0, 0, 0, 0, 1), 1),  # E + y -> E* + y
    ((0, 0, 0, 0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0), 1),  # E* + z -> E + R
    ((0, 0, 0, 0, 0, 0, 1, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), 1),  # x -> R
    ((0, 0, 1, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), 1),  # y -> R
    ((0, 0, 0, 0, 1, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0), 1)   # z -> R
]
initial_counts = [0, 0, 0, 0, 0, 1, 0, 0, 0]  # Initial counts of each species

# Simulate
# times, states = gillespie(reactions, initial_counts, max_time=2000)
times, states = gillespie(reactions, initial_counts, max_time=100)

# Plot x-y, x-z, and y-z
plt.figure(figsize=(15, 5))

# x-y plot
plt.subplot(1, 3, 1)
plt.plot(states[:, 0], states[:, 1])
plt.xlabel('x')
plt.ylabel('y')
plt.title('x-y plot')

# x-z plot
plt.subplot(1, 3, 2)
plt.plot(states[:, 0], states[:, 2])
plt.xlabel('x')
plt.ylabel('z')
plt.title('x-z plot')

# y-z plot
plt.subplot(1, 3, 3)
plt.plot(states[:, 1], states[:, 2])
plt.xlabel('y')
plt.ylabel('z')
plt.title('y-z plot')

plt.tight_layout()
plt.show()