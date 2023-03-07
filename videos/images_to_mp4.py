import cv2
import os

# Path to input images
image_folder = "./summer_images_test/section1"

# Output video name
video_name = "./summer_images_test/section1/section1.mp4"

# Frame rate for output video
fps = 10

# Target size for resized images
target_size = (1226, 370)

# Get all images from the input folder
images = [img for img in os.listdir(image_folder) if img.endswith(".png")]

# Sort images by filename (assumes image filenames are numbered sequentially)
images = sorted(images, key=lambda x: int(x.split(".")[0]))

# Get image dimensions from first image
img = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = img.shape

# Initialize video writer object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(video_name, fourcc, fps, target_size)

# Loop through all images and write to output video
for image in images:
    img = cv2.imread(os.path.join(image_folder, image))
    resized_img = cv2.resize(img, target_size)
    video.write(resized_img)

# Release video writer object and destroy all windows
cv2.destroyAllWindows()
video.release()
