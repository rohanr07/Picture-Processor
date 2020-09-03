#RohanRenganathan

from PIL import Image
from PIL import ImageOps


def chooseFilter(img) :
    print ("Available Filters:")
    print ("-----------------")
    print ("1. Invert Colour")
    print ("2. Gray Scale")
    print ("3. Rotate image")
    print ("4. Flip image")
    print ("5. Exit\n")

    userChoice = int(input ("Please enter your choice (1, 2, 3, 4, 5): "))

    while userChoice != 5 :
        if userChoice == 1 :
            # showing the inverted colour version of the image
            invertedImage = InvertColour(img)
            invertedImage.show()
            saveImage(invertedImage)

        elif userChoice == 2 :
            # showing the Gray Scale version of the image
            grayScaleImage = grayScale(img)
            grayScaleImage.show()
            saveImage(grayScaleImage)

        elif userChoice == 3 :
            # showing the rotated version of the image
            rotatedImage = rotateImage(img)
            rotatedImage.show()
            saveImage(rotatedImage)

        elif userChoice == 4 :
            # showing the image flipped either horizontally or vertically
            flippedImage = flipImage(img)
            flippedImage.show()
            saveImage(flippedImage)

        elif userChoice == 5 :
            exit()

        else :
            print ("Invalid Choice!")
        userChoice = int(input("Please enter your choice (1, 2, 3, 4, 5): "))

# Function opens an image
def OpenImage(file_path, image_name) :
    img = Image.open(file_path + image_name)
    #img.show()
    return img


# Function to save the image
def saveImage(imgToStore) :
    saveRequired = input ("Do you want to save the image? ")

    if saveRequired.lower() == "yes" or saveRequired.lower() == "y" :
        filePath = input("Enter the location where you want to save the new image ")
        imageName = input("Enter the name of the new image ")
        imgToStore.save(filePath + imageName, format = None)
        print ("Your image is saved at " + filePath + imageName + "\n")


# Function for Invert Filter of image
def InvertColour(img) :
    imgInvert = ImageOps.invert(img.convert("RGB"))
    return imgInvert


# Function to Grayscale the image
def grayScale(img) :
    # L - 8 bit pixel black and white
    imgGrayScale = img.convert("L")
    return imgGrayScale


# Function to rotate the image a certain angle specified by the user
def rotateImage(img) :
    rotateDirection = input ("Enter a degree you want to rotate the image ")

    # loop to check if the input value is number
    while not rotateDirection.isdigit() :
        rotateDirection = input("Enter a degree you want to rotate the image (number) ")

    imgRotate = img.rotate(int(rotateDirection))
    return imgRotate


# Function to flip the image either horizontally or vertically
def flipImage(img) :
    flipDirection = input ("How do you want to flip the image: Horizontally OR Vertically... ")


    if (flipDirection.lower() == "horizontal") or (flipDirection.lower() == "horizontally") or (flipDirection.lower() == "h") :
        flippedImage = ImageOps.mirror(img)

    elif (flipDirection.lower() == "vertical") or (flipDirection.lower() == "vertically") or (flipDirection.lower() == "v") :
        flippedImage = ImageOps.flip(img)

    else :
        print ("Invalid Direction!")

    return flippedImage

filePath = input ("Enter the filePath ")
imageName = input ("Enter the name of the image ")


# showing the original image
imgPointer = OpenImage(filePath, imageName)
imgPointer.show()

chooseFilter(imgPointer)





