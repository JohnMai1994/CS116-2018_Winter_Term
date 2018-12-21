##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 08, Question 2
##===============================================
#q2
import check
# ## a Bingocard is a (dictof Str (listof (anyof Nat 'XX'))) and 		
# ## represents a standard bingo card in 75 ball bingo
# ## requires: 
# ##	- it has exactly 5 key value pairs
# ##	- the keys are the capital letters 'B' 'I' 'N' 'G' 'O'
# ## 	- each list is length 5 and is made up of the string 'XX' or 
# ##	  numbers 1 through 75 according to the breakdown below
# ##	- key 'B' only has numbers between 1 and 15 inclusive 
# ##	- key 'I' only has numbers between 16 and 30 inclusive
# ##	- key 'N' only has numbers between 31 and 45 inclusive
# ##	- key 'G' only has numbers between 46 and 60 inclusive
# ##	- key 'O' only has numbers between 61 and 75 inclusive
# ##	- the associated list at key 'N' will always have its element at 
# ##	  index 2 equal to 'XX' (representing the free space)
# ##	- the numbers in each list must be unique

# display_bingo_card(crd) prints a nicely formatted version of crd
# Effects: 6 lines are printed
# display_bingo_card: Bingocard -> None

def display_bingo_card(crd):
    
    header = "  B  I  N  G  O  "
    
    print(header)
    
    for i in range(5):
        line = " {0:2} {1:2} {2:2} {3:2} {4:2}  ".format(crd['B'][i],
                                                         crd['I'][i],
                                                         crd['N'][i],
                                                         crd['G'][i],
                                                         crd['O'][i])
        print(line)
        
row_win = "Winner: Row {0}."
column_win = "Winner: Column {0}."
no_win = "Not a winner."


# play_bingo(crd, lon) consumes a bingo card, crd, and a list of integers, lon,
#   and returns a string stating what column or row is winner or not and mutates
#   crd' number which also appear in lon into 'XX'

# play_bingo: Bingocard (listof Int) -> Str

# Effect: the same numbers between crd and lon are mutated into 'XX' 

# Requires:
# integers in lon are between 1 to 75

# Examples:
# EX1
# If bgo_crd = {'O': [61, 72, 'XX', 67, 74], 'I': [25, 23, 'XX', 20, 26],\
#               'N': [43, 38, 'XX', 36, 40], 'B': ['XX', 'XX', 6, 'XX', 10],
#               'G': [56, 53, 'XX', 47, 52]}
# play_bingo(bgo_crd,[6]) => 'Winner: Row 3.'
# EX2
# If my_card = {'O': [65, 62, 'XX', 64, 74], 'I': [22, 25, 'XX', 20, 26],
#               'N': [41, 45, 'XX', 33, 43], 'B': ['XX', 'XX', 14, 'XX', 'XX'],
#               'G': [55, 60, 'XX', 53, 56]}
# play_bingo(my_card, [55,50,22]) => 'Not a winner.'
# EX3 - continue playing
# play_bingo(my_card, [14]) => 'Winner: Column B.'

def play_bingo(crd,lon):
    def replace_xx(lst, num):
        k = 0
        while k < len(lst):
            if lst[k] == num:
                lst[k] = 'XX'
                k += 1
            else:
                k += 1            
        return lst   
    
    def bingo_win(crd_list):
        for z in crd:   
            if crd[z] == ['XX', 'XX', 'XX', 'XX', 'XX']:
                return True    
        for t in range(5):
            if crd['B'][t] == crd['I'][t] == crd['N'][t] == \
               crd['G'][t] == crd['O'][t] == 'XX':
                return True
            
    for rip in lon:
        if bingo_win(crd):
            for z in crd:
                if crd[z] == ['XX', 'XX', 'XX', 'XX', 'XX']:
                    return column_win.format(z)
        
            for t in range(5):
                if crd['B'][t] == crd['I'][t] == crd['N'][t] == \
                   crd['G'][t] == crd['O'][t] == 'XX':
                    return row_win.format(t+1)     
                
        if 1 <= rip <= 15:
            replace_xx(crd['B'], rip)
        elif rip <= 30:
            replace_xx(crd['I'], rip)
        elif rip <= 45:
            replace_xx(crd['N'], rip)
        elif rip <= 60:
            replace_xx(crd['G'], rip)
        else:
            replace_xx(crd['O'], rip)
    
    for z in crd:   
        if crd[z] == ['XX', 'XX', 'XX', 'XX', 'XX']:
            return column_win.format(z)    
    for t in range(5):
        if crd['B'][t] == crd['I'][t] == crd['N'][t] == \
           crd['G'][t] == crd['O'][t] == 'XX':
            return row_win.format(t+1)    
    
    return no_win
    

        
# Test 

bingo_1 ={'B': [15, 10, 4, 13, 3], 'I': [17, 22, 30, 28, 19], \
          'N': [33, 32, 'XX', 44, 43], 'G': [57, 60, 47, 53, 56], \
          'O': [65, 69, 73, 62, 72]}
bingo_2 = {'B': [3, 2, 11, 6, 1], 'I': [26, 23, 16, 27, 17],\
           'N': [35, 42, 'XX', 33, 38], 'G': [55, 58, 50, 54, 51],\
           'O': [72, 75, 71, 61, 64]}
bingo_3 = {'B': [2, 5, 15, 13, 3], 'I': [24, 30, 25, 27, 21],\
           'N': [40, 44, 'XX', 31, 41], 'G': [53, 46, 47, 57, 54],\
           'O': [72, 67, 71, 61, 66]}
bingo_4 = {'B': [10, 14, 1, 5, 8], 'I': [22, 23, 21, 16, 18],\
           'N': [39, 36, 'XX', 45, 40], 'G': [52, 58, 50, 48, 53], \
           'O': [62, 75, 70, 64, 72]}
bingo_5 = {'B': [11, 13, 8, 15, 3], 'I': [23, 27, 25, 16, 24],\
           'N': [43, 32, 'XX', 44, 41], 'G': [46, 58, 50, 55, 54],\
           'O': [73, 62, 74, 69, 65]}
bcard = {'O': [73, 61, 64, 72, 70], 'I': [29, 27, 28, 21, 17],
         'N': [33, 40, 'XX', 42, 43], 'B': [13, 8, 5, 15, 1],
         'G': [49, 55, 60, 56, 54]}

# T1 - no win - no win - win column I
check.expect('T1a', play_bingo(bingo_1, [15,22,60,69]), no_win)
check.expect('T1a(bingo_1)', bingo_1, {'B': ['XX', 10, 4, 13, 3], 'I': [17, 'XX', 30, 28, 19], \
                                      'N': [33, 32, 'XX', 44, 43], 'G': [57, 'XX', 47, 53, 56], \
                                      'O': [65, 'XX', 73, 62, 72]})
check.expect('T1b', play_bingo(bingo_1, [30, 47, 72]), no_win)
check.expect('T1b(bingo_1)', bingo_1, {'B': ['XX', 10, 4, 13, 3], 'I': [17, 'XX', 'XX', 28, 19], \
                                      'N': [33, 32, 'XX', 44, 43], 'G': [57, 'XX', 'XX', 53, 56], \
                                      'O': [65, 'XX', 73, 62, 'XX']})
check.expect('T1c', play_bingo(bingo_1, [17, 28, 19]), 'Winner: Column I.')
check.expect('T1c(bingo_1)', bingo_1, {'B': ['XX', 10, 4, 13, 3], 'I': ['XX', 'XX', 'XX', 'XX', 'XX'], \
                                      'N': [33, 32, 'XX', 44, 43], 'G': [57, 'XX', 'XX', 53, 56], \
                                      'O': [65, 'XX', 73, 62, 'XX']})

# T2 - no win - both column G and Row 5
check.expect('T2a', play_bingo(bingo_2, [55,50,51,1,33,17]), no_win)
check.expect('T2a(bingo_2)', bingo_2, {'B': [3, 2, 11, 6, 'XX'], 'I': [26, 23, 16, 27, 'XX'],\
                                       'N': [35, 42, 'XX', 'XX', 38], 'G': ['XX', 58, 'XX', 54, 'XX'],\
                                       'O': [72, 75, 71, 61, 64]})
check.expect('T2b', play_bingo(bingo_2, [64,58,54,38]), 'Winner: Column G.')
check.expect('T2b(bingo_2)', bingo_2, {'B': [3, 2, 11, 6, 'XX'], 'I': [26, 23, 16, 27, 'XX'],\
                                       'N': [35, 42, 'XX', 'XX', 38], 'G': ['XX', 'XX', 'XX', 'XX', 'XX'],\
                                       'O': [72, 75, 71, 61, 'XX']})

# T3 - no win - no win - no win
check.expect('T3a', play_bingo(bingo_3, [2,15,47,66,25,21,41,44]), no_win)
check.expect('T3a(bingo_3)', bingo_3, {'B': ['XX', 5, 'XX', 13, 3], 'I': [24, 30, 'XX', 27, 'XX'],\
                                       'N': [40, 'XX', 'XX', 31, 'XX'], 'G': [53, 46, 'XX', 57, 54],\
                                       'O': [72, 67, 71, 61, 'XX']})
check.expect('T3b', play_bingo(bingo_3, [3,67,72,57]), no_win)
check.expect('T3b(bingo_3)', bingo_3, {'B': ['XX', 5, 'XX', 13, 'XX'], 'I': [24, 30, 'XX', 27, 'XX'],\
                                       'N': [40, 'XX', 'XX', 31, 'XX'], 'G': [53, 46, 'XX', 'XX', 54],\
                                       'O': ['XX', 'XX', 71, 61, 'XX']})
check.expect('T3c', play_bingo(bingo_3, [24,30,13,31,61]), no_win)
check.expect('T3c(bingo_3)', bingo_3, {'B': ['XX', 5, 'XX', 'XX', 'XX'], 'I': ['XX', 'XX', 'XX', 27, 'XX'],\
                                       'N': [40, 'XX', 'XX', 'XX', 'XX'], 'G': [53, 46, 'XX', 'XX', 54],\
                                       'O': ['XX', 'XX', 71, 'XX', 'XX']})

# T4 - Row 5
check.expect('T4a', play_bingo(bingo_4, [14,36,75,23,58]), "Winner: Row 2.")
check.expect('T4a(bingo_4)', bingo_4, {'B': [10, 'XX', 1, 5, 8], 'I': [22, 'XX', 21, 16, 18],\
                                       'N': [39, 'XX', 'XX', 45, 40], 'G': [52, 'XX', 50, 48, 53], \
                                       'O': [62, 'XX', 70, 64, 72]})

# T5 - Row 1,2,3,4,5, Column B I N G O
check.expect('T5a', play_bingo(bingo_5, [11,13,8,15,3,23,27,25,16,24,43,32,44,41,46,58,50,54,55,73,62,74,69,65]), "Winner: Column B.")
check.expect('T5a(bingo_5)', bingo_5, {'B': ['XX', 'XX', 'XX', 'XX', 'XX'], 'I': [23, 27, 25, 16, 24],\
                                       'N': [43, 32, 'XX', 44, 41], 'G': [46, 58, 50, 55, 54],\
                                       'O': [73, 62, 74, 69, 65]})

# T6 - Example on pdf
check.expect('Ex1', play_bingo(bcard,[29,27,45,15,61,17,60,21,13,28,70,33]), 'Winner: Column I.')
check.expect('Ex1(bcard)', bcard, {'O': [73, 'XX', 64, 72, 70],
                          'I': ['XX', 'XX', 'XX', 'XX', 'XX'], 'N': [33, 40, 'XX', 42, 43],
                          'B': ['XX', 8, 5, 'XX', 1], 'G': [49, 55, 'XX', 56, 54]})


from random import randint

# make_bingo_card() returns a randomized Bingocard
# make_bingo_card: None -> Bingocard
def make_bingo_card():
    interval_width = 15
    card = {}
    for i in range(5):
        L = []
        while len(L) < 5:
            n = randint(interval_width*i+1,interval_width*(i+1))
            if not n in L:
                L.append(n)
                
        if i == 0:
            card['B'] = L
        elif i == 1:
            card['I'] = L
        elif i == 2:
            L[2] = 'XX'
            card['N'] = L
        elif i == 3:
            card['G'] = L
        else:
            card['O'] = L
    
    return card




