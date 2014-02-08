def palindromeV1(string):
    if string == string[::-1]:
        return "YES"
    return "NO"
print palindromeV1(raw_input())
