from PIL import Image

def BlueGradient():
    mon_image_bleue = Image.new("RGB",(256,256))
    for i in range (0,256):
        for j in range (0,256):
            mon_image_bleue.putpixel((i,j),(0,0,i))
    return mon_image_bleue
            
BlueGradient().show()

def GreenGradient():
    mon_image_verte = Image.new("RGB", (256,256))
    for a in range (0,256):
        for b in range (0,256):
            mon_image_verte.putpixel((a,b),(a,255,a))
    return mon_image_verte

GreenGradient().show()
