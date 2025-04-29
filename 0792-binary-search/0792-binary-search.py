class Solution(object):
    def search(self, nums, target):
        low,high=0,len(nums)-1
        result=-1
        while low<=high:
            mid=(low+high)/2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return result