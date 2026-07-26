import open3d as o3d
import cv2
import numpy as np

# Path configuration
rgb_path = "color_002.png"
depth_path = "depth_002.png"

# Load the depth image
depth = cv2.imread(depth_path, cv2.IMREAD_UNCHANGED)  # Preserve the original depth values
height, width = depth.shape

# Load the RGB image and resize it to match the depth image
color = cv2.imread(rgb_path)
color = cv2.resize(color, (width, height))
color = cv2.cvtColor(color, cv2.COLOR_BGR2RGB)

# Convert to Open3D images
color_o3d = o3d.geometry.Image(color)
depth_o3d = o3d.geometry.Image(depth)

# Set camera intrinsics for the depth-image resolution
fx, fy = 525.0, 525.0  # Focal length; adjust for the camera if needed
cx, cy = width / 2, height / 2
intrinsic = o3d.camera.PinholeCameraIntrinsic(width, height, fx, fy, cx, cy)

# Create an RGB-D image
rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
    color_o3d,
    depth_o3d,
    depth_scale=1000.0,   # Use when depth values are in millimeters
    convert_rgb_to_intensity=False
)

# Generate a point cloud from the RGB-D image
pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic)

# Optional coordinate-system adjustment
pcd.transform([[1, 0, 0, 0],
               [0, -1, 0, 0],
               [0, 0, -1, 0],
               [0, 0, 0, 1]])

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])

# Save the point cloud
o3d.io.write_point_cloud("output.ply", pcd)
print("Point cloud saved as output.ply")
