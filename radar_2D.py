import numpy as np
import matplotlib.pyplot as plt

# Constants
num_targets = 5  # Number of targets
radar_range = 1000  # Radar range (meters)

# Generate random positions for targets within radar range
x_positions = np.random.uniform(-radar_range, radar_range, num_targets)
y_positions = np.random.uniform(-radar_range, radar_range, num_targets)

# Plot targets on a 2D radar map
plt.figure(figsize=(8, 8))
plt.scatter(x_positions, y_positions, c='red', label='Targets')
plt.title("2D Radar Map")
plt.xlabel("X Position (m)")
plt.ylabel("Y Position (m)")
plt.xlim(-radar_range, radar_range)
plt.ylim(-radar_range, radar_range)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
