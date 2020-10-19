#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:56:06 2020
@author: eleve
"""

from PIL import Image

print("Aide:")
print("G<COLOR> generates an image of the given color")
print("<COLOR> keeps the channel of the given image to output image")
print("BW makes black and white image to output image")
print("GS makes a grayscale of the image to output image")
print("OLD makes a filter as it was an olp picture")

image = Image.open("/home/eleve/Bureau/50690360.jpeg")#input("Quel fichier voulez-vous ouvrir?\n"))
outfile = "/home/nicolas/Desktop/out_test.jpg"#input("Quel est le fichier de sortie?\n")
effect = input("Choisissez un effet [RED|GREEN|BLUE|GRED|GGREEN|GBLUE|GS|BW|OLD]: ")


def blueGradient():
    mon_image_bleue = Image.new("RGB",(256,256))
    for i in range (0,256):
        for j in range (0,256):
            mon_image_bleue.putpixel((i,j),(0,0,i))
    return mon_image_bleue

def greenGradient():
    mon_image_verte = Image.new("RGB", (256,256))
    for a in range (0,256):
        for b in range (0,256):
            mon_image_verte.putpixel((a,b),(a,255,a))
    return mon_image_verte

def redGradient():
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
            scaled = ( 0 if (scaled < (256/2)) else 255)
            binded.putpixel((i,j), (scaled, scaled, scaled))
            j+=1
        i+=1
    return binded

def oldImage(img):
    binded = img
    width, height = binded.size
    i = 0
    while i<width:
        j = 0
        while j<height:
            pixel = img.getpixel((i,j))
            scaled = int((pixel[0] + pixel[1] + pixel[2])/3)
            binded.putpixel((i,j), (int((159+scaled)/2), int((85+scaled)/2), int((30+scaled)/2)))
            j+=1
        i+=1
    return binded

def run(inp, out, eff):
    if(eff == "GS"):
        grayScale(inp).show()#.save(out)
    elif eff=="RED":
        redScale(inp).show()#.save(out)
    elif eff=="GREEN":
        greenScale(inp).show()#.save(out)
    elif eff=="BLUE":
        blueScale(inp).show()#.save(out)
    elif eff=="GRED":
        redGradient().show()#.save(out)
    elif eff=="GGREEN":
        greenGradient().show()#.save(out)
    elif eff=="GBLUE":
        blueGradient().show()#.save(out)
    elif eff=="BW":
        BnW(inp).show()#.save(out)
    elif eff=="OLD":
        oldImage(inp).show()
    else:
        print("Unsupported effect!")

run(image, outfile, effect)
