class Solution(object):
    
    def twoSum(self, nums, target):
        keep = dict()
        for i, v in enumerate(nums):
            c = target - v
            if c not in keep:
                keep[v] = i
            else:
                return [keep[c], i]
                
        raise Exception('No indices found')

if __name__ == '__main__':
    print(Solution().twoSum([3, 2, 3], 6))