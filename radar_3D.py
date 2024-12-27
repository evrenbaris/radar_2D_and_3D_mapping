from mpl_toolkits.mplot3d import Axes3D

# Generate random positions for targets in 3D space
z_positions = np.random.uniform(-radar_range / 2, radar_range / 2, num_targets)

# Plot targets on a 3D radar map
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_positions, y_positions, z_positions, c='blue', label='Targets')
ax.set_title("3D Radar Map")
ax.set_xlabel("X Position (m)")
ax.set_ylabel("Y Position (m)")
ax.set_zlabel("Z Position (m)")
ax.set_xlim(-radar_range, radar_range)
ax.set_ylim(-radar_range, radar_range)
ax.set_zlim(-radar_range / 2, radar_range / 2)
plt.legend()
plt.show()
