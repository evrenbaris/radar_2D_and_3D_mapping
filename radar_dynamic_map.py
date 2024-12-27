import matplotlib.animation as animation

# Simulate target movements
num_steps = 100  # Number of time steps
x_movements = np.random.uniform(-10, 10, (num_targets, num_steps))
y_movements = np.random.uniform(-10, 10, (num_targets, num_steps))

# Initialize figure
fig, ax = plt.subplots(figsize=(8, 8))
sc = ax.scatter([], [], c='red', label='Targets')
ax.set_xlim(-radar_range, radar_range)
ax.set_ylim(-radar_range, radar_range)
ax.set_title("Dynamic 2D Radar Map")
ax.set_xlabel("X Position (m)")
ax.set_ylabel("Y Position (m)")
ax.grid(True)

# Update function for animation
def update(frame):
    sc.set_offsets(np.c_[x_positions + x_movements[:, frame], y_positions + y_movements[:, frame]])
    return sc,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=num_steps, interval=100, blit=True)
plt.legend()
plt.show()
