class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        pos = True
        if x < 0:
            pos = False
            x = x * -1
        x = list(str(x))
        n = ''
        while len(x) > 0:
            n = '{}{}'.format(n, x.pop())
        
        if (-2**31) > -int(n) or (2**31)-1 < int(n):
            return 0
            
        return int(n) if pos else int(n) * -1
        
if __name__ == '__main__':
    print(Solution().reverse(-8000))