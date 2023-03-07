import open3d as o3d
import numpy as np

# Load the CSV file
map_data = np.genfromtxt("./pointcloud/map.csv", delimiter=",", skip_header=1)

# Extract the points and colors
points = map_data[:, :3]
colors = map_data[:, 3:6] / 255.0  # Scale RGB values to [0, 1]

# Create a point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors)

# Display the point cloud
o3d.visualization.draw_geometries([pcd])
