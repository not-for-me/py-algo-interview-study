
# time complexity: O(N)
# space complexity: O(N)
def check(sentence: str) -> bool:
    chars = [c.lower() for c in sentence if c.isalnum()]
    for i in range( len(chars) // 2 ):
        if chars[i] == chars[len(chars) - i - 1]:
            continue
        
        return False
    return True
