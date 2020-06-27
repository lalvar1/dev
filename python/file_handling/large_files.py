import time
import sys
from timeit import default_timer as timer

# pypy is the fastest, faster than cpython
# data = sys.stdin.readlines()
# n, k = map(int, input().split())
# n, k = map(int, next(sys.stdin).split())

# print "Counted", len(data), "lines."
start = time.time()
start2 = timer()
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print(list(result))
numbers = '1234'
result = map(int, numbers)
print(list(result))

with open(file, 'r') as f:
    while True:
        read_data = f.read(chunksize)
        if not read_data:
            break
        for line in read_data:
            process_line()

# nicer way to do it

def read_in_chunks(file, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        yield data


with open('really_big_file.dat') as f:
    for piece in read_in_chunks(f):
        for line in piece:
            process_line()




end = time.time()
end2 = timer()
print('elepsed time: {}'.format(end-start))
print('elepsed time: {}'.format(end2-start2))
