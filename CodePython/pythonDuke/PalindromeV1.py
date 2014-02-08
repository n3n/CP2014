import math

def isPalindrome(st):
    """
    isPalindrome -> bool

    Check palindrome string if palindrome return True,
    Otherwise return False.
    """
    return st[:len(st)/2] == st[:int(math.ceil(len(st)/2.0))-1:-1]

print ["NO", "YES"][isPalindrome(raw_input())]
    
