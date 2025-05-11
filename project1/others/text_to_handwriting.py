

from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting():
    # Text to convert to handwriting
    # # Open the file in read mode
    # file_path = "abc.txt"
    # file = open(file_path, "r")

    # # Read the contents of the file
    # text = file.read()

    # # Close the file
    # file.close()

    # # Print the contents of the file
    # print(text)

    text=input("Enter Your text : -->>")

    # Path to the font file (you can change this to the path of your desired handwriting font)
    font_path = "Myfont-Regular.ttf"

    # Font size
    font_size = 80

    # Padding around the text (optional)
    padding = 20

    # Color of the text (black by default)
    text_color = (0, 0, 0)  # RGB color tuple

    # Determine the width and height of the image based on the text and font size
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = font.getsize(text)

    # Add padding to the image size
    image_width = text_width + 2 * padding
    image_height = text_height + 2 * padding

    # Create a new image with a white background
    image = Image.new("RGB", (image_width, image_height), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Calculate the position to center the text
    x = (image_width - text_width) / 2
    y = (image_height - text_height) / 2

    # Draw the text on the image
    draw.text((x, y), text, font=font, fill=text_color)

    # Save the image
    image.save("handwriting.png")


while True:
    text_to_handwriting()












