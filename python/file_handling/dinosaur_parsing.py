from math import sqrt
from collections import OrderedDict
import multiprocessing as mp
import time
from timeit import default_timer as timer

# find speed for bipedal dinosaur, and print it in order
def parse_csv(file, file2):
    g = 9.8
    hash_map = {}
    with open(file, 'r') as f:
        # for line in f.readlines(): only move one item to RAM!!
        # If the file is line-based, the file object is already a lazy generator of lines (like this case)
        for line in f:
            if 'NAME' in line:
                pass
            else:
                name, stride_length, stance = line.split(',')
                if stance.strip() == 'bipedal':
                    hash_map[name] = float(stride_length)
                    # hash_map[name]['stance'] = stance.strip()
    with open(file2, 'r') as f:
        for line in f:
            if 'NAME' in line:
                pass
            else:
                name, leg_length, diet = line.split(',')
                # if name in hash_map.keys():
                if name in hash_map:
                    leg_length = float(leg_length)
                    # hash_map[name]['diet'] = diet.strip()
                    # hash_map[name]['length'] = leg_length
                    hash_map[name] = ((hash_map[name]/leg_length) - 1) * sqrt(leg_length * g)

    return hash_map



#
# #init objects
# pool = mp.Pool(2)
# jobs = []

start = time.time()
start2 = timer()
hash_map = parse_csv('data2.csv', 'data1.csv')
print(hash_map)
print('---------------------------------------------------------------------------------')
ordered_dinos = OrderedDict(sorted(hash_map.items(), key=lambda x: x[1], reverse=False))
print(*(list(ordered_dinos.items())), sep='\n')
print('---------------------------------------------------------------------------------')
print(hash_map.items())
ordered_dinos = sorted(hash_map.items(), key=lambda x: x[1])
print(*ordered_dinos, sep='\n')

# hash_map_list = [{dino: values['speed']} for dino, values in hash_map.items() if 'speed' in values]
# print(hash_map_list)
# print(sorted(hash_map_list, key=lambda i: i['dino_name']))

#wait for all jobs to finish
# for job in jobs:
#     job.get()
# #clean up
# pool.close()

# end = time.time()
# end2 = timer()
# print(end - start)
# print(end2 - start2)


def parse_cleaner(file, file2):
    g = 9.8
    dinos_dict = {}
    with open(file, 'r') as f:
        for line in f:
            if 'NAME' in line:
                pass
            name, stride_length, stance = line.split(',')
            if stance.strip() == 'bipedal':
                dinos_dict[name] = float(stride_length)
    with open(file2, 'r') as f:
        for line in f:
            if 'NAME' in line:
                pass
            name, leg_length, diet = line.split(',')
            if name in dinos_dict.keys():
                leg_length = float(leg_length)
                dinos_dict[name] = ((dinos_dict[name]/leg_length) - 1) * sqrt(leg_length * g)
    return hash_map

