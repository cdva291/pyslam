import cv2
import os

# Path to input images
image_folder = "./Szene_2/img"

# Output video name
video_name = "./Szene_2/img/spring.mp4"

# Frame rate for output video
fps = 90

# Get all images from the input folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

# Sort images by filename (assumes image filenames are numbered sequentially)
images = sorted(images, key=lambda x: int(x.split(".")[0].zfill(4)))

# Initialize video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Loop through all images and write to output video
for image in images:
    img = cv2.imread(os.path.join(image_folder, image))
    resized_img = cv2.resize(img, (1226, 370))  # Resize image to 1226x370
    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    if image == images[0]:  # Get image dimensions from first image
        height, width = gray.shape
        video = cv2.VideoWriter(video_name, fourcc, fps, (width, height), 0)
    video.write(gray)

# Release video writer object and destroy all windows
cv2.destroyAllWindows()
video.release()