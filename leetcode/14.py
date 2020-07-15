

class Solution():
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]
        tab = dict()
        prefix = ''
        for p, s in enumerate(strs):
            if len(s) == 0:
                return ''
            for i, c in enumerate(s):
                if not tab.get(i):
                    tab[i] = [c, 1]
                elif c == tab[i][0]:
                    tab[i][1] += 1
                    prefix = '{}{}'.format(prefix, c if p == len(strs) - 1 else '')
                else:
                    break
        return ''.join([t[0] if t[1] == len(strs) else '' for t in tab.values()])


def test_func(benchmark):
    benchmark(Solution().longestCommonPrefix, ['abfabafbfabfd', 'abfabafbfabfdtrtrrg'])
    assert True