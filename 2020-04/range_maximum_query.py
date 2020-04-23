#!/usr/bin/python3
# coding=utf-8
"""
区间最大和

问题描述:

给定 n 个正整型组成的数列 a1, a2, ..., an 和一个整数 M.

要求从这个数列中找到一个自区间 [i, j], 也就是这个数列中连续的数字 ai, ai+1, ..., aj-1, aj, 
使得这个自区间的和在不超过 M 的情况下最大.

输出 i, j 和区间和, 如果多个区间符合要求, 请输出 i 最小的那一个. (ai <= 10^5, M <= 10^9)
"""
import time
import random


def record_time(func):
    def decorator(*args, **kwargs):
        start_time = time.time()

        result = func(*args, **kwargs)

        used_time = time.time() - start_time

        print(f'[{func.__name__}] result: {result}, used_time: {used_time}s.')

        return result

    return decorator


@record_time
def sum_range_maximum_query_v1(array: list, m: int):
    """穷举法 O(n^3)"""
    sum_value = 0
    res_i = 0
    res_j = 0

    n = len(array)

    for i in range(n):
        for j in range(n):
            temp_value = 0
            for k in range(i, j + 1):
                temp_value += array[k]

            if temp_value <= m and temp_value > sum_value:
                sum_value = temp_value
                res_i = i
                res_j = j

    return res_i + 1, res_j + 1, sum_value


@record_time
def sum_range_maximum_query_v2(array: list, m: int):
    """前缀记忆 O(n^2)"""
    sum_value = 0
    res_i = 0
    res_j = 0

    n = len(array)

    s = [0]
    for num in array:
        s.append(s[-1] + num)

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            temp_value = s[j] - s[i - 1]
            if temp_value <= m and temp_value > sum_value:
                sum_value = temp_value
                res_i = i
                res_j = j

    return res_i, res_j, sum_value


@record_time
def sum_range_maximum_query_v3(array: list, m: int):
    """前缀记忆 + 二分查找, O(nlogn)"""
    sum_value = 0
    res_i = 0
    res_j = 0

    n = len(array)

    s = [0]
    for num in array:
        s.append(s[-1] + num)

    def binary_search(i):
        value = s[i - 1] + m
        left = i
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if s[mid] >= value:
                right = mid
            else:
                left = mid + 1

        if s[left] == value:
            return left
        else:
            return left - 1

    for i in range(1, n + 1):
        j = binary_search(i)

        temp_value = s[j] - s[i - 1]
        if temp_value <= m and temp_value > sum_value:
            sum_value = temp_value
            res_i = i
            res_j = j

    return res_i, res_j, sum_value


@record_time
def sum_range_maximum_query_v4(array: list, m: int):
    """队列辅助 O(n)"""
    sum_value = 0
    res_i = 0
    res_j = 0

    n = len(array)

    i = j = 0

    temp_value = 0

    while i < n:
        while j < n & temp_value + array[j] <= m:
            temp_value += array[j]
            j += 1

        if temp_value <= m & temp_value > sum_value:
            sum_value = temp_value
            res_i = i + 1
            res_j = j

        temp_value -= array[i]
        i += 1

    return res_i, res_j, sum_value


if __name__ == '__main__':
    m = random.randint(200, 2000)
    test_array = [random.randint(1, 100) for _ in range(1000)]

    print(test_array, m)

    sum_range_maximum_query_v1(test_array, m)
    sum_range_maximum_query_v2(test_array, m)
    sum_range_maximum_query_v3(test_array, m)
    sum_range_maximum_query_v4(test_array, m)
