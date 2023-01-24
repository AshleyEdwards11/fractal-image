from PIL import Image
import random

# Define the size of the image
width = 800
height = 800

# Create a new image with a white background
image = Image.new("RGB", (width, height), "white")
pixels = image.load()

# Define the properties of the fractal
xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
max_iter = 256

# Generate the fractal
for x in range(width):
    for y in range(height):
        zx, zy = x * (xmax - xmin) / (width - 1) + xmin, y * (ymax - ymin) / (height - 1) + ymin
        c = zx + zy * 1j
        z = c
        for i in range(max_iter):
            if abs(z) > 2.0:
                break 
            z = z * z + c

        # Color the pixel based on the number of iterations
        r, g, b = i % 8 * 32, i % 16 * 16, i % 32 * 8
        pixels[x, y] = (r, g, b)

# Generate a random hue shift
hue_shift = random.randint(0, 359)

# Apply the hue shift to the image
image = image.convert("HSV")
data = list(image.getdata())
image.putdata([(hue, s, v) if (hue + hue_shift) % 255 != 0 else (hue, 0, 0) for (hue, s, v) in data])
image = image.convert("RGB")

# Save the image
image.save("fractal.png")
