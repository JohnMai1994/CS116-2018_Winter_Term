##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 08, Question 1
##===============================================

import check
#q1a
# shift_encode(s) converts a string, s, to another by shifting each alphabetic 
#    character by a fixed amount, which determined by the most frequently 
#    alphabetic in s

# shift_encode: Str -> Str

# Examples:
# shift_encode('HEY! Where you at?') => "KHB! Zkhuh brx dw?"
# shift_encode("Q"*(26*2 + 3) + "w") => "T"*(26*2 + 3) + "z"
# shift_encode("a2b") => "b2c"

def shift_encode(s):
    character = {}
    for char in s:
        char = char.lower()
        if char.isalpha():
            if char in character:
                character[char] += 1
            else:
                character[char] = 1
            
    max_times = 0
    for curr_chars in character:
        if character[curr_chars] > max_times:
            max_times = character[curr_chars]
    
    s_character = 'abcdefghijklmnopqrstuvwxyz'
    l_character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    def swap(char, num):
        if char.isupper():
            pos = (l_character.find(char) + num) % 26
            return l_character[pos]
        elif char.islower():
            pos = (s_character.find(char) + num) % 26
            return s_character[pos]
        else:
            return char
    
    return ''.join(list(map(lambda x: swap(x, max_times), s)))

# Test:
# String == '' or other None alpha
check.expect('T1(a)', shift_encode(''), '')
check.expect('T2(a)', shift_encode('132412'), '132412')
check.expect('T3(a)', shift_encode('?":#!'), '?":#!')
check.expect('T4(a)', shift_encode('13?"'), '13?"')
# String only alpha, contain Capital
check.expect('T5(a)', shift_encode('I love Computer Science'), 'M pszi Gsqtyxiv Wgmirgi')
check.expect('T6(a)', shift_encode('Z'* 23), 'W' * 23)
check.expect('T7(a)', shift_encode('AABBCCa'), 'DDEEFFd')
check.expect('T8(a)', shift_encode('abcdefghijk'), 'bcdefghijkl')
check.expect('T9(a)', shift_encode('ABCDEFGHIJKl'), 'BCDEFGHIJKLm')
# String mix alpha and other symbol
check.expect('T10(a)', shift_encode('      a'), '      b')
check.expect('T11(a)', shift_encode('#####aac'), '#####cce')
check.expect('T12(a)', shift_encode('&*1223AVbbUiF'), '&*1223CXddWkH')



#q1b
# shift_dncode(s) converts a string, s, to another by shifting each alphabetic 
#    character by a fixed amount, which determined by the most frequently 
#    alphabetic in s, inverse to the encode

# shift_dncode: Str -> Str

# shift_decode("KHB! Zkhuh brx dw?") => "HEY! Where you at?"
# shift_decode("Q"*26) => "Q"*26
# shift_decode("b2c") => "a2b"

def shift_decode(s):
    character = {}
    for char in s:
        char = char.lower()
        if char.isalpha():
            if char in character:
                character[char] += 1
            else:
                character[char] = 1
            
    max_times = 0
    for curr_chars in character:
        if character[curr_chars] > max_times:
            max_times = character[curr_chars]
    
    s_character = 'abcdefghijklmnopqrstuvwxyz'
    l_character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            
    def swap(char, num):
        if char.isupper():
            pos = (l_character.find(char) - num) % 26
            return l_character[pos]
        elif char.islower():
            pos = (s_character.find(char) - num) % 26
            return s_character[pos]
        else:
            return char
            
    return ''.join(list(map(lambda x: swap(x, max_times), s)))

# Test
# String == '' or other None alpha
check.expect('T1(b)', shift_decode(''), '')
check.expect('T2(b)', shift_decode('132412'), '132412')
check.expect('T3(b)', shift_decode('?":#!'), '?":#!')
check.expect('T4(b)', shift_decode('13?"'), '13?"')
# String only alpha, contain Capital
check.expect('T5(b)', shift_decode('I love Computer Science'), 'E hkra Ykilqpan Oyeajya')
check.expect('T6(b)', shift_decode('Z'* 23), 'C' * 23)
check.expect('T7(b)', shift_decode('AABBCCa'), 'XXYYZZx')
check.expect('T8(b)', shift_decode('abcdefghijk'), 'zabcdefghij')
check.expect('T9(b)', shift_decode('ABCDEFGHIJKl'), 'ZABCDEFGHIJk')
# String mix alpha and other symbol
check.expect('T10(b)', shift_decode('      a'), '      z')
check.expect('T11(b)', shift_decode('#####aac'), '#####yya')
check.expect('T12(b)', shift_decode('&*1223AVbbUiF'), '&*1223YTzzSgD')
