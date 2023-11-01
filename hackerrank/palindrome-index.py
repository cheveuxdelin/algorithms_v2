def palindromeIndex(s):
    def is_palindrome(i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    i = 0
    j = len(s)-1
        
    while i <= j:
        if s[i] != s[j]:
            if is_palindrome(i+1, j):
                return i
            elif is_palindrome(i, j-1):
                return j
            else:
                return -1
        i += 1
        j -= 1
    return -1