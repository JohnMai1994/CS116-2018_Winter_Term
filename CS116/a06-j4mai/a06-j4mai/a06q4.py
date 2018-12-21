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
  
