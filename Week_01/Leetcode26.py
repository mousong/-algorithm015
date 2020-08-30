'''
因为是排序数组，所以重复元素永远是相邻的
双指针法，前指针i初始为0，后指针j从1开始循环每次无论比对结果如何都+1后移。
比较i,j所指向的相邻元素，如果相同则i停留在原地，j指针一直后移直到找到第一个不同元素，这时把i后移一位，把j指针找到的不同元素赋予给这一位元素。相当于保留了重复元素一次，最邻近的不同元素被往前提紧跟在它后面。
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1