class Solution:
    def multiply(self, A: int, B: int) -> int:
        if B == 0:
            return 0
        if B > 0:
            return A + self.multiply(A, B - 1)
        if B < 0:
            return -self.multiply(A, -B)

# 然后你可以按照下面的方式调用它：
s = Solution()
print(s.multiply(3, 4))  # 输出：12
print(s.multiply(1, 10))  # 输出：10
# 然后你可以按照下面的方式调用它：
s = Solution()
print(s.multiply(3, 4))  # 输出：12
print(s.multiply(1, 10))  # 输出：10