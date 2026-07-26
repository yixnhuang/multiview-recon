import pyrealsense2 as rs
import numpy as np
import cv2
import os

# -----------------------------
# Configure the RealSense pipeline
# -----------------------------
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)   # Depth stream
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # RGB stream

# Start the pipeline
profile = pipeline.start(config)

# Configure alignment from depth to RGB
align_to = rs.stream.color
align = rs.align(align_to)

# Create the output directory
save_path = "data"
os.makedirs(save_path, exist_ok=True)
frame_id = 0

print("Press 's' to save RGB and depth frames, or 'q' to quit")

try:
    while True:
        # Wait for a frame
        frames = pipeline.wait_for_frames()

        # Align the frames
        aligned_frames = align.process(frames)
        aligned_depth = aligned_frames.get_depth_frame()
        color_frame = aligned_frames.get_color_frame()

        if not aligned_depth or not color_frame:
            continue

        # Convert to NumPy arrays
        depth_image = np.asanyarray(aligned_depth.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Create a colorized depth image for display only
        depth_colormap = cv2.applyColorMap(
            cv2.convertScaleAbs(depth_image, alpha=0.03),
            cv2.COLORMAP_JET
        )

        # Display
        cv2.imshow('Color', color_image)
        cv2.imshow('Depth', depth_colormap)

        # Handle keyboard input
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # Save RGB and depth frames
            cv2.imwrite(os.path.join(save_path, f"color_{frame_id:06d}.png"), color_image)
            cv2.imwrite(os.path.join(save_path, f"depth_{frame_id:06d}.png"), depth_image)  # 16-bit PNG
            print(f"Saved frame {frame_id}")
            frame_id += 1

        elif key == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
