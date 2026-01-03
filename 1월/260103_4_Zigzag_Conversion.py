class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        answer = {}
        for i in range(numRows):
            answer[i] = ""

        flag = 1
        current = 0
        for i in s:
            answer[current] = answer[current]+i

            if flag: current += 1
            else: current -= 1

            if current == numRows:
                flag = 0
                current = current - 2
            elif current == -1:
                flag = 1
                current = current + 2

        answer_str = ""
        for i in answer:
            answer_str += answer[i]
        
        return answer_str

test = Solution()
print(test.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
# print(test.convert("AB", 1))