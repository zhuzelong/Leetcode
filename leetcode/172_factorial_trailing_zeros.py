class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0
        while n/5:
            res = res + n / 5
            n = n / 5
        return res
