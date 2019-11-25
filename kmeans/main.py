from collections import Counter
import random, math

with open('pix.txt', 'r') as f:
    inp = f.read()
    inp = inp.replace('\n', '')
    inp = inp.replace(' ', '')
    b_points = inp.split(';')

K = 8

OVERRIDE = 8

points = []
pts = []

n = len(b_points)

for point in b_points:
    point = point.replace('(', '')
    point = point.replace(')', '')
    point = point.replace(' ', '')
    point = tuple(point.split(','))
    points.append(point)

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


def valid(type, means, list_of_means):

    if type == 'record':
        if OVERRIDE and len(list_of_means) > OVERRIDE:
            return True

        if means == list_of_means[-2] and means == list_of_means[-3] and means == list_of_means[-4]:
            return True

        if list_of_means.count(means) >= 50:
            return True

        if len(list_of_means) >= 10000 and means == Counter(list_of_means).most_common(1)[0][0]:
            return True

    if type == 'list':
        if OVERRIDE and len(list_of_means) > 5:
            return True
        if means == list_of_means[-2]:
            return True

    print type + ': ' + str(len(list_of_means))

    return False

list_of_means = [i for i in range(5)]

means = False

while not valid('list', means, list_of_means):
    means = False
    record_of_means = [i for i in range(5)]
    while not valid('record', means, record_of_means):
        kmns = kmeans(pts, K, means)
        if kmns:
            s_pts, s_mns = kmns
            mns = [tuple(mean) for mean in s_mns]
            means = tuple(sorted(mns, key=lambda x: x[0]))
            record_of_means.append(means)
        else:
            means = False
    list_of_means.append(means)

outp = ''

outp_grph = ''

for mean in means:
    outp += '('
    for dim in mean:
        outp += str(dim) + ', '
        outp_grph += str(dim) + '   '
    outp = outp[:-2]
    outp += '), '
    outp_grph += '\n'

outp = outp[:-2]

outp_file = ''

print outp

for s_pt in s_pts:
    for pt in s_pt:
        outp_file += '('
        for dim in pt:
            outp_file += str(dim) + ', '
        outp_file = outp_file[:-2]
        outp_file += '), '
    outp_file = outp_file[:-2] + '\n'

print 1

with open('out.txt', 'w') as f:
    f.write(outp_file)

with open('out_grph.txt', 'w') as f:
    f.write(outp_grph)
