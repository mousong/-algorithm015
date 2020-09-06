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