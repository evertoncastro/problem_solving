from math import log10

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + (x % 10)
            x = x // 10
    
        return x == reverted or x == reverted//10
            


if __name__ == '__main__':
    print(Solution().isPalindrome(10))


XXIX  
10 10 1 5

CCXLV
100 100 10 50 5