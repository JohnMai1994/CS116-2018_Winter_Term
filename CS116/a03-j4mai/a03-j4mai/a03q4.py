##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 03, Question 4
##===============================================

import check

#Q4
# space_position(s, n) consumes a string, s, and a natural number, n, and returns
#   an number n space position in s.
# space_position: Str Nat -> Nat
# Requires:
# s is a non-empty string
# n is a natural number greater than 0
# Examples:
# space_position("ab ab ar cde fa e", 3) => 8

def space_position(s, n):
    g = 0
    if n == 0:
        return -1
    if s[0:1].isspace():
        g = 1 + space_position(s[1:], n-1) 
    else:
        if s.count(" ") >= n:
            g = 1 + space_position(s[1:], n)
        else:
            g = len(s) +1 
    return g


# make_poem(s,n) consumes a string, s, and a natural number, n, and prints out
#  multiple lines, the same string as s where each line has n words in it.
# make_poem: Str Nat -> None
# Requires:
# s is a non-empty string
# n is a natural number greater than 0
# Examples:
# make_poem("How many Lowes would Rob Lowe rob if Rob Lowe could rob Lowes", 3) 
#           will print:
#  How many Lowes
#  would Rob Lowe
#  rob if Rob
#  Lowe could rob
#  Lowes
def make_poem(s,n):
    k = space_position(s, n)
    if k >= len(s):
        print(s)
    else:
        print(s[0:k])
        make_poem(s[k+1:], n)

# Test Example, n = 3
check.set_screen("How many Lowes\nwould Rob Lowe\nrob if Rob\nLowe could rob\nLowes")
check.expect("Q4T1", make_poem("How many Lowes would Rob Lowe rob if Rob Lowe could rob Lowes", 3), 
             None)

# Test when n = 1
check.set_screen("abc\ndef\nhijk\nlmno\npQ")
check.expect("Q4T2", make_poem("abc def hijk lmno pQ",1), None)

# Test When n = 4
check.set_screen("my job is very\nawaresome and my dad\nis superman")
check.expect("Q4T3", make_poem("my job is very awaresome and my dad is superman", 4), None)

