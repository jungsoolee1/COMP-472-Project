# This file is for the data visualization. Running this script will create a bar graph to show the number of images in
# each class. It will also create a histogram for each class that will show the aggregated pixel intensities. It will
# also create pixel intensity histograms of 15 randomly sampled images of each class.

import os
import matplotlib.pyplot as plt
from PIL import Image
import random


# Method for bar graph creation of the different classes
def classDistribution(dataset):
    classes = ['angry', 'happy', 'engaged', 'neutral']
    # list of paths for the folders
    directories = [f'../dataset-cleaned/{expression}' for expression in classes]

    # Find nb of images in each class
    nb_images = [len(os.listdir(dir)) for dir in directories]

    # Create bar graph
    plt.figure()
    plt.bar(classes, nb_images)
    plt.xlabel('Class of Images')
    plt.ylabel('Number of Images')
    plt.title(f'Number of Images in each Class for {dataset} Dataset')
    plt.show()

# Method to create histograms of the pixel intensities of the different classes
def pixelIntensityDistribution(dataset):
    classes = ['angry', 'happy', 'engaged', 'neutral']
    # For the colors of the histograms
    colors = ['red', 'green', 'blue', 'gray']
    # list of paths for the folders
    directories = [f'../dataset-cleaned/{expression}' for expression in classes]

    plt.figure(figsize=(10, 10))

    # Loop over each class
    for i, dir in enumerate(directories):
        # To keep track of the aggregated pixel intensities
        pixels = []

        # Loop over each image
        for file_name in os.listdir(dir):
            # Get the image
            img = Image.open(os.path.join(dir, file_name))
            
            # Extra measure to check if image is in grayscale
            if img.mode != 'L':
                img = img.convert('L')

            # Get the pixel intensities of the image and add it to the array.
            pixels.extend(list(img.getdata()))

        # Histogram for the class
        plt.subplot(2, 2, i + 1)
        plt.hist(pixels, color=colors[i], bins=256)
        plt.title(f'{classes[i]} in {dataset}')
        plt.xlabel('Aggregated Pixel Intensity')
        plt.ylabel('Frequency')

    # Show the plot
    plt.show()


# Method to show pixel intensity distribution for 15 randomly sampled images of each class
def sampleImages(dataset):
    classes = ['angry', 'happy', 'engaged', 'neutral']
    #list of paths for the folders
    directories = [f'../dataset-cleaned/{expression}' for expression in classes]

    for number, dir in enumerate(directories):
        fig, axes = plt.subplots(5, 6, figsize=(30, 16))
        #coordinates for figure grid
        i = 0
        j = 0
        image_names = os.listdir(dir)
        # Select 15 random images
        rand_images = random.sample(image_names, 15)

        for image_name in rand_images:
            # Obtain the image
            img = Image.open(os.path.join(dir, image_name))
            # Get histogram of image
            histogram = img.histogram()

            # Plot histogram with image
            axes[i, 2*j].imshow(img, cmap='gray')
            axes[i, 2*j].axis('off')
            axes[i, 2*j+1].bar(range(256), histogram)

            # Increment coordinates
            if j < 2:
                j += 1
            else:
                j = 0
                i += 1

        fig.suptitle(f'Pixel Intensity for {classes[number]} sample images in {dataset} dataset')
    plt.show()


classDistribution('train')
pixelIntensityDistribution('train')
sampleImages('train')
