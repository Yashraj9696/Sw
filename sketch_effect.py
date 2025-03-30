import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def apply_sketch_effect(frame):
    """Convert a frame to a pencil sketch."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    inverted = cv2.bitwise_not(gray)  # Invert grayscale image
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)  # Apply Gaussian blur
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)  # Blend the images
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)  # Convert back to 3-channel format

def process_video(input_path, output_path):
    """Apply the sketch effect to a video."""
    clip = VideoFileClip(input_path)

    def process_frame(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
        sketched_frame = apply_sketch_effect(frame)
        return cv2.cvtColor(sketched_frame, cv2.COLOR_BGR2RGB)  # Convert back to RGB

    processed_clip = clip.fl_image(process_frame)
    processed_clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

if __name__ == "__main__":
    input_video = "input.mp4"   # Change this to your input video file
    output_video = "output_sketch.mp4"
    
    process_video(input_video, output_video)
