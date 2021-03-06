import random
import time


def naive_search(l, target):
    # example l = [1, 2, 3, 4, 5, 10]  and target = 10
    for index, x in enumerate(l):
        if x == target:
            return index
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
# in this function we will return the index of target value in list l
def binary_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1
    
    if high < low:
        return -1

    # example l = [1, 2, 3, 10, 15]  we should return index 3 for target = 10
    midpoint = (low + high) // 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint -1)
    else:
        # target > l[midpoint]
        return binary_search(l, target, midpoint + 1, high)


if __name__ == '__main__':
    '''
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))
    '''
    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print('Naive Search time:', (end - start) / length, 'seconds')

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('Binary Search time:', (end - start) / length, 'seconds')
    