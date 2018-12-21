##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 06, Question 3
##===============================================
import check
# Question 3 - part a
# is_palindrome(s) Return True if s is a palindrome.
# is_palindrome: Str -> Bool
# Examples:
# is_palindrome ( ' racecar ') => True
# is_palindrome ( ' sata ') => False 

def is_palindrome(s):
    if len(s) < 2:
        return True
    else:
        head = 0
        end = 0
        k = s[:]
        while len(k) > 1:
            if k[0] == k[-1]:
                head += 1
                end -= 1
                k = k[1:-1]
            else:
                return False
        return True
# Test:
# Test1: is palindrome
check.expect('is palindrome1', is_palindrome('aldrtyuyuytrdla'), True)
check.expect('is palindrome2', is_palindrome('qwerrewq'), True)
check.expect('is palindrome3', is_palindrome('yuttrrttuy'), True)
check.expect('is palindrome4', is_palindrome('tttttttttttt'), True)
check.expect('is palindrome5', is_palindrome('peegfdAAdfgeep'), True)
check.expect('is palindrome6', is_palindrome('TOMILKYYKLIMOT'), True)
# Test2: is not palindrome
check.expect('is not palindrome1', is_palindrome('abcde'), False)
check.expect('is not palindrome2', is_palindrome('abcdefdcba'), False)
check.expect('is not palindrome3', is_palindrome('abcdeedcbk'), False)
check.expect('is not palindrome4', is_palindrome('abbccde'), False)
check.expect('is not palindrome5', is_palindrome('a bceceb a'), False)
check.expect('is not palindrome6', is_palindrome('adeeeedba'), False)
    
# Question 3 - part b
# longest_subpalindrome(s) consume a str, s, and returns the longest 
#   subpalindrome in s
# longest_subpalindrome: Str -> Str
# Requires:
#    s conatins only lowercase letters
# Examples:
# longest_subpalindrome('acaba') => 'aca'
# longest_subpalindrome('anna') => 'anna'
# longest_subpalindrome('sata') => 'ata'
# longest_subpalindrome('cba') => 'c'
# longest_subpalindrome('aracecarwinsarace') => 'racecar'

def longest_subpalindrome(s):
    length = len(s)
    k = 0
    empty_good = []
    while k < length:
        z = k+1
        while z <= length:
            if is_palindrome(s[k:z]):
                empty_good.append([s[k:z]])
                z += 1
            else:
                z += 1
        k += 1
        q = 0
    for i in empty_good:
        q = max(q, len(i[0]))
    for g in empty_good:
        if len(g[0]) == q: 
            return g[0]
    
# Test:
# Test1: Example Question
check.expect('Examples Question1', longest_subpalindrome('acaba'), 'aca')
check.expect('Examples Question2', longest_subpalindrome('anna'), 'anna')
check.expect('Examples Question3', longest_subpalindrome('sata'), 'ata')
check.expect('Examples Question4', longest_subpalindrome('cba'), 'c')
check.expect('Examples Question5', longest_subpalindrome('aracecarwinsarace'), 'racecar')
# Test2: s is palindrome
check.expect('is palindrome1', longest_subpalindrome('anbcddcbna'), 'anbcddcbna')
check.expect('is palindrome2', longest_subpalindrome('likeekil'), 'likeekil')
check.expect('is palindrome3', longest_subpalindrome('pythonnohtyp'), 'pythonnohtyp')
check.expect('is palindrome4', longest_subpalindrome('ilikeyouuoyekili'), 'ilikeyouuoyekili')
# Test3: s is not palindrome, but contain palindrome
check.expect('not palindrome1', longest_subpalindrome('ajdjasflkgaja'), 'ajdja')
check.expect('not palindrome2', longest_subpalindrome('hndgdnhgqwere'), 'hndgdnh')
check.expect('not palindrome3', longest_subpalindrome('rqwabcdefgfedcba'), 'abcdefgfedcba')
check.expect('not palindrome4', longest_subpalindrome('rweigiweq'), 'igi')
check.expect('not palindrome5', longest_subpalindrome('ywywywywy'), 'ywywywywy')
