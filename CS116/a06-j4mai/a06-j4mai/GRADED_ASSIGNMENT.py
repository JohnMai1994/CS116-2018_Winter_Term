ASSIGNMENT 06
Student's Quest ID: j4mai

**** Testing Results **********************************************************

39/40   Total Mark

 ** Question 1: 9/9
 ** Question 2: 7/7
 ** Question 3: 13/14
 ** Question 4: 10/10

(Question 1, Test t01, 1 marks): Part A: n2b:13: Passed; passed.
(Question 1, Test t02, 1 marks): Part A: n2b:12: Passed; passed.
(Question 1, Test t03, 1 marks): Part A: n2b:1: Passed; passed.
(Question 1, Test t04, 1 marks): Part A: n2b:0: Passed; passed.
(Question 1, Test t05, 1 marks): Part B: base2: Passed; passed.
(Question 1, Test t06, 1 marks): Part B: base12: Passed; passed.
(Question 1, Test t07, 1 marks): Part B: base5: Passed; passed.
(Question 1, Test t08, 1 marks): Part B: a million: Passed; passed.
(Question 1, Test t09, 1 marks): Part B: a pretty big number: Passed; passed.
(Question 2, Test t01, 1 marks): down: Passed; passed.
(Question 2, Test t02, 1 marks): up: Passed; passed.
(Question 2, Test t03, 1 marks): up and down: Passed; passed.
(Question 2, Test t04, 1 marks): repeated peak: Passed; passed.
(Question 2, Test t05, 1 marks): all negative: Passed; passed.
(Question 2, Test t06, 1 marks): empty: Passed; passed.
(Question 2, Test t07, 1 marks): check to ensure NO mutation of original list:
    Passed; passed.
(Question 3, Test t01, 1 marks): Part A: empty Str: Passed; passed.
(Question 3, Test t02, 1 marks): Part A: length 1: Passed; passed.
(Question 3, Test t03, 1 marks): Part A: even & True: Passed; passed.
(Question 3, Test t04, 1 marks): Part A: even & False: Passed; passed.
(Question 3, Test t05, 1 marks): Part A: odd & True: Passed; passed.
(Question 3, Test t06, 1 marks): Part A: odd & False: Passed; passed.
(Question 3, Test t07, 1 marks): Part A: aman: Passed; passed.
(Question 3, Test t08, 1 marks): Part B: empty Str: FAILED; FAILED: got None
    expected
(Question 3, Test t09, 1 marks): Part B: single char: Passed; passed.
(Question 3, Test t10, 1 marks): Part B: two equal length subpals: Passed;
    passed.
(Question 3, Test t11, 1 marks): Part B: whole string: Passed; passed.
(Question 3, Test t12, 1 marks): Part B: no subpal: Passed; passed.
(Question 3, Test t13, 1 marks): Part B: pretty long: Passed; passed.
(Question 3, Test t14, 1 marks): Part B: preposterously long: Passed; passed.
(Question 4, Test t01, 1 marks): Part A: testdata: Passed; passed.
(Question 4, Test t02, 1 marks): Part A: /\: Passed; passed.
(Question 4, Test t03, 1 marks): Part A: peak, height 3: Passed; passed.
(Question 4, Test t04, 1 marks): Part A: up down (x3), peak height 1: Passed;
    passed.
(Question 4, Test t05, 1 marks): Part A: empty string: Passed; passed.
(Question 4, Test t06, 1 marks): Part A: pretty high: Passed; passed.
(Question 4, Test t07, 1 marks): Part B: simple: Passed; passed.
(Question 4, Test t08, 1 marks): Part B: return to horizon: Passed; passed.
(Question 4, Test t09, 1 marks): Part B: empty string: Passed; passed.
(Question 4, Test t10, 1 marks): Part B: tall: Passed; passed.


**** testing_result.txt *****************************************************************
Total number of tests missing: 7

nat2bin: All 6 required cases were tested.

nat2base: 1 of the 8 required cases were missing:
 - n = 1

find_bigger: All 5 required cases were tested.

is_palindrome: 3 of the 7 required cases were missing:
 - Empty String
 - Length of 1
 - Palindrome of Odd number length

longest_subpalindrome: 2 of the 6 required cases were missing:
 - Empty String
 - Single Character

max_height: All 4 required cases were tested.

render_mountain: 1 of the 4 required cases were missing:
 - Empty String



**** a06q1.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 06, Question 1
##===============================================
## In each function, copy the function header to your own file. 
## Your solution will replace "pass" in the body of the functions.
import check
# Question 1 - part a
# nat2bin(n) return a non-empty list which is the binary digits by consuming 
#   a Nat number, n.
# nat2bin: Nat -> (listof (anyof 0 1))
# require:
# n >= 0
# Examples:
# nat2bin(12) => [1, 1, 0, 0]
# nat2bin(5) => [1, 0, 1]
# nat2bin(2) => [1, 0]
# nat2bin(0) => [0]

def nat2bin(n):
    if n == 0:
        return [0]
    else:
        list_num = 0
        while n >= 2**list_num:
            list_num += 1
            alist = list(range(list_num))
            alist.reverse()
            value_list = []
        for i in alist:
            append = n // 2**i
            n = n % 2**i
            value_list.append(append)
        return value_list
# Test:
# Test1: 0 - 9
check.expect('n=0', nat2bin(0), [0])
check.expect('n=1', nat2bin(1), [1])
check.expect('n=2', nat2bin(2), [1,0])
check.expect('n=3', nat2bin(3), [1,1])
check.expect('n=4', nat2bin(4), [1,0,0])
check.expect('n=6', nat2bin(6), [1,1,0])
check.expect('n=5', nat2bin(5), [1,0,1])
check.expect('n=8', nat2bin(8), [1,0,0,0])
check.expect('n=9', nat2bin(9), [1,0,0,1])
# Test2: 10 - 99
check.expect('n=12', nat2bin(12), [1,1,0,0])
check.expect('n=25', nat2bin(25), [1,1,0,0,1])
check.expect('n=38', nat2bin(38), [1,0,0,1,1,0])
check.expect('n=49', nat2bin(49), [1,1,0,0,0,1])
check.expect('n=58', nat2bin(58), [1,1,1,0,1,0])
check.expect('n=79', nat2bin(79), [1,0,0,1,1,1,1])
# Test3: bigger than 100
check.expect('n=100', nat2bin(100), [1,1,0,0,1,0,0])
check.expect('n=250', nat2bin(250), [1,1,1,1,1,0,1,0])
        
# Question 1 - part b
# nat2base(n, base) consumes two Nat,n and base, and returns a list of Nat 
# representing n in the base given by base.
# nat2base: Nat Nat -> (listof Nat)
# requires:
# n >= 0, base >= 0
# examples:
# nat2base(12, 2) => [1, 1, 0, 0]
# nat2base(245, 10) => [2, 4, 5]
# nat2base(326, 5) => [2, 3, 0, 1]
# nat2base(165, 16) => [10, 5]
# nat2base(36, 36) => [1, 0]

def nat2base(n, base):
    if n == 0:
        return [0]
    else:
        list_num = 0
        while n >= base**list_num:
            list_num += 1
            alist = list(range(list_num))
            alist.reverse()
            value_list = []
        for i in alist:
            append = n // base**i
            n = n % base**i
            value_list.append(append)
        return value_list        

# Test:
# Test1: n from 0 to 150, base = 2
check.expect('n=0, base=2', nat2base(0,2), [0])
check.expect('n=5, base=2', nat2base(5,2), [1,0,1])
check.expect('n=17, base=2', nat2base(17,2), [1,0,0,0,1])
check.expect('n=24, base=2', nat2base(24,2), [1,1,0,0,0])
check.expect('n=63, base=2', nat2base(63,2), [1,1,1,1,1,1])
check.expect('n=97, base=2', nat2base(97,2), [1,1,0,0,0,0,1])
check.expect('n=149, base=2', nat2base(149,2), [1,0,0,1,0,1,0,1])
# Test2: n from 0 to 150, base =5
check.expect('n=0, base=5', nat2base(0,5), [0])
check.expect('n=5, base=5', nat2base(5,5), [1,0])
check.expect('n=15, base=5', nat2base(15,5), [3,0])
check.expect('n=25, base=5', nat2base(25,5), [1,0,0])
check.expect('n=78, base=5', nat2base(78,5), [3,0,3])
check.expect('n=49, base=5', nat2base(49,5), [1,4,4])
check.expect('n=50, base=5', nat2base(50,5), [2,0,0])
check.expect('n=150, base=5', nat2base(150,5), [1,1,0,0])
# Test3: n from 0 to 150, base = 17
check.expect('n=0, base=17', nat2base(0,17), [0])
check.expect('n=17, base=17', nat2base(17,17), [1,0])
check.expect('n=34, base=17', nat2base(34,17), [2,0])
check.expect('n=56, base=17', nat2base(56,17), [3,5])
check.expect('n=77, base=17', nat2base(77,17), [4,9])
check.expect('n=99, base=17', nat2base(99,17), [5,14])
check.expect('n=132, base=17', nat2base(132,17), [7,13])
# Test4: n from 0 to 500, base = 36
check.expect('n=0, base=36', nat2base(0,36), [0])
check.expect('n=36, base=36', nat2base(36,36), [1,0])
check.expect('n=72, base=36', nat2base(72,36), [2,0])
check.expect('n=90, base=36', nat2base(90,36), [2,18])
check.expect('n=150, base=36', nat2base(150,36), [4,6])
check.expect('n=260, base=36', nat2base(260,36), [7,8])
check.expect('n=360, base=36', nat2base(360,36), [10,0])




**** a06q2.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 06, Question 2
##===============================================
import check
# Question 2
# find_bigger(ints) consumes a (listof Int), ints, and returns a (listof Int)
#   which values in the list that are bigger than all values that came before 
#   in the list
# find_bigger: (listof Int) -> (listof Int)
# Examples:
# find_bigger([0, 4, 5, 4]) => [0, 4, 5]
# find_bigger([1, 2, 4, 4]) => [1, 2, 4]
# find_bigger([-2, -4, -4, -1]) => [-2, -1]
# find_bigger([]) => []

def find_bigger(ints):
    if ints==[]:
        return []
    else:
        num = -1
        z = [ints[0]]
        max_num = ints[0]
        for k in ints:
            if max_num < k:
                max_num = max(max_num, k)
                z.append(k)
                num +=1
            else:
                num +=1
        return z

# Test:
# Test1: empty list
check.expect('empty', find_bigger([]), [])
# Test2: increasing order
check.expect('Increase Order1', find_bigger([1,2,3,4,5,6,7]), [1,2,3,4,5,6,7])
check.expect('Increase Order2', find_bigger([1,3,3,4,6,6,8]), [1,3,4,6,8])
check.expect('Increase Order3', find_bigger([1,2,4,5,8,10]), [1,2,4,5,8,10])
check.expect('Increase Order4', find_bigger([1,5,8,12,33,99]), [1,5,8,12,33,99])
check.expect('Increase Order5', find_bigger([1,15,15,15,90]), [1,15,90])
check.expect('Increase Order6', find_bigger([1,5,6,7]), [1,5,6,7])
# Test3: decreasing order
check.expect('Decreasing Order1', find_bigger([9,8,7,6,5,4,3]), [9])
check.expect('Decreasing Order2', find_bigger([19,7,4,2]), [19])
check.expect('Decreasing Order3', find_bigger([99,55,32,32,12,0]), [99])
check.expect('Decreasing Order4', find_bigger([87,4,3,67,3]), [87])
check.expect('Decreasing Order5', find_bigger([9,8,8,8,8,8,8]), [9])
check.expect('Decreasing Order6', find_bigger([9,8,2,9,4]), [9])
# Test4: up-down-up order
check.expect('Up-Down-UP Order1', find_bigger([2,6,9,8,7,7,5,8,10]), [2,6,9,10])
check.expect('Up-Down-UP Order2', find_bigger([2,19,7,5,100,101]), [2,19,100,101])
check.expect('Up-Down-UP Order3', find_bigger([2,20,21,20,21,22]), [2,20,21,22])
# Test5: All Same
check.expect('All Same', find_bigger([2,2,2,2,2]), [2])
check.expect('All Same', find_bigger([5,5,5]), [5])
# Test6: Sample Question
check.expect('Sample Question1', find_bigger([0, 4, 5, 4]), [0,4,5])
check.expect('Sample Question2', find_bigger([1,2,4,4]), [1,2,4])
check.expect('Sample Question3', find_bigger([-2,-4,-4,-1]), [-2,-1])



**** a06q3.py *****************************************************************
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

**** a06q4.py *****************************************************************
##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 06, Question 4
##===============================================
import check
# Question 4 - part a
# max_height(desc) consumes a Str, desc, and returns the maximum height reached
# max_height: Str -> Nat
# Requires: 
#  desc is guaranteed to have the following properties:
#  (1) it contains only the characters '+' and '-'.
#  (2) The two characters appear the same number of times.
#  (3) Every substring of desc that starts at zero has at 
#      least as many '+' characters as '-'.
# Examples:
testdata = '+++--+++---+-++---'
# max_height(testdata) => 4
# max_height('+-') => 1
# max_height('+++---') => 3
# max_height('+-+-+-') => 1
# max_height('') => 0

def max_height(desc):
    height = 0
    max_height = 0
    if desc == '':
        return height
    for k in list(desc):
        if k == '+':
            height += 1
            max_height = max(height, max_height)
        else:
            height -= 1
            max_height = max(height, max_height)
    return max_height


# Test
# Test1: Examples
check.expect('Example1', max_height(testdata), 4)
check.expect('Example2', max_height('+-'), 1)
check.expect('Example3', max_height('+++---'), 3)
check.expect('Example4', max_height('+-+-+-'), 1)
check.expect('Example5', max_height(''), 0)
# Test2: Complex height
check.expect('Complex1', max_height('+++-++-++-++-------'), 6)
check.expect('Complex2', max_height('+-+++-+---'), 3)
check.expect('Complex3', max_height('+++-++-+++------'), 6)
check.expect('Complex4', max_height('+++---+++---+++---'), 3)

# Question 4 - part b
# height(desc) consumes a Str, desc, and returns the height reached.
# height: Str -> Nat
# Examples:
# height(testdata) => 0
# height('++-') => 1
# height('+++-') => 2
# height('++-+++-') => 3

def height(desc):
    height = 0
    max_height = 0
    if desc == '':
        return height
    for k in list(desc):
        if k == '+':
            height += 1
        else:
            height -= 1
    return height    

# render_mountain(desc) consumes a Str, desc, and returns a (listof Str), which
#  could be printed as the mountain
# render_mountain: Str -> (listof Str)
# Requires: 
#  desc is guaranteed to have the following properties:
#  (1) it contains only the characters '+' and '-'.
#  (2) The two characters appear the same number of times.
#  (3) Every substring of desc that starts at zero has at 
#      least as many '+' characters as '-'.
# Examples:
# render_mountain('++-++---') => ['    /\\  ', ' /\\/  \\ ', '/      \\']

def render_mountain(desc):
    total_height = max_height(desc)
    length = len(desc)
    empty_list = []
    k = 0
    while k < total_height:
        empty_list.append([])
        z = 0
        while z < length:
            empty_list[k].append(' ')
            z += 1
        k += 1
    start = 0
    up = '/'
    down = '\\'
    while start < length:
        if desc[start] == '+':
            height_desc = -height(desc[:start+1])
            empty_list[height_desc][start] = up
            start += 1
        else:
            height_desc = -height(desc[:start])
            empty_list[height_desc][start] = down
            start += 1
    for i in range(len(empty_list)):
        empty_list[i] = ''.join(empty_list[i])
    return empty_list

# Test:
# Test1: Sample
check.expect('simple',
             render_mountain('++-++---'),
             [
                '    /\\  ',
                ' /\\/  \\ ',
                '/      \\'
             ])
# Test2: easy test
check.expect('easy test1',
             render_mountain('+-'),
             ['/\\'])

check.expect('easy test2',
             render_mountain('+-+-+-+-'),
             ['/\\/\\/\\/\\'])

# Test3: complex test
check.expect('complex test1',
             render_mountain('+-++--+++---'),
             [
                 '        /\\  ',
                 '   /\\  /  \\ ',
                 '/\\/  \\/    \\'
             ])

check.expect('complex test2',
             render_mountain('+++--+++---+-++---'),
             [
                 '       /\\         ',
                 '  /\\  /  \\    /\\  ',
                 ' /  \\/    \\/\\/  \\ ',
                 '/                \\'
             ])
  

**** End of graded assignment. *************************************************
