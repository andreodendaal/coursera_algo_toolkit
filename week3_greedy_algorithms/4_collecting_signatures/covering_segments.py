# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    common_points = []

    #write your code here
    segments.sort()

    for s in (segments):
        #points.append(s.start)
        points.append(s.end)

    points.sort()

    for ctr, value in enumerate(points):



    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

# 3 1 3 2 5 3 6 = 1 3
# 4 4 7 1 3 2 5 5 6 = 2 3 6