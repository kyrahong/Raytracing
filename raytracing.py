# Pixel march function

import numpy as np
from PIL import Image

def create_image(width, height):
    # Create an array to hold the pixel data
    image_data = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Iterate over each pixel
    for y in range(height):
        for x in range(width):
            # Generate a simple gradient color based on pixel position
            r = int(255 * (x / width))
            g = int(255 * (y / height))
            b = 128  # constant blue value for simplicity
            image_data[y, x] = [r, g, b]
    
    # Create and save the image using PIL
    image = Image.fromarray(image_data, 'RGB')
    image.save('gradient.png')

# Define image dimensions
width = 800
height = 400

# Create the image
create_image(width, height)

# Object (Sphere) Intersection
import numpy as np
from PIL import Image

def hit_sphere(center, radius, ray_origin, ray_direction):
    oc = ray_origin - center
    a = np.dot(ray_direction, ray_direction)
    b = 2.0 * np.dot(oc, ray_direction)
    c = np.dot(oc, oc) - radius * radius
    discriminant = b * b - 4 * a * c
    return discriminant > 0

def color(ray_origin, ray_direction):
    # Sphere details
    center = np.array([0, 0, -1])
    radius = 0.5
    
    if hit_sphere(center, radius, ray_origin, ray_direction):
        return np.array([255, 0, 0])  # Red color for the sphere
    
    unit_direction = ray_direction / np.linalg.norm(ray_direction)
    t = 0.5 * (unit_direction[1] + 1.0)
    return (1.0 - t) * np.array([255, 255, 255]) + t * np.array([127, 178, 255])

def create_image(width, height):
    image_data = np.zeros((height, width, 3), dtype=np.uint8)
    
    # Camera setup
    lower_left_corner = np.array([-2.0, -1.0, -1.0])
    horizontal = np.array([4.0, 0.0, 0.0])
    vertical = np.array([0.0, 2.0, 0.0])
    origin = np.array([0.0, 0.0, 0.0])
    
    for y in range(height):
        for x in range(width):
            u = x / width
            v = (height - y - 1) / height  # Flip y-axis
            direction = lower_left_corner + u * horizontal + v * vertical
            pixel_color = color(origin, direction)
            image_data[y, x] = np.clip(pixel_color, 0, 255)
    
    image = Image.fromarray(image_data, 'RGB')
    image.save('sphere.png')

width = 800
height = 400
create_image(width, height)

