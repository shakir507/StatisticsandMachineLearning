
# Load the image
from PIL import Image
import numpy as np

# Load the image
image_path = '../../../Data/mymnist/six.jpg'
img = Image.open(image_path).convert('L')

# Resize and invert the image
img = img.resize((28, 28))
img = np.invert(img)

# Normalize and reshape the image
img = np.array(img) / 255.0
img = img.reshape(-1, 28*28)
