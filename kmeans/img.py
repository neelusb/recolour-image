from PIL import Image

im = Image.open('img.jpg')
pix = im.load()

x, y = im.size

pixels = []

for i in range(x):
    for j in range(y):
        pixel = pix[i, j]
        pixels.append(pixel)

outp = ''

for pixel in pixels:
    outp += str(pixel[0]) + '   ' + str(pixel[1]) + '   ' + str(pixel[2]) + '\n'

outp = outp[:-1]

with open('pix.txt', 'w') as f:
    f.write(str(outp))
