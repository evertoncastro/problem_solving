from math import log10

class Solution(object):
    def romanToInt(self, x):
        """
        :type s: str
        :rtype: int
        """
        from_to = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        i = 0
        value = 0
        while i < len(x):
            current = from_to[x[i]]
            if i == 0:
                value += current
            else:
                last = from_to[x[i-1]]
                last_plus_2 = 2 * last
                value += current if last >= current else (current - last_plus_2)
            i += 1
        return value

        


if __name__ == '__main__':
    print(Solution().romanToInt('MMMCMXCIX'))


# XXIX  
# 10 10 1 5

# CCXLV
# 100 100 10 50 5


# XXIX = 29

# error XXIIV = 28
# XXVIII