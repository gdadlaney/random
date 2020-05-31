from PIL import Image
import os
import random

### Output Parameters ###
tickets = 20  # No. of ticket to be generated

rowsInGame = 3
colsInGame = 3

separatorLength = 10 # in pixels

### Input Parameters ###
topLeft = (42, 138)         # x, y in 4th quadrant
topRight = (408, 138)
bottomRight = (408, 591)
bottomLeft = (42, 591)

def getInputImages(dirPath):
    images = []

    for file in os.listdir(dirPath):
        if file.endswith(".jpg"):
            imagePath = os.path.join(dirPath, file)
            images.append(Image.open(imagePath))
    
    return images

# Scales and pastes images in template
def pasteImagesInTemplate(imagesToPaste, templateName, outFileName):
    template = Image.open(templateName)

    width = int((topRight[0] - topLeft[0])/ colsInGame)
    height = int((bottomLeft[1] - topLeft[1])/ rowsInGame)
    
    for row in range(0, rowsInGame):
        for col in range(0, colsInGame):
            index = colsInGame*row + col
            resizedDimentions = (width - separatorLength,height - separatorLength)
            resizedPic = imagesToPaste[index].resize(resizedDimentions, Image.ANTIALIAS)        # AntiAlias helped to reduce Pixelation
            template.paste(resizedPic, (topLeft[0]+width*col,topLeft[1]+height*row))

    template.save(outFileName)

def shuffleInputImages(inputImages):
    # Shuffling the whole array may be expensive but guarantees no duplication which random.sample() does not
    random.shuffle(inputImages)                         # shuffles the same object.
    return inputImages[:rowsInGame*colsInGame]          # n images in the grid

if __name__ == "__main__":
    inputImages = getInputImages("images/")

    for i in range(1,tickets+1):
        imagesToPaste = shuffleInputImages(inputImages)

        pasteImagesInTemplate(imagesToPaste, templateName='template.jpg', outFileName='output/ticket' + str(i) + '.jpg')
        
        print("Ticket {} Creation Successful!".format(i))
    
    print("Success!")