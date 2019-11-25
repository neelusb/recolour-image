import random

e = 50
n = 50

centres = [
    [0, 20, 200, 400, 350],
    [-100, 30, 100, 0, 40],
    [-30, 40, 30, 0, -600]
]

d = len(centres)

s_pts = [[random.sample(range(centres[j][i] - e, centres[j][i] + e), n) for j in range(d)] for i in range(len(centres[0]))]

outp = ''

points_sets = []

for points in s_pts:

    points_set = []

    for i in range(n):
        point = [points[j][i] for j in range(d)]
        points_set.append(point)

    points_sets.append(points_set)

outp = ''

all_pts = []

for pts in points_sets:
    for pt in pts:
        outp += '('
        for dim in pt:
            outp += str(dim) + ', '
        outp = outp[:-2]
        outp += '), '
        all_pts.append(pt)
    outp = outp[:-2] + '\n'

outp += '\n'

outp_file = ''

outp_grph = ''


for pt in all_pts:
    outp_file += '('
    outp += '('
    for dim in pt:
        outp_file += str(dim) + ','
        outp += str(dim) + ', '
        outp_grph += str(dim) + '   '
    outp_file = outp_file[:-1]
    outp = outp[:-2]
    outp_file += ');'
    outp += '), '
    outp_grph += '\n'

outp_file = outp_file[:-1] + '\n'

# for pt in all_pts:
#     outp_file += '(' + str(pt[0]) + ',' + str(pt[1]) + ');'
#     outp += '(' + str(pt[0]) + ', ' + str(pt[1]) + '), '

outp = outp[:-2]


with open('in.txt', 'w') as f:
    f.write(outp_file)

with open('in_grph.txt', 'w') as f:
    f.write(outp_grph)

print(outp)
