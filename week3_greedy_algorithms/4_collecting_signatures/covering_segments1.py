# Uses python3
import sys
from collections import namedtuple
import operator

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    common_points = []
    full_segments = []

    #write your code here
    segments.sort(key=operator.itemgetter(0))

    for s in segments:
        sub_segment = []
        value = s.start
        while value <= s.end:
            sub_segment.append(value)
            value += 1
        full_segments.append(sub_segment)

    full_segments.sort(key=operator.itemgetter(0))

    for cur, nxt in zip(full_segments, full_segments[1:]):
        s_cur = set(cur)
        s_nxt = set(nxt)
        intersect = s_cur.intersection(s_nxt)
        l_intersect = list(intersect)
        if points:
            appnd = True

            for elem in l_intersect:
                if elem in points:
                    appnd = False

            if appnd and l_intersect:
                points.append(max(l_intersect))

        else:
            # Add first link
            points.append(max(l_intersect))


    points.sort()

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

# 100 41 42 52 52 63 63 80 82 78 79 35 35 22 23 31 32 44 45 81 82 36 38 10 12 1 1 23 23 32 33 87 88 55 56 69 71 89 91 93 93 38 40 33 34 14 16 57 59 70 72 36 36 29 29 73 74 66 68 36 38 1 3 49 50 68 70 26 28 30 30 1 2 64 65 57 58 58 58 51 53 41 41 17 18 45 46 4 4 0 1 65 67 92 93 84 85 75 77 39 41 15 15 29 31 83 84 12 14 91 93 83 84 81 81 3 4 66 67 8 8 17 19 86 87 44 44 34 34 74 74 94 95 79 81 29 29 60 61 58 59 62 62 54 56 58 58 79 79 89 91 40 42 2 4 12 14 5 5 28 28 35 36 7 8 82 84 49 51 2 4 57 59 25 27 52 53 48 49 9 9 10 10 78 78 26 26 83 84 22 24 86 87 52 54 49 51 63 64 54 54
# = 43
# 1 4 5 8 9 10 14 15 18 23 26 28 29 30 32 34 35 36 40 41 44 46 49 52 54 56 58 61 62 63 65 67 70 74 77 78 79 81 84 87 91 93 95
#M
# 1 2 4 8   10 14 15 18 23 26 27 29 32 33 34 35 36 38 40 41 42 44 49 51 52 54 58 63 64 65 67 70 74 78 79 81 82 84 87 91 93
#https://rosettacode.org/wiki/Largest_int_from_concatenated_ints#Python:_Sort_on_comparison_of_concatenated_ints_method