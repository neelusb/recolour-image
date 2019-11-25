#!/usr/bin/env python3

# USAGE: ./recolour_img.py INFILE OUTFILE K

from PIL import Image
from collections import Counter
import random, math, sys

outp = ''

OVERRIDE = 2

script, infile, outfile, K = sys.argv

K = int(K)

im = Image.open(infile)
pix = im.load()

print('Opened image (size ' + str(im.size[0]) + 'x' + str(im.size[1]) + ')')

x, y = im.size

pixels = []

for i in range(x):
    for j in range(y):
        pixel = pix[i, j]
        pixels.append(pixel)

print('Read image')

points = pixels
pts = []

n = len(points)

d = len(points[0])

for point in points:
    pt = tuple([float(point[i]) for i in range(d)])
    pts.append(pt)

def distance(a, b):
    sq_dist = 0
    for i, ele in enumerate(a):
        sq_dist += (float(b[i]) - float(a[i])) ** 2

    dist = math.sqrt(sq_dist)

    return dist

def kmeans(pts, k, means):
    global n, d
    try:
        if not means:
            means = []
            indices = random.sample(range(n), k)

            for index in indices:
                means.append(pts[index])

        s_pts = [[] for i in range(k)]

        def sort(pts, means):
            global d
            s_pts = [[] for i in range(k)]

            for pt in pts:
                dist = distance(means[0], pt)
                for i, mean in enumerate(means):
                    dist_new = distance(mean, pt)
                    if dist_new <= dist:
                        dist = dist_new
                        m = i

                s_pts[m].append(pt)

            means = []

            for s_pt in s_pts:

                sums = [0 for i in range(d)]
                for pt in s_pt:
                    for i in range(d):
                        sums[i] += pt[i]

                mns = []

                for sum in sums:
                    mn = sum / len(s_pt)
                    mns.append(mn)

                means.append(mns)

            return (s_pts, means)

        # for i in range(m):
        #     s_pts, means = sort(pts, means)


        s_pts, means = sort(pts, means)

        return (s_pts, means)

    except ZeroDivisionError:
        return None


def valid(type, means, list_of_means, record_of_means):

    global outp

    if type == 'list':
        list = list_of_means

    elif type == 'record':
        list = record_of_means

    if means == list[-2] and means == list[-3] and means == list[-4]:
        return True

    if type == 'list':
        if len(list) >= 10 and means == Counter(list).most_common(1)[0][0]:
            return True

        if OVERRIDE and len(list) >= OVERRIDE + 5 and list.count(means) >= OVERRIDE:
            return True

    if type == 'record':
        if len(list) >= 30 and means == Counter(list).most_common(1)[0][0]:
            return True



    sys.stdout.write('\r' + (' ' * len(outp)) + '\r')

    if type == 'record':
        outp = 'Trial ' + str(len(list_of_means) - 4) + ' Iteration '  + str(len(record_of_means) - 4)

    sys.stdout.write(outp)
    sys.stdout.flush()

    return False

list_of_means = [i for i in range(5)]

means = False

print('---\nK-Means algorithm started')

while not valid('list', means, list_of_means, None):
    outp = ''
    means = False
    record_of_means = [i for i in range(5)]
    while not valid('record', means, list_of_means, record_of_means):
        kmns = kmeans(pts, K, means)
        if kmns:
            s_pts, s_mns = kmns
            mns = []
            for mn in s_mns:
                mean = []
                for dim in mn:
                    mean.append(int(dim))
                mns.append(tuple(mean))
            means = tuple(sorted(mns, key=lambda x: x[0]))
            record_of_means.append(means)
        else:
            means = False
    sys.stdout.write('\r' + (' ' * len(outp)) + '\rTrial ' + str(len(list_of_means) - 4) + ' completed')
    sys.stdout.flush()
    list_of_means.append(means)

sys.stdout.write('\r' + (' ') * len(outp) + '\r')
sys.stdout.flush()

print('K-Means algorithm completed\n---')

colours = s_pts

im = Image.open(infile)
pix = im.load()

x, y = im.size

outp = ''

print('Started writing image')

sys.stdout.write('Written pixel ')

for i in range(x):
    for j in range(y):
        pixel = pix[i, j]
        for k, colour in enumerate(colours):
            if pixel in colour:
                pix[i, j] = means[k]
            sys.stdout.write('\r' + (' ') * len(outp) + '\rWritten pixel ')
            outp = '(' + str(i) + ', ' + str(j) + ')'
            sys.stdout.write(outp)
            sys.stdout.flush()

sys.stdout.write('\r' + (' ') * (len(outp) + 13) + '\r')
sys.stdout.flush()

print('Finished writing image\n---')

print('Image saved to ' + outfile)

im.save(outfile)
