from PIL import Image

def getRed(pixel):
    return pixel[0]

def getGreen(pixel):
    return pixel[1]

def getBlue(pixel):
    return pixel[2]

def moreRed(pixel):
  new_red = getRed(pixel) + 40
  new_green = getGreen(pixel)
  new_blue = getBlue(pixel)

  new_pixel = (new_red, new_green, new_blue)
  return new_pixel

def moreBlue(pixel):
  new_red = getRed(pixel) - 20
  new_green = getGreen(pixel) -20
  new_blue = getBlue(pixel) + 50

  new_pixel = (new_red, new_green, new_blue)
  return new_pixel

def moreGreen(pixel):
  new_red = getRed(pixel)
  new_green = getGreen(pixel) + 50
  new_blue = getBlue(pixel)

  new_pixel = (new_red, new_green, new_blue)
  return new_pixel

def brighten(pixel):
  new_red = getRed(pixel) * 2
  new_green = getGreen(pixel) * 2
  new_blue = getBlue(pixel) * 2

  new_pixel = (new_red, new_green, new_blue)
  return new_pixel

def swap(pixel):
  new_red = getGreen(pixel)
  new_green = getBlue(pixel)
  new_blue = getRed(pixel)

  new_pixel = (new_red, new_green, new_blue)
  return new_pixel

def grayscale(pixel):
  new_red = getRed(pixel)
  new_green = getRed(pixel)
  new_blue = getRed(pixel)
  new_pixel = (new_red, new_green, new_blue)
  return new_pixel

def inversion(pixel):
  new_red = 255 - getRed(pixel)
  new_green = 255 - getGreen(pixel)
  new_blue = 255 - getBlue(pixel) 

  new_pixel = (new_red, new_green, new_blue)
  return new_pixel

print('hello')
shia = Image.open("Shia2.jpg")
bikini = Image.open("Bikini.png")
shia = shia.resize(bikini.size)

new_pixels = []
num_pixels = len(shia.getdata())
pixels = shia.getdata()
print(num_pixels)

ypixels = bikini.getdata()

for i in range(1, num_pixels, 1):
  # if getGreen(pixels[i]) > 200 and 500000 % i != 0 and i != 0:
  #   new_pixel = (255, 0, 0)
  #   new_pixels.append(new_pixel)
  # else:
  #   new_pixel = (0, 0, 255)
  #   new_pixels.append(new_pixel)
  if getGreen(pixels[i]) >= 200:
    new_pixel = (getRed(ypixels[i]), getGreen(ypixels[i]),getBlue(ypixels[i]))
    new_pixels.append(new_pixel)
  else:
    new_pixel = (getRed(pixels[i]), getGreen(pixels[i]), getBlue(pixels[i]))
    new_pixels.append(new_pixel) 

new_image = Image.new("RGB", shia.size)
new_image.putdata(new_pixels)
new_image.save("ShiaBottom.jpg", "JPEG")
