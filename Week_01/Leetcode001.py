'''
先sort,左端最小，右端最大，方便从数组两头布置双指针i,j收缩试探i+j是否符合目标值，i<j说明已经左右指针已经汇合不需要继续
符合返回i,j位置
高于目标则左移右指针，当某元素已经大于目标值后，
低于目标则右移左指针
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size=len(nums)
        if not size:
            return []
        nums,idx=zip(*sorted(zip(nums,list(range(size)))))
        i=0
        j=size-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [idx[i],idx[j]]
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
        return []