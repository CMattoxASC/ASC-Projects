from Myro import *
pic = makePicture(pickAFile())
getPixels(pic)

ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)

for pixel in getPixels(pic):
    gray = getGray(pixel)
    if gray > 180:
        setColor(pixel,ObamaYellow)
    elif gray > 120:
        setColor(pixel, ObamaBlue)
    elif gray > 60:
        setColor(pixel, ObamaRed)
    else:
        setColor(pixel, ObamaDarkBlue)
show(pic)
