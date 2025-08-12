# AZ
from collections import Counter

def getTargetCount(nums):
    if len(nums) <= 2: return 0
    # improvement: use min & max instead of sort
    sorted_nums = sorted(nums)
    min_num = sorted_nums[0]
    max_num = sorted_nums[-1]
    # improvement: count accurance of min and max instead of statistics on all
    statistics = Counter(sorted_nums)
    return len(nums) - statistics[min_num] - statistics[max_num]

if __name__ == "__main__":
    a1 = [11,7,2,15]
    a2 = [-3,3,3,90]
    res = getTargetCount(a1)
    assert(res == 2)
    print(res)
    
    res = getTargetCount(a2)
    assert(res == 2)
    print(res)