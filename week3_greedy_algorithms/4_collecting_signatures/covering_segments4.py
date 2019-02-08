# Uses python3
import sys
from collections import namedtuple
import operator

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    full_segments = []
    #write your code here
    segments.sort(key=operator.itemgetter(0))
    # load first

    for s in segments:
        # load 2nd
        sub_segment = list(range(s.start, s.end + 1))
        full_segments.append(sub_segment)

    # full_segments.sort(key=operator.itemgetter(0))

    header = []
    hdr_header = []
    for cur, nxt in zip(full_segments, full_segments[1:]):
        # check common elements still connect segments. If not choose one and store
        if not header:
            for elem in cur:
                if elem in nxt:
                    header.append(elem)
            if not header:
                points.append(max(cur))

        else:
            for h in header:
                if h in nxt:
                    hdr_header.append(h)

            if hdr_header:
                header = hdr_header[:]
                hdr_header = []
            else:
                points.append(max(header))
                header = []

        # drop cur
    # process last segment
    if header:
        # last link
        points.append(max(header))
    else:
        # no link, last segment on its own
        points.append(max(nxt))

    #points.sort()

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

#

# = 43
# 1 4 5 8 9 10 14 15 18 23 26 28 29 30 32 34 35 36 40 41 44 46 49 52 54 56 58 61 62 63 65 67 70 74 77 78 79 81 84 87 91 93 95
# 1 4   8   10 14    18 23 26 29       32 34 35 36 40 41 44    49 52 54    58       63 65 67 70 74 78 79    81 84 87 91 93
#M
# 1 2 4 8   10 14 15 18 23 26 27 29 32 33 34 35 36 38 40 41 42 44 49 51 52 54 58 63 64 65 67 70 74 78 79 81 82 84 87 91 93
#https://rosettacode.org/wiki/Largest_int_from_concatenated_ints#Python:_Sort_on_comparison_of_concatenated_ints_method