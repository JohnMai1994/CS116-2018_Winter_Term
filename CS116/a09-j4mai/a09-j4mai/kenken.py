##===============================================  
##   Jiadong Mai (20557203)  
##   CS 116 Winter 2018  
##   Assignment 09  
##===============================================

import check
import copy   

class Puzzle:
    '''
    Fields:
            size: Nat 
            board: (listof (listof (anyof Str Nat Guess))
            constraints: (listof (list Str Nat (anyof '+' '-' '*' '/' '='))))
    requires: See Assignment Specifications
    '''
    
    def __init__(self, size, board, constraints):
        self.size=size
        self.board=board
        self.constraints=constraints
        
    def __eq__(self, other):
        return (isinstance(other,Puzzle)) and \
            self.size==other.size and \
            self.board == other.board and \
            self.constraints == other.constraints
    
    def __repr__(self):
        s='Puzzle(\nSize='+str(self.size)+'\n'+"Board:\n"
        for i in range(self.size):
            for j in range(self.size):
                if isinstance(self.board[i][j],Guess):
                    s=s+str(self.board[i][j])+' '
                else:
                    s=s+str(self.board[i][j])+' '*7
            s=s+'\n'
        s=s+"Constraints:\n"
        for i in range(len(self.constraints)):
            s=s+'[ '+ self.constraints[i][0] + '  ' + \
                str(self.constraints[i][1]) + '  ' + self.constraints[i][2]+ \
                ' ]'+'\n'
        s=s+')'
        return s    

class Guess:
    '''
    Fields:
            symbol: Str 
            number: Nat
    requires: See Assignment Specifications
    '''        
    
    def __init__(self, symbol, number):
        self.symbol=symbol
        self.number=number
        
    def __repr__(self):
        return "('{0}',{1})".format(self.symbol, self.number)
    
    def __eq__(self, other):
        return (isinstance(other, Guess)) and \
            self.symbol==other.symbol and \
            self.number == other.number        

class Posn:
    '''
    Fields:
            y: Nat 
            y: Nat
    requires: See Assignment Specifications
    '''         
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return "({0},{1})".format(self.x, self.y)
    
    def __eq__(self,other):
        return (isinstance(other, Posn)) and \
            self.x==other.x and \
            self.y == other.y 
    
    

## Constants used for tests
    
puzzle1 = Puzzle(4, [['a','b','b','c'],
                     ['a','d','e','e'],
                     ['f','d','g','g'],
                     ['f','h','i','i']],
                 [['a', 6,'*'],
                  ['b',3,'-'],
                  ['c',3,'='],
                  ['d',5,'+'],
                  ['e',3,'-'],
                  ['f',3, '-'],
                  ['g',2,'/'],
                  ['h',4,'='],
                  ['i',1,'-']])

puzzle1partial=Puzzle(4, [['a','b','b','c'],
                          ['a',2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

# a partial solution to puzzle1 with a cage partially filled in
puzzle1partial2=Puzzle(4, [[Guess('a',2),'b','b','c'],
                          ['a',2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

# a partial solution to puzzle1 with a cage partially filled in
#   but not yet verified 
puzzle1partial3=Puzzle(4, [[Guess('a',2),'b','b','c'],
                          [Guess('a',3),2,1,4],
                          ['f',3,'g','g'],
                          ['f','h','i','i']],
                      [['a', 6,'*'],
                       ['b',3,'-'],
                       ['c',3,'='],
                       ['f',3, '-'],
                       ['g',2,'/'],
                       ['h',4,'='],
                       ['i',1,'-']])

# The solution to puzzle 1
puzzle1soln=Puzzle(4, [[2,1,4,3],[3,2,1,4],[4,3,2,1],[1,4,3,2]], [])

puzzle2=Puzzle(6,[['a','b','b','c','d','d'],
                  ['a','e','e','c','f','d'],
                  ['h','h','i','i','f','d'],
                  ['h','h','j','k','l','l'],
                  ['m','m','j','k','k','g'],
                  ['o','o','o','p','p','g']],
               [['a',11,'+'],
                ['b',2,'/'],
                ['c',20,'*'],
                ['d',6,'*'],
                ['e',3,'-'],
                ['f',3,'/'],
                ['g',9,'+'],
                ['h',240,'*'],
                ['i',6,'*'],
                ['j',6,'*'],
                ['k',7,'+'],
                ['l',30,'*'],
                ['m',6,'*'],
                ['o',8,'+'],
                ['p',2,'/']])
                
#  The solution to puzzle 2
puzzle2soln=Puzzle(6,[[5,6,3,4,1,2],
                      [6,1,4,5,2,3],
                      [4,5,2,3,6,1],
                      [3,4,1,2,5,6],
                      [2,3,6,1,4,5],
                      [1,2,5,6,3,4]], [])


puzzle3=Puzzle(2,[['a','b'],['c','b']],[['b',3,'+'],
                                       ['c',2,'='],
                                       ['a',1,'=']])

puzzle3partial=Puzzle(2,[['a',Guess('b',1)],['c',Guess('b',2)]],
                      [['b',3,'+'],
                       ['c',2,'='],
                       ['a',1,'=']])
                  
puzzle3soln=Puzzle(2,[[1,2],[2,1]],[])                  
                  
# part a)
## read_puzzle(fname) reads information from fname file and returns the info as 
## Puzzle value.
## read_puzzle: Str -> Puzzle

def read_puzzle(fname):
    file = open(fname, 'r')
    all_index = file.readlines()
    file.close()
    
    result = Puzzle(0, [], [])
    
    size = int(all_index[0].strip('\n'))
    
    board_line = all_index[1: size+1]
    board = []
    for line in board_line:
        lst = line.split(' ')
        lst[-1] = lst[-1].strip('\n')
        board.append(lst)
    
    constraints_line = all_index[size+1:]
    constraints = []
    for line in constraints_line:
        lst = line.split(' ')
        lst[-1] = lst[-1].strip('\n')
        lst[1] = int(lst[1])
        constraints.append(lst)        
    
    result = Puzzle(size, board, constraints)
    return result
    
    

check.expect("Ta1", read_puzzle("inp1.txt"), puzzle1)
check.expect("Ta2", read_puzzle("inp2.txt"), puzzle2) 
check.expect("Ta3", read_puzzle("inp3.txt"), puzzle3) 


#part b)
## print_sol(puz, fname) prints the Puzzle puz in fname file
## print_sol: Puzzle Str -> None

def print_sol(puz, fname):
    output_file = open(fname, 'w')
    require = puz.board
    for z in require:
        lst = []
        for f in z:
            k = str(f)
            lst.append(k)
        
        k = '  '.join(list(lst)) + '  \n'
        output_file.write(k)
    output_file.close()
    


check.expect("Tb1", print_sol(puzzle1soln, "out1.txt"), None)
check.set_file_exact("out1.txt", "result.txt")

check.expect("Tb2", print_sol(puzzle2soln, "out2.txt"), None)
check.set_file_exact("out2.txt", "result2.txt")

check.expect("Tb3", print_sol(puzzle3soln, "out3.txt"), None)
check.set_file_exact("out3.txt", "result3.txt")

    

#part c)
## find_blank(puz) returns the position of the first blank
## space in puz, or False if no cells are blank.  If the first constraint has
## only guesses on the board, find_blank returns 'guess'.  
## find_blank: Puzzle -> (anyof Posn False 'guess')
## Examples:
## find_blank(puzzle1) => Posn(0 0)
## find_blank(puzzle3partial) => 'guess'
## find_blank(puzzle2soln) => False

def find_blank(puz):
    if puz.constraints == []:
        return False
    target = puz.constraints[0][0]
    board_line = puz.board
    
    col = 0
    for list_value in board_line:
        row = 0
        for value in list_value:
            if target == value:
                return Posn(row, col)
            row += 1
        col += 1

    for list_value in board_line:
        row = 0
        for value in list_value:
            if (type(value) is Guess) and value.symbol == target:
                return 'guess'
            row += 1
        col += 1    

        
    return False
    
check.expect("Tc1", find_blank(puzzle1),Posn(0,0))
check.expect("Tc2", find_blank(puzzle1soln),False)
check.expect("Tc3", find_blank(puzzle1partial),  Posn(0,0))
check.expect("Tc4", find_blank(puzzle1partial2),  Posn(0,1))
check.expect("Tc5", find_blank(puzzle1partial3),  'guess')

check.expect("Tc6", find_blank(puzzle3),  Posn(1,0))
check.expect("Tc7", find_blank(puzzle3partial),  'guess')
check.expect("Tc8", find_blank(puzzle3soln), False)

check.expect("Tc9", find_blank(puzzle2),Posn(0,0))
check.expect("Tc10", find_blank(puzzle2soln),False)
check.expect("Tc11", find_blank(Puzzle(3, [["b","c","a"],["a","a","a"],
                                          ["d","a","e"]],
                                          [["a",18,"*"],["b",1,"="],["c",2,"="],
                                           ["d",3,"="],["e",1,"="]])), 
             Posn(2,0))
check.expect("Tc12",find_blank(Puzzle(3, 
                                     [[1,2,"d"],[Guess("b",2),3,Guess("b",1)],
                                      [Guess("b",3),Guess("b",1),Guess("b",2)]],
                                     [["b",12,"*"],["d",3,"="]])), 'guess')
check.expect('Tc13', find_blank(Puzzle(3,
                                       [['a', 3, 'b'],
                                        ['a', 'b', 'b'],
                                        ['c', 'd', 'e']],
                                       [['e', 6, '='], ['a', 5, '+'], ['b', 4, '*'],
                                        ['c', 2, '='], ['d', 1, '=']])), Posn(2,2))


#part d)
## used_in_row(puz, pos) returns a list of numbers used in the same 
## row as (x,y) position, pos, in the given puz.  
## used_in_row: Puzzle Posn -> (listof Nat)
## Example: 
## used_in_row(puzzle1,Posn(1,1)) => []
## used_in_row(puzzle1partial2,Posn(0,1)) => [1,2,4]

def used_in_row(puz,pos):
    need_row = pos.y
    need_line = puz.board[need_row]
    
    result = []
    for k in need_line:
        if type(k) is int:
            result.append(k)
        elif type(k) is Guess:
            result.append(k.number)
    
    result.sort()
    return result
            
        


check.expect("Td1", used_in_row(puzzle1,Posn(1,1)), [])
check.expect("Td2", used_in_row(puzzle1partial2,Posn(0,1)), [1,2,4])
check.expect("Td3", used_in_row(puzzle1partial3,Posn(0,0)), [2])
check.expect("Td4", used_in_row(puzzle1soln,Posn(2,1)), [1,2,3,4])
check.expect("Td5", used_in_row(puzzle1partial3,Posn(0,1)), [1,2,3,4])
check.expect("Td6", used_in_row(puzzle2,Posn(0,1)), [])
check.expect("Td7", used_in_row(Puzzle(3,[[1,2,'d'],['b',3,'b'],
                                          ['b','b','b']],
                                       [['b',12,'*'],['d',3,'=']])
                                       ,Posn(0,1)), [3])



## used_in_col(puz, pos) returns a list of numbers used in the same 
## column as (x,y) position, pos, in the given puz.  
## used_in_col: Puzzle Posn -> (listof Nat)
## Examples:
## used_in_col(puzzle1partial2,Posn(1,0)) => [2,3]
## used_in_col(puzzle2soln,Posn(3,5)) => [1,2,3,4,5,6]

def used_in_col(puz,pos):
    need_col = pos.x
    
    result = []
    for k in puz.board:
        target = k[need_col]
        if type(target) is int:
            result.append(target)
        elif type(target) is Guess:
            result.append(target.number)
    
    result.sort()
    return result
 

check.expect("Td8", used_in_col(puzzle1partial2,Posn(1,0)), [2,3])  
check.expect("Td9", used_in_col(puzzle2soln,Posn(3,5)), [1,2,3,4,5,6])  
check.expect("Td10", used_in_col(puzzle1partial2,Posn(0,1)), [2])
check.expect("Td11", used_in_col(puzzle1partial3,Posn(0,0)), [2,3])
check.expect("Td12", used_in_col(puzzle1soln,Posn(2,1)), [1,2,3,4])
check.expect("Td13", used_in_col(puzzle1partial3,Posn(3,1)), [4])
check.expect("Td14", used_in_col(puzzle2,Posn(0,1)), [])
check.expect("Td15", used_in_col(Puzzle(3,[[1,2,'d'],['b',3,'b'],
                                          ['b','b','b']],
                                       [['b',12,'*'],['d',3,'=']])
                                       ,Posn(0,1)), [1])

#part e)
##available_vals(puz,pos) returns a list of valid entries for the (x,y)  
## position, pos, of the consumed puzzle, puz.  
## available_vals: Puzzle Posn -> (listof Nat)
## Examples:
## available_vals(puzzle1partial, Posn(2,2)) => [2,4]
## available_vals(puzzle1partial2, Posn(0,1)) => [3]

def available_vals(puz,pos):
    used_row = used_in_row(puz, pos)
    used_col = used_in_col(puz, pos)
    all_used = used_row + used_col
    available = list(range(1, puz.size+1))
    for k in all_used:
        available = list(filter(lambda x: x != k, available))
    
    return available

check.expect("Te1", available_vals(puzzle1, Posn(3,1)), [1,2,3,4])
check.expect("Te2", available_vals(puzzle1partial, Posn(2,2)), [2,4])
check.expect("Te3", available_vals(puzzle1partial2, Posn(0,1)), [3])
check.expect("Te4", available_vals(puzzle1soln, Posn(2,1)), [])
check.expect("Te5", available_vals(puzzle2, Posn(0,1)), [1,2,3,4,5,6])
check.expect("Te6", available_vals(puzzle2soln, Posn(4,5)), [])
check.expect("Te7", available_vals(puzzle3partial, Posn(0,1)), [1])

             

# part f)  
## place_guess(brd,pos,val) fills in the (x,y) position, pos, of the board, brd, 
## with the a guess with value, val
## place_guess: (listof (listof (anyof Str Nat Guess))) Posn Nat 
##              -> (listof (listof (anyof Str Nat Guess)))
## Examples:
## See provided tests


def place_guess(brd,pos,val):
    res=copy.deepcopy(brd) # a copy of brd is assigned to res without any 
                           # aliasing to avoid mutation of brd. 
                           #  You should update res and return it
    target = res[pos.y][pos.x]
    built_guess = Guess(target, val)
    res[pos.y][pos.x] = built_guess
    
    return res



check.expect("Tf1", place_guess(puzzle3.board, Posn(1,1),2), 
             [['a','b'],['c',Guess('b',2)]])
check.expect("Tf2", place_guess(puzzle1partial2.board, Posn(0,1),3), 
             puzzle1partial3.board)
check.expect("Tf3", place_guess(puzzle1.board, Posn(3,1),5), 
             [['a', 'b', 'b', 'c'], ['a', 'd', 'e', Guess('e', 5)], ['f', 'd', 'g', 'g'], ['f', 'h', 'i', 'i']])
check.expect("Tf4", place_guess(puzzle1partial3.board, Posn(3,3),5), 
             [[Guess('a',2), 'b', 'b', 'c'], [Guess('a',3), 2, 1, 4], ['f', 3, 'g', 'g'], ['f', 'h', 'i', Guess('i', 5)]])


#  **********  DO NOT CHANGE THIS FUNCTION ******************

# fill_in_guess(puz, pos, val) fills in the pos Position of puz's board with 
# a guess with value val
# fill_in_guess: Puzzle Posn Nat -> Puzzle
# Examples: See provided tests

def fill_in_guess(puz, pos, val):
    res=Puzzle(puz.size, copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    tmp=copy.deepcopy(res.board)
    res.board=place_guess(tmp, pos, val)
    return res


check.expect("Tf5", fill_in_guess(puzzle1, Posn(3,2),5), 
             Puzzle(4,[['a','b','b','c'],
                      ['a','d','e','e'],
                      ['f','d','g',Guess('g',5)],
                      ['f','h','i','i']], puzzle1.constraints))
check.expect("Tf6", fill_in_guess(puzzle1, Posn(2,0),4), 
             Puzzle(4,[['a','b',Guess('b',4),'c'],
                      ['a','d','e','e'],
                      ['f','d','g','g'],
                      ['f','h','i','i']], puzzle1.constraints))
check.expect("Tf7", fill_in_guess(puzzle1partial2, Posn(0,1),1), 
             Puzzle(4,[[Guess('a',2),'b','b','c'],
                       [Guess('a',1),2,1,4],
                       ['f',3,'g','g'],
                       ['f','h','i','i']], puzzle1partial2.constraints))

#  *************************************************************************             

# part g)
## guess_valid(puz) determines if the guesses in puz satisfy their constraint
## guess_valid: Puzzle -> Bool
## Examples: See provided tests

def guess_valid(puz):
    calculate = puz.constraints[0][2]
    target_number = puz.constraints[0][1]
    target_alp = puz.constraints[0][0]
    board = puz.board
    lst = []
    for a in board:
        for b in a:
        
            if type(b) is Guess and b.symbol == target_alp:
                lst.append(b.number)    
    we_get = 0
    if calculate == '/':
        lst.sort()
        if target_number == lst[1] / lst[0]:
            return True
        False
    elif calculate == '+':
        for a in lst:
            we_get += a
        return target_number == we_get
    elif calculate == '*':
        we_get = 1
        for a in lst:
            we_get = we_get* a
        return target_number == we_get
    elif calculate == '-':
        lst.sort()
        if target_number == lst[1] - lst[0]:
            return True
    elif calculate == '=':
        return lst[0] == target_number




    
check.expect("Tg1", guess_valid(puzzle3partial), True)
check.expect("Tg2", guess_valid(Puzzle(3,[['a','a',3],
                                          ['a',Guess('b',1),2],
                                          ['a',Guess('b',3),1]],
                                       [['b',3,'/'],['a',8,'+']])), True)
check.expect("Tg3", guess_valid(Puzzle(2,[[Guess('a',2),Guess('a',1)],
                                          [Guess('a',1),Guess('a',2)]],
                                       [['a',4,'+']])), False)

check.expect("Tg4", guess_valid(Puzzle(3,[[Guess('a',1),Guess('a',2),3],
                                          [Guess('a',3),1,2],
                                          [Guess('a',2),3,1]],
                                       [['a',8,'+']])), True)
check.expect("Tg5", guess_valid(Puzzle(3,[[Guess('a',2),Guess('a',2),3],
                                          [Guess('a',3),1,2],
                                          [Guess('a',2),3,1]],
                                       [['a',8,'+']])), False)
check.expect('Tg6', guess_valid(Puzzle(2,[['a', 'b'],['a',Guess('c',1)]], [['c',1,'='], \
                                                                 ['b', 2, '='],
                                                                 ['a', 3, '+']])),
             True)
check.expect('Tg7', guess_valid(Puzzle(2,[[Guess('a',1), 2],[Guess('a',2),1]], [['a', 2, '*']])),
             True)
check.expect('Tg8', guess_valid(Puzzle(2,[[Guess('a',3), 2],[Guess('a',2),1]], [['a', 2, '*']])),
             False)
check.expect('Tg9', guess_valid(Puzzle(2,[[Guess('a',1), 2],[Guess('a',2),1]], [['a', 1, '-']])),
             True)



# part h) 
## apply_guess(puz) converts all guesses in puz into their corresponding numbers
## and removes the first contraint from puz's list of contraints
## apply_guess:  Puzzle -> Puzzle
## Examples: See provided tests

def apply_guess(puz):
    # a copy of puz is assigned to res without any 
    # aliasing to avoid mutation of puz. 
    #  You should update res and return it    
    res=Puzzle(puz.size, copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    board = res.board
    a = 0
    for line in board:
        b = 0
        for target in line:
            if type(target) is Guess:
                res.board[a][b] = target.number
            b += 1
        a += 1
    
    res.constraints = res.constraints[1:]
    return res
    



check.expect("Th1", apply_guess(Puzzle(6,[[5,6,3,4,1,2],[6,1,4,5,2,3],
                                          [4,5,2,3,6,1],[3,4,1,2,5,6],
                                          [2,3,6,1,4,5],
                                          [1,2,5,Guess('p',6),Guess('p',3),4]],
                                       [['p',2,'/']])), puzzle2soln)

                               
                               

# part i)
## neighbours(puz) returns a list of next puzzles after puz in
## the implicit graph
## neighbours: Puzzle -> (listof Puzzle)
## Examples: See provided tests

def neighbours(puz):
    # a copy of puz is assigned to tmp without any 
    # aliasing to avoid mutation of puz. 
    tmp=Puzzle(puz.size, copy.deepcopy(puz.board), 
               copy.deepcopy(puz.constraints))
    
    result = []
    if type(find_blank(tmp)) is Posn:
        target_posn = find_blank(tmp)
        target_avail = available_vals(tmp, target_posn)
        for a in target_avail:
            puzzle = fill_in_guess(tmp, target_posn, a)
            result.append(puzzle)
            
    elif find_blank(tmp) == 'guess':
        if guess_valid(tmp):
            puzzle = apply_guess(tmp)
            result.append(puzzle)
    
    return result
    
    

check.expect("Ti1", neighbours(puzzle2soln), [])
check.expect("Ti2", neighbours(puzzle3), [Puzzle(2,[['a',Guess('b',1)],
                                                    ['c','b']],
                                                 [['b',3,'+'], ['c',2,'='],
                                                  ['a',1,'=']]),
                                          Puzzle(2,[['a',Guess('b',2)],
                                                    ['c','b']],[['b',3,'+'],
                                                                ['c',2,'='],
                                                                ['a',1,'=']])])

puz1=Puzzle(4,[[4,2,'a','a'],['b', Guess('c',3),'a',4],
               ['b', Guess('c',1),Guess('c',4),2],
               [1,Guess('c',4),Guess('c',2),3]],
            [['c',96,'*'],['b',5,'+'],['a',3,'*']])

puz2=Puzzle(4,[[4,2,'a','a'],['b',3,'a',4],['b',1,4,2],
               [1,4,2,3]],[['b',5,'+'],['a',3,'*']])
check.expect("Ti3",neighbours(puz1),[puz2])


# ******** DO NOT CHANGE THIS PART ***************
# ************** THE MAIN FUNCTION ***************
## solve_kenken(orig) finds the solution to a KenKen puzzle,
## orig, or returns False if there is no solution.  
## solve-kenken: Puzzle -> (anyof Puzzle False)
## Examples: See provided tests




def solve_kenken(orig):
    to_visit=[]
    visited=[]
    to_visit.append(orig)
    while to_visit!=[] :
        if find_blank(to_visit[0])==False:
            return to_visit[0]
        elif to_visit[0] in visited:
            to_visit.pop(0)
        else:
            nbrs = neighbours(to_visit[0])
            new = list(filter(lambda x: x not in visited, nbrs))
            new_to_visit=new + to_visit[1:] 
            new_visited= [to_visit[0]] + visited
            to_visit=new_to_visit
            visited=new_visited     
    return False


solve_kenken(puzzle3)



check.expect("game1",solve_kenken(puzzle3partial),False)
check.expect("game2",solve_kenken(puzzle1), puzzle1soln)
check.expect("game3",solve_kenken(puzzle2), puzzle2soln)
check.expect("game4",solve_kenken(puzzle3), puzzle3soln)
check.expect("game5",solve_kenken(puzzle3soln), puzzle3soln)

puzzle5 = Puzzle(4, [['a','b', 'b', 'c'],
                     ['d','d', 'e', 'c'],
                     ['f', 'f', 'e', 'c'],
                     ['f', 'g','g', 'h']],
                 [['a', 1,'='],
                  ['b',1,'-'],
                  ['c',7,'+'],
                  ['d',2,'-'],
                  ['e',7,'+'],
                  ['f',8,'+'],
                  ['g',3,'-'],
                  ['h',3,'=']])
check.expect('game5', solve_kenken(puzzle5), Puzzle(4,[[1,3,2,4],[3,1,4,2],[4,2,3,1],[2,4,1,3]],[]))
