import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def apply_sketch_effect(frame):
    """Convert a frame to a pencil sketch."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    inverted = cv2.bitwise_not(gray)
    blurred = cv2.GaussianBlur(inverted, (21, 21), sigmaX=0, sigmaY=0)
    inverted_blur = cv2.bitwise_not(blurred)
    sketch = cv2.divide(gray, inverted_blur, scale=256.0)
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

def blend_with_original(original_frame, sketch_frame, alpha=0.15):
    """Blend the original frame with the sketch effect frame using alpha transparency."""
    return cv2.addWeighted(original_frame, alpha, sketch_frame, 1 - alpha, 0)

def process_video(input_path, output_path):
    """Apply the sketch effect and overlay the original video with 15% transparency."""
    clip = VideoFileClip(input_path)

    def process_frame(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Convert to OpenCV format
        sketch_frame = apply_sketch_effect(frame)
        blended_frame = blend_with_original(frame, sketch_frame, alpha=0.15)
        return cv2.cvtColor(blended_frame, cv2.COLOR_BGR2RGB)  # Convert back to RGB

    processed_clip = clip.fl_image(process_frame)
    processed_clip.write_videofile(output_path, codec="libx264", fps=clip.fps)

if __name__ == "__main__":
    input_video = "input.mp4"
    output_video = "output_sketch.mp4"
    process_video(input_video, output_video)
