from PIL import Image

mns = [
(60.2726543705, 85.0970328789, 66.0617481957), (178.611735331, 195.073657928, 214.187265918)
]

means = []

for mn in mns:
    mean = []
    for dim in mn:
        mean.append(int(dim))
    means.append(tuple(mean))


with open('out.txt', 'r') as f:
    colours = f.read().split('\n')

im = Image.open('img.jpg')
pix = im.load()

x, y = im.size

for i in range(x):
    for j in range(y):
        pixel = pix[i, j]
        for k, colour in enumerate(colours):
            colour = eval('[' + colour + ']')
            print i, j
            if pixel in colour:
                pix[i, j] = means[k]

im.save('new.png')
