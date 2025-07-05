import os
os.system('cls')

import PIL.Image

ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

def grayfiy(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return(ascii_str)

def main():
    path = input("Enter the path to the image file:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid image file.")
        return

    new_image_data = pixels_to_ascii(grayfiy(resize_image(image)))
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[i:(i + 100)] for i in range(0, pixel_count, 100)])

    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

    print("ASCII art generated and saved to ascii_image.txt")

if __name__ == "__main__":
    main()