from typing import List

# time complexity: O(N)
# space complexity: O(N)
def reverse(s: List[str]) -> None:
    # pythonic한 기본 내장 api가 inplace 변환이라니...
    s.reverse()
    # t = s[::-1]

    # for (i,v) in enumerate(t):
    #     print(i, v)
    #     s[i] = v