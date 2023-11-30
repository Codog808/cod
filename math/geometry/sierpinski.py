from PIL import Image, ImageDraw

# img = Image.new("RGB", (300, 300), "blue")
# img.show()
def sierpinski(draw, x1, y1, x2, y2, x3, y3, depth):
    if depth == 0:
        draw.polygon([(x1, y1), (x2, y2), (x3, y3)], outline="black", fill="black")
    else:
        # Calculate the midpoint of each side of the triangle
        mx1, my1 = (x1 + x2) / 2, (y1 + y2) / 2
        mx2, my2 = (x2 + x3) / 2, (y2 + y3) / 2
        mx3, my3 = (x1 + x3) / 2, (y1 + y3) / 2

        # Recursively draw the smaller triangles
        sierpinski(draw, x1, y1, mx1, my1, mx3, my3, depth - 1)
        sierpinski(draw, x2, y2, mx1, my1, mx2, my2, depth - 1)
        sierpinski(draw, x3, y3, mx2, my2, mx3, my3, depth - 1)

def create_image(size, depth):
    # Create a blank white image
    img = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(img)

    # Define the 3 vertices of the triangle
    x1, y1 = 0, size
    x2, y2 = size, size
    x3, y3 = size / 2, 0

    sierpinski(draw, x1, y1, x2, y2, x3, y3, depth)

    return img

# Create and save the image
img = create_image(256, 3)  # Size = 512x512, Depth = 4
img.save("sierpinski_triangle.png")
img.show()
