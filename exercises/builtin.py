import heapq
import itertools
from functools import reduce, lru_cache
import math
import bisect

def main():
    l = [3,8,4,5,100,1]
    l2 = [13,78,34,15,1100,-11]
    # print("nsmallest 3", heapq.nsmallest(3, l))
    # print("nlargest 3", heapq.nlargest(3, l))

    # heapq.heappush(l, 102)
    # heapq.heappush(l, 99)
    # heapq.heappush(l, 103)
    # heapq.heappush(l, 2)

    # iter = heapq.merge(sorted(l), sorted(l2))
    # for i in iter:
    #     print(i)

    # print([i for i in itertools.combinations(l, 3)])
    # print([i for i in itertools.permutations(l, 3)])
    # print(itertools.permutations(l, 3))
    # itertools.chain(l,l2)
    # print([i for i in itertools.chain(l,l2)])
    # print(l + l2)
    # print([i for i in ])


    # nums = [12, 18, 9]
    # result = reduce(math.gcd, nums)
    # print(result)  # Output: 3

    # x = 2.63
    # print("round",x,round(x))
    # print("ceil",math.ceil(x))

    # count = itertools.count(9)
    # for i in range(10):
    #     print(next(count))

    # print("factorial(3)",math.factorial(3))
    # print("sqrt(3)",math.sqrt(3)**2==3, math.sqrt(4)**2==4)
    # print("pow(3,4)",math.pow(3,4))


    arr = [1, 3, 4, 4,0, 5, 6]
    # print([i for i in reversed(arr)])
    # rarr = arr[::-1]
    # print([i for i in zip(arr,rarr,rarr)])
    # arr = map(lambda x:x+1, arr)
    # print(arr)
    # s = "abc"
    # print(s.index("c"))
    # i = 10
    # if True:
    #     j = 120
    # print(j)

    # print("" == None)
    # print("" is None)

    # class base:
    #     def aaa(self,n=3):
    #         print("aaa in base",n)
    #     def aaa1(self,n=3):
    #         print("aaa in base haha",n)

    class Abc():
        def aaa1(self):
            print("aaa")
            return "i am aaa"
    abc = Abc()
    import cProfile
    cProfile.run('abc.aaa1()')





if __name__ == "__main__":
    main()