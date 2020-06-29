# insert interval, merge if an intersection exists


def insert2(new_interval, intervals):
    new_min_arrays, i = [], 0
    for i, it in enumerate(intervals):
        if new_interval[1] < it[0]:      # is minor case
            i -= 1
            break
        elif it[1] < new_interval[0]:       # is major/ after_this case
            new_min_arrays += it
        else:
            new_interval[0], new_interval[1] = min(it[0], new_interval[0]), max(it[1], new_interval[1])  # merge case
    return new_min_arrays + [new_interval] + intervals[i + 1:]

print(insert2([4,8],[[1,2],[3,5],[6,7],[8,10],[12,16]]))
#print(insert_new([6,8], [[1,5]]))
print(insert2([0, 0], [[1, 5]]))

# nice case to apply recursion...




















