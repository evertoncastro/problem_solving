class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p = {
            '(': ')',
            ')': '(',
            '{': '}',
            '}': '{',
            '[': ']',
            ']': '['
        }
        i = 0
        print(s)
        while i < len(s) -1 and len(s) >= 2:
            if p[s[i]] == s[i+1]:
                s = s[:i] + s[i+2:]
                i += -1 if i > 0 else 0
                print(s)
                print('I continue or returns in: {}'.format(str(i)))
                continue
            i+=1
            print('I goes to: {}'.format(str(i)))
        if len(s) > 0:
            return False
        return True

if __name__ == '__main__':
    Solution().isValid('(]')