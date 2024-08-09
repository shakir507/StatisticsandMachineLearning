# from PIL import Image, ImageEnhance

# # Load the image
# image_path = "../../Data/pentagon.png"#rentanglefield,pentagon
# img = Image.open(image_path)

# # Enhance the color
# enhancer = ImageEnhance.Color(img)
# enhanced_img = enhancer.enhance(0.0)  # Increase color saturation by 50%

# # Save the enhanced image
# enhanced_img.save("../../Data/enhanced_pentagon2.png")

# # Optionally, display the enhanced image
# enhanced_img.show()

from PIL import Image, ImageEnhance

# Load the image
image_path = "../../Data/pentagon.png"  # Replace with your image path
img = Image.open(image_path)

# Enhance the brightness
enhancer = ImageEnhance.Brightness(img)
enhanced_img = enhancer.enhance(3)  # Increase brightness (1.5 is an example value)

# Save the enhanced image
enhanced_img.save("../../Data/enhanced_pentagon2.png")

# Optionally, display the enhanced image
enhanced_img.show()
