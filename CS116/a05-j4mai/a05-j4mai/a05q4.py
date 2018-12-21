##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 05, Question 4
##===============================================
import check

# Question 4
# is_folded(old, new) returns True if old could be 'folded' into new, otherwise,
#   False.
# is_folded: Str Str -> Bool
# Require:
# len(old) == len(new) and 
# neither len(old) or len(new) exceed 10
# Examples:
# is_folded('AACTC', 'ACATC') => True
# is_folded('ATGCA', 'ACTGA') => False
def is_folded(old, new):
  new_two = new[:2]
  if old == new:
    return True
  else:
    if old[0:2] == new_two:
      return is_folded(old[1:],new[1:])
    elif old[-1]+ old[-2] == new_two:
      return is_folded(old[:-1], new[1:])
    elif old[0] + old[-1] == new_two:
      return is_folded(old[1:], new[1:])
    elif old[-1] + old[0] == new_two:
      return is_folded(old[:-1], new[1:])
    else:
      return False
# Tests:
# Test1: Example Test:
check.expect('Q4T1', is_folded('AACTC', 'ACATC'), True)
check.expect('Q4T2', is_folded('ATGCA', 'ACTGA'), False)
# Test2: start -> start -> start:
check.expect('Q4T3', is_folded('AACTC', 'AACTC'), True)
check.expect('Q4T4', is_folded('AACTCABRQE', 'AACTCABRQE'), True)
check.expect('Q4T5', is_folded('AACTC', 'ACCTA'), False)
# Test3: end -> end ->end:
check.expect('Q4T6', is_folded('AACTC', 'CTCAA'), True)
check.expect('Q4T7', is_folded('AACTCATC', 'CTACTCAA'), True)
check.expect('Q4T8', is_folded('AACTCATC', 'CTACCTAA'), False)
# Test4: start -> end -> start:
check.expect('Q4T9', is_folded('AACTCATC', 'ACATCATC'), True)
check.expect('Q4T10', is_folded('ATGCAWEIR', 'ARTIGECWA'), True)
check.expect('Q4T11', is_folded('ATGCA', 'AATCG'), True)
check.expect('Q4T12', is_folded('ATGCA', 'AAGTC'), False)
# Test5: start -> end -> end -> start:
check.expect('Q4T13', is_folded('ATGCA', 'AACTG'), True)
check.expect('Q4T14', is_folded('AACTC', 'ACTAC'), True)
check.expect('Q4T15', is_folded('AACTCATC', 'ACTACACT'), True)
