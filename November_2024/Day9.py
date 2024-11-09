class Solution:
    def minEnd(self, n: int, x: int) -> int:
        unsetBits = []

        for bit in range(64):
            if x >> bit & 1 ^ 1:
                unsetBits.append(bit)

        mask = n - 1
        for index in range(len(unsetBits)):
            if mask >> index & 1: 
                x |= 1 << unsetBits[index]

        return x