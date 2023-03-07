from PIL import Image
import os

# set the directory path
dir_path = './summer_images_test/section2'

# loop through all images in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.png'):  # check if the file is a JPEG image
        # open the image using Pillow
        img = Image.open(os.path.join(dir_path, filename))
        
        # resize the image to the same size
        new_size = (800, 600)
        img = img.resize(new_size)
        
        # save the image as BMP
        new_filename = os.path.splitext(filename)[0] + '.bmp'
        img.save(os.path.join(dir_path, new_filename), 'BMP')
  