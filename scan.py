# import the necessary packages
import re
from PIL import Image
import pytesseract
from pathlib import Path
from pdf2image import convert_from_path


# start the timer to measure the time it takes to process all of the images
import time
start = time.time()



def grayscale_image(image):
    # convert the pillow image to grayscale
    return image.convert("L")



# check if in the data folder there are any pdfs
# if there are, convert them to images
pdfs = Path("data").rglob("*.pdf")

# check if the generator is empty

for f in pdfs:
    if f is None:
        break
    images = convert_from_path(f'{f}')
    for i, image in enumerate(images):
        image.save(f'images/{f.stem}_{i}.jpg', 'JPEG')


    # copy all images in the data folder to the images folder
    images = Path("data").rglob("*.jpg")
    for f in images:
        shutil.copy(f, "images")
    images= Path("data").rglob("*.png")
    for f in images:
        shutil.copy(f, "images")
    images = Path("data").rglob("*.jpeg")
    for f in images:
        shutil.copy(f, "images")


# collect all files in the images folder
images = Path("images").rglob("*.*")

# List of available languages
print(pytesseract.get_languages(config=''))

# iterate over all of the images
for f in images:
    # load the image as a PIL/Pillow image, apply OCR, and then store the text in a file
    print(f"Processing {f}")
    text = pytesseract.image_to_string(Image.open(f).convert("L"), lang="deu")
    
    # remove the line breaks if there are more than 2 directly behind each other
    text = re.sub(r'(\n){2,}', '', text)


    # write the text to a file
    with open(f"output/{f.stem}.txt", "w") as file:
        file.write(text)

print("Done!")

# print the time it took to process all of the images
print(f"Time: {time.time() - start}")


# 1864 seconds = 31 minutes