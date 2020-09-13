class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

	# 回溯法
        def backtrack(first = 0):
            # 递归terminator, 当所有数都填完了
            if first == n:  
                result.append(nums[:])
            # 递归currentLevelLogic
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 递归drilldown,继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        result = []
        backtrack()
        return result