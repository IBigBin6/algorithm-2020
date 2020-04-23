# coding=utf-8
"""
最大容量

给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
"""


def maxArea(height: list) -> int:
    max_area = 0

    i, j = 0, len(height) - 1

    while i < j:
        if height[i] < height[j]:
            tmp = height[i] * (j - i)
            i += 1
        else:
            tmp = height[j] * (j - i)
            j -= 1

        if tmp > max_area:
            max_area = tmp

    return max_area


if __name__ == '__main__':
    maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
