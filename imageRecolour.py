from PIL import Image

#Functions will replace certain colours in the image saved at the old path
#The edited image will be saved at the new path
oldImagePath = r""
newImagePath = r""


#Replaces any green, red, or yellow pixels (of the specified shades) with blue ones
def replaceWithBlue():
    #The new RGB values for replaced pixels
    R_new, G_new, B_new = (000, 000, 255)
    

    #The image is opened from the old path by Pillow and its pixel data is loaded
    #The load() function will close the image if it is open when the program is run
    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()
    

    #Saves two variables using the "size" tuple which contains the image's horizontal and vertical size in pixels
    width, height = theImage.size
    #Checks the colour of every pixel in the image
    #Replaces all pixels that are any of the specified colours
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (255, 000, 000) or (r, g, b) == (000, 255, 000) 
            or (r, g, b) == (255, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)
                
    
    #Saves the image at the path specified by the newImagePath variable
    theImage.save(newImagePath)
    


 #Replaces any green, blue, or yellow pixels (of the specified shades) with red ones
def replaceWithRed():
    #The new RGB values for replaced pixels
    R_new, G_new, B_new = (255, 000, 000)
    

    #The image is opened from the old path by Pillow and its pixel data is loaded
    #The load() function will close the image if it is open when the program is run
    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()
    

    #Saves two variables using the "size" tuple which contains the image's horizontal and vertical size in pixels
    width, height = theImage.size
    #Checks the colour of every pixel in the image
    #Replaces all pixels that are any of the specified colours
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (000, 000, 255) or (r, g, b) == (000, 255, 000) 
            or (r, g, b) == (255, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)
                
    
    #Saves the image at the path specified by the newImagePath variable
    theImage.save(newImagePath)


#Replaces any blue, red, or yellow pixels (of the specified shades) with green ones
def replaceWithGreen():
    #The new RGB values for replaced pixels
    R_new, G_new, B_new = (000, 255, 000)

    #The image is opened from the old path by Pillow and its pixel data is loaded
    #The load() function will close the image if it is open when the program is run
    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()

    #Saves two variables using the "size" tuple which contains the image's horizontal and vertical size in pixels
    width, height = theImage.size
    #Checks the colour of every pixel in the image
    #Replaces all pixels that are any of the specified colours
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (000, 000, 255) or (r, g, b) == (255, 000, 000) 
            or (r, g, b) == (255, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)
    
    #Saves the image at the path specified by the newImagePath variable
    theImage.save(newImagePath)


#Replaces any blue, red, or green pixels (of the specified shades) with yellow ones
def replaceWithYellow():
    #The new RGB values for replaced pixels
    R_new, G_new, B_new = (255, 255, 000)
    

    #The image is opened from the old path by Pillow and its pixel data is loaded
    #The load() function will close the image if it is open when the program is run
    theImage = Image.open(oldImagePath)
    imagePixels = theImage.load()
    

    #Saves two variables using the "size" tuple which contains the image's horizontal and vertical size in pixels
    width, height = theImage.size
    #Checks the colour of every pixel in the image
    #Replaces all pixels that are any of the specified colours
    for x in range(width):
        for y in range(height):
            r, g, b = imagePixels[x, y]
            if (r, g, b) == (000, 000, 255) or (r, g, b) == (255, 000, 000) 
            or (r, g, b) == (000, 255, 000):
                imagePixels[x, y] = (R_new, G_new, B_new)
                

    #Saves the image at the path specified by the newImagePath variable
    theImage.save(newImagePath)
