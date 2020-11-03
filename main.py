#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:56:06 2020
@author: eleve
"""

from PIL import Image


def getHelp():
    """Prints program help for the user"""
    print("\n---------Help----------")
    print(" |- G<COLOR> generates an image of the given gradient color")
    print(" |    |- RED")
    print(" |    |- GREEN")
    print(" |    +- BLUE")
    print(" |- <COLOR>  keeps the channel of the given image to output image")
    print(" |    |- RED")
    print(" |    |- GREEN")
    print(" |    +- BLUE")
    print(" |- BW       makes black and white image to output image")
    print(" |- GS       makes a grayscale of the image to output image")
    print(" |- OLD      makes a filter as it was an old picture")
    print(" +- TNO      applies Teal and Orange filter to the image")
    print("-----------------------\n")

def blueGradient():
    """Generates a gradient as: Black > Blue > White"""
    mon_image_bleue = Image.new("RGB",(256,256))
    for i in range (0,256):
        for j in range (0,256):
            mon_image_bleue.putpixel((i,j),(0,0,i))
    return mon_image_bleue

def greenGradient():
    """Generates a gradient as: Black > Green > White"""
    mon_image_verte = Image.new("RGB", (256,256))
    for a in range (0,256):
        for b in range (0,256):
            mon_image_verte.putpixel((a,b),(a,255,a))
    return mon_image_verte

def redGradient():
    """Generates a gradient as: Black > Red > White"""
    img = Image.new("RGB",(256,256))
    #Set the black to red
    i = 0
    while i<(256/2):
        j = 0
        while j<(256):
            img.putpixel((i, j), (int((i*2)), 0, 0))
            j+=1
        i+=1
    #Set the red to white!
    i = int(256/2)
    f = 0
    while i<(256):
        j = 0
        while j<(256):
            img.putpixel((i, j), (int(255), int(f*2), int(f*2)))
            j+=1
        i+=1
        f+=1
    return img

def redScale(img):
    """Pass Image type as param, it'll be returned as binded to RED scale"""
    binded = img
    width, height = binded.size
    i=0
    while i<width:
        j=0
        while j<height:
            binded.putpixel((i,j), (img.getpixel((i,j))[0], 0, 0))
            j+=1
        i+=1
    return binded

def greenScale(img):
    """Pass Image type as param, it'll be returned as binded to RED scale"""
    binded = img
    width, height = binded.size
    i=0
    while i<width:
        j=0
        while j<height:
            binded.putpixel((i,j), (0, img.getpixel((i,j))[1], 0))
            j+=1
        i+=1
    return binded

def blueScale(img):
    """Pass Image type as param, it'll be returned as binded to RED scale"""
    binded = img
    width, height = binded.size
    i=0
    while i<width:
        j=0
        while j<height:
            binded.putpixel((i,j), (0, 0, img.getpixel((i,j))[2]))
            j+=1
        i+=1
    return binded

def grayScale(img):
    """Pass Image type as parameter, it'll be returned as binded to GS"""
    binded = img
    width, height = binded.size
    i=0
    while i<width:
        j=0
        while j<height:
            pixel = img.getpixel((i,j))
            scaled = int((pixel[0] + pixel[1] + pixel[2])/3)
            binded.putpixel((i,j), (scaled, scaled, scaled))
            j+=1
        i+=1
    return binded

def BnW(img):
    """Pass Image type as param, it'll be returned as binded to Black & White"""
    binded = img
    width, height = binded.size
    i = 0
    while i<width:
        j = 0
        while j<height:
            pixel = img.getpixel((i,j))
            scaled = int((pixel[0] + pixel[1] + pixel[2])/3)
            #Filter to know if it have to be B or W
            scaled = ( 0 if (scaled < (256/2)) else 255)
            binded.putpixel((i,j), (scaled, scaled, scaled))
            j+=1
        i+=1
    return binded

def oldImage(img):
    """Function oldImage returns the input image with a sepia filter
    img is of type PIL.Image.Image"""
    binded = img
    width, height = binded.size
    i = 0
    while i<width:
        j = 0
        while j<height:
            pixel = img.getpixel((i,j))
            #Needs to make an average to have a proper gray scale
            scaled = int((pixel[0] + pixel[1] + pixel[2])/3)
            #Add the color values to get the sepia effect
            binded.putpixel((i,j), (int((159+scaled)/2), int((85+scaled)/2), int((30+scaled)/2)))
            j+=1
        i+=1
    return binded

def TnO(img):
    """Applyes the Teal & Orange effect from the input image and is returned"""
    #The range in which the color is considered as white (pad*2)
    pad = 5
    binded = img
    width, height = binded.size
    
    
    i = 0
    while i<width:
        j = 0
        while j<height:
            pixel = img.getpixel((i,j))
            blue = pixel[2]
            green = pixel[1]
            red = pixel[0]
            match = 0
            shouldSkip = False
            
            #Filter the pixel color to know if it in the same range
            if pixel[2]<pixel[1]:
                if pixel[1]<pixel[0]:
                    match = pixel[0]
                    if (pixel[1]<match+pad and pixel[1]>match-pad and pixel[2]<match+pad and pixel[2]>match-pad) == True:
                        shouldSkip = True
                else:
                    match = pixel[1]
                    if (pixel[2]<match+pad and pixel[2]>match-pad and pixel[0]<match+pad and pixel[0]>match-pad) == True:
                        shouldSkip = True
            else:
                if pixel[2]<pixel[0]:
                    match = pixel[0]
                    if (pixel[1]<match+pad and pixel[1]>match-pad and pixel[2]<match+pad and pixel[2]>match-pad) == True:
                        shouldSkip = True
                else:
                    match = pixel[2]
                    if (pixel[1]<match+pad and pixel[1]>match-pad and pixel[0]<match+pad and pixel[0]>match-pad) == True:
                        shouldSkip = True
            
            #If the pixel value range was correct, we skip it
            if shouldSkip == False:
                #Check blue color to make it higher
                #[TODO] fix the blue which isn't good enough
                if pixel[2]>150:
                    blue = int(pixel[2]+70)
                    if pixel[1]>60 and pixel[1]<200:
                        green = pixel[1]+40
                #Check the red to make orange if it's not good enough
                if pixel[0]>60 and pixel[0]<200:
                     red = int(((pixel[0]*100/256)+10)*256/100)
                binded.putpixel((i,j), (red, green, blue))
            j+=1
        i+=1
    return binded

def MirrorPic(mirror_pic):
    """Function MirrorPic flips the picture"""
    return mirror_pic.transpose(Image.FLIP_LEFT_RIGHT)

def applyEffect(inp):
    """Lets the user choose the effect to apply on the input image and returns the image with the effect applied."""
    eff = input("Choose the effect you want: [RED|GREEN|BLUE|GRED|GGREEN|GBLUE|GS|BW|OLD|MIR|TNO] \n")
    #Parse input to know which effect is to be used
    if(eff == "GS"):
        return grayScale(inp)
    elif eff=="RED":
        return redScale(inp)
    elif eff=="GREEN":
        return greenScale(inp)
    elif eff=="BLUE":
        return blueScale(inp)
    elif eff=="GRED":
        return redGradient()
    elif eff=="GGREEN":
        return greenGradient()
    elif eff=="GBLUE":
        return blueGradient()
    elif eff=="BW":
        return BnW(inp)
    elif eff=="OLD":
        return oldImage(inp)
    elif eff=="TNO":
        return TnO(inp)
    elif eff=="MIR":
        return MirrorPic(inp)
    else:
        print("Unsupported effect!")
        return applyEffect(inp)

def askContinue():
    """Used to ask the user is he wants or not, otherwise maybe get help. Generates a loop if nothing clear was given in waiting of a valid answer."""
    data = input("Do you want to continue or get some help? [Y/N/H] ")
    if data == "Y":
        return True
    elif data == "N":
        return False
    elif data == "H":
        getHelp()
        return askContinue()
    else:
        return askContinue()

def requestInputFile():
    """Asks the user for a (valid) input image that is returned. Generates a loop in waiting of a valid file"""
    inputfile = input("Which file do you want as input?\n")
    try:
        return Image.open(inputfile)
    except FileNotFoundError:
        print("Error, the file doesn't exists!")
        return requestInputFile()

def main():
    """Program main loop"""
    close = False
    while close == False:
        close = not askContinue()
        if close == False:
            image = requestInputFile()
            outfile = input("Which file do you want as output?\n")
            image = applyEffect(image)
            print("Saving file...")
            image.save(outfile)

main()
