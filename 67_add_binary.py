class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        if len(a) >= len(b):
            res = self.add(a, b)
        else:
            res = self.add(b, a)
        return res

    def add(self, big, small):
        diff = len(big) - len(small)
        # Reverse the original strings
        big = big[::-1]
        small = small[::-1]
        carry = 0
        res = list()
        for i in range(0, len(small)):
            res.append(str((int(big[i]) + int(small[i]) + carry) % 2))
            carry = (int(big[i]) + int(small[i]) + carry) / 2

        if diff > 0:
            for i in range(len(small), len(big)):
                res.append(str((int(big[i]) + carry) % 2))
                carry = (int(big[i]) + carry) / 2

        if carry == 1:
            res.append('1')

        res.reverse()
        return ''.join(res)
