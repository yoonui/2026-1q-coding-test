class Solution:
    def reverse(self, x: int) -> int:
        answer = 0

        strNum = list(str(x))[::-1]

        intNum = ''.join(strNum)
        if x < 0:
            answer = -int(intNum[:len(intNum)-1])
            return 0 if answer < -2 ** 31 else answer
        else:
            answer = int(intNum)
            return 0 if answer > 2 ** 31 -1 else answer

test = Solution()
# print(test.reverse(123))
# print(test.reverse(-123))
# print(test.reverse(120))
print(test.reverse(1534236469))