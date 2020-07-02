class Solution(object):
    
    def twoSum(self, nums, target):
        keep = dict()
        i = 0
        while i < len(nums):
            v = nums[i]
            if keep.get(target - v) is not None:
                return [keep.get(target - v), i]
            
            if i+1 == len(nums):
                i += 1
                continue
            elif v + nums[i+1] == target:
                return [i, i+1]  
            else:
                keep[v] = i
            i += 1
                
if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 3], 6))