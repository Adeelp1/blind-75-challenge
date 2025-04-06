class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = list(bin(n))
        count = 0
        for i in range(len(bit)):
            if bit[i] == '1':
                count += 1
        return count

