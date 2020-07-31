
def check(sentence) -> bool:
    chars = [c.lower() for c in sentence if c.isnumeric() or c.isalpha()]
    for i in range( len(chars) // 2 ):
        if chars[i] == chars[len(chars) - i - 1]:
            continue
        
        return False
    return True
