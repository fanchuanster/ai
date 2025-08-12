import math
from collections import Counter
from itertools import permutations, combinations, chain
import heapq
from collections import deque, defaultdict,
def min_cable(states, dists):

    dist_states = zip(dists, states)

    consolidated_dists = []
    off_list = []
    for dist, state in dist_states:
        if state == 1:
            if off_list:
                consolidated_dists.append(off_list)
                off_list = []
            consolidated_dists.append(dist)
        elif state == 0:
            off_list.append(dist)
    if off_list:
        consolidated_dists.append(off_list)

    total_length = 0
    for i, v in enumerate(consolidated_dists):
        min_distance = float("inf")
        if isinstance(v, list):
            if i-1 >= 0:
                min_distance = min(min_distance, v[0]-consolidated_dists[i-1])
            if i+1 < len(consolidated_dists):
                min_distance = min(min_distance, consolidated_dists[i+1]-v[-1])
            total_length += min_distance + v[-1] - v[0]

    return total_length

