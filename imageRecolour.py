from PIL import Image

oldImagePath = r"c:\Users\Jack\Documents\CodingStuff\Python\ImageRecolouring\blue.png"
newImagePath = r"c:\Users\Jack\Documents\CodingStuff\Python\ImageRecolouring\green.png"

def replaceWithBlue():
    R_new, G_new, B_new = (000, 000, 255)

    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()

    width, height = theImage.size
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (255, 000, 000) or (r, g, b) == (000, 255, 000) or (r, g, b) == (255, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)

    theImage.save(newImagePath)

def replaceWithRed():
    R_new, G_new, B_new = (255, 000, 000)

    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()

    width, height = theImage.size
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (000, 000, 255) or (r, g, b) == (000, 255, 000) or (r, g, b) == (255, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)

    theImage.save(newImagePath)

def replaceWithGreen():
    R_new, G_new, B_new = (000, 255, 000)

    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()

    width, height = theImage.size
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (000, 000, 255) or (r, g, b) == (255, 000, 000) or (r, g, b) == (255, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)

    theImage.save(newImagePath)

def replaceWithYellow():
    R_new, G_new, B_new = (255, 255, 000)

    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()

    width, height = theImage.size
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (000, 000, 255) or (r, g, b) == (255, 000, 000) or (r, g, b) == (000, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)

    theImage.save(newImagePath)

replaceWithGreen()
