import open3d as o3d
import numpy as np
import cv2

# Set camera intrinsics (adjust for your camera)
width, height = 640, 480
fx, fy = 525.0, 525.0  # Focal length
cx, cy = width / 2, height / 2

intrinsic = o3d.camera.PinholeCameraIntrinsic(width, height, fx, fy, cx, cy)

# RGB and depth file paths
rgb_path = "color_002.png"
depth_path = "depth_002.png"

# Load images
color = o3d.io.read_image(rgb_path)
depth = o3d.io.read_image(depth_path)

# Create an RGB-D image
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color, depth, convert_rgb_to_intensity=False
)

# Generate a point cloud from the RGB-D image
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic)

# Optional: adjust the coordinate system
pcd.transform([[1, 0, 0, 0],
               [0, -1, 0, 0],
               [0, 0, -1, 0],
               [0, 0, 0, 1]])

# Visualize
o3d.visualization.draw_geometries([pcd])

# Save the point cloud
o3d.io.write_point_cloud("output.ply", pcd)
print("Point cloud saved as output.ply")
