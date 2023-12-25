def multiply(x, y):
    if y == 0:
        return 0
    elif y < 0:
        return -(x - multiply(x, y+1))
    else:
        return x + multiply(x, y-1)

def collectMultiples(intList, n):
    if len(intList) == 0:
        return []
    if intList[0] % n == 0: # first integer is multiple of n
        return [intList[0]] + collectMultiples(intList[1:], n)
    else: # first int is not multiple of n
        return collectMultiples(intList[1:], n)

def countVowels(s):
    if s == '':
        return 0
    elif s[0] in "AEIOUaeiou":
        return 1 + countVowels(s[1:])
    else:
        return 0 + countVowels(s[1:])

def reverseVowels(s):
    vowel_str = ''
    if s == '':
        return vowel_str
    elif s[0] not in "AEIOUaeiou":
        return reverseVowels(s[1:])
    else:
        vowel_str += reverseVowels(s[1:]) + s[0]
        return vowel_str
    
def removeSubString(s, sub):
    if len(s) == 0:
        return ''
    elif len(sub) == 0:
        return s
    elif s.startswith(sub):
        return removeSubString(s[len(sub):], sub)
    else:
        return s[0] + removeSubString(s[1:], sub)