from typing import List

# time complexity: O(N)
# space complexity: O(N)
def reverse(s: List[str]) -> None:
    t = s[::-1]

    for (i,v) in enumerate(t):
        print(i, v)
        s[i] = v