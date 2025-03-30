import cv2 import numpy as np import sys

Check if correct arguments are passed

if len(sys.argv) != 3: print("Usage: python sketch.py <input_video> <output_video>") sys.exit(1)

input_video = sys.argv[1] output_video = sys.argv[2]

Open video file

cap = cv2.VideoCapture(input_video) if not cap.isOpened(): print("Error: Could not open input video file.") sys.exit(1)

Get video properties

frame_width = int(cap.get(3)) frame_height = int(cap.get(4)) fps = int(cap.get(cv2.CAP_PROP_FPS))

Define codec and create VideoWriter object

fourcc = cv2.VideoWriter_fourcc(*'mp4v') out = cv2.VideoWriter(output_video, fourcc, fps, (frame_width, frame_height))

while True: ret, frame = cap.read() if not ret: break

# Convert to grayscale
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur
blur = cv2.GaussianBlur(gray, (5,5), 0)

# Detect edges using Canny
edges = cv2.Canny(blur, 30, 70)

# Convert edges to 3 channels
edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Write frame to output video
out.write(edges_colored)

Release everything

cap.release() out.release() cv2.destroyAllWindows() print("Processing complete! Output saved as:", output_video)

