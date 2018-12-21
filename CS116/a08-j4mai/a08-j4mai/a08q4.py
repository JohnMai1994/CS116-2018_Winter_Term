##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 08, Question 4
##===============================================

#q4
import math
import check

acute_cat = 'ACUTE'
obtuse_cat = 'OBTUSE'
right_cat = 'RIGHT'
par_cat = 'PARALLEL'

class Vector:
    '''Fields: x(Int), y(Int)'''
    def __init__(self,xVal,yVal):
        self.x = xVal
        self.y = yVal
        
    def __eq__(self,other):
        if isinstance(other,Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __repr__(self):
        return "Vector({0},{1})".format(self.x,self.y)
    
    def __add__(self,other):
        return Vector(self.x+other.x, self.y+other.y)
    
    def __mul__(self,other):
        return self.x*other.x + self.y*other.y
    
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def scale(self,k):
        self.x *= k
        self.y *= k


# classify_angles(lov, vec): consumes a list of non_zero vectors, lov, and
#   a single non-zero vector, vec, and returns a dictionary contain 4 keys, 
#   'ACUTE', 'OBTUSE', 'RIGHT', 'PARALLEL'
# classify_angles: (listof Vector) Vector -> (dictof Str (listof Vector))
# Requires:
# both lov and vec are non-zero vectors
# Examples:
# if vecs = [Vector(-4,0), Vector(0,-7), Vector(10,5), Vector(-1,7),\
#            Vector(-5,-3), Vector(4,-6), Vector(-1,7),Vector(-9,3)]
# classify_angles(vecs ,Vector(3,0)) => {'ACUTE': [Vector(10,5), Vector(4,-6)],
#                                        'OBTUSE': [Vector(-1,7), Vector(-5,-3), Vector(-9,3)],
#                                        'RIGHT': [Vector(0,-7)], 'PARALLEL': [Vector(-4,0)]}
# classify_angles(vecs ,Vector(-2,3)) => {'ACUTE': [Vector(-4,0), Vector(-1,7), Vector(-5,-3), Vector(-9,3)],
#                                         'OBTUSE': [Vector(0,-7), Vector(10,5)], 'RIGHT': [],
#                                         'PARALLEL': [Vector(4,-6)]}

def classify_angles(lov,vec):
    result = {acute_cat: [], obtuse_cat: [], right_cat: [], par_cat: []}
    
    for k in lov:
        cos = (k * vec) / (k.length() * vec.length())
        if (k*vec)**2 == (k.x**2 + k.y**2)*(vec.x**2 + vec.y**2):
            if k in result[par_cat]:
                None
            else:
                result[par_cat].append(k)
        elif -1<cos<0:
            if k in result[obtuse_cat]:
                None
            else:
                result[obtuse_cat].append(k)
        elif cos == 0:
            if k in result[right_cat]:
                None
            else:
                result[right_cat].append(k)
        elif cos <1:
            if k in result[acute_cat]:
                None
            else:
                result[acute_cat].append(k)
    return result
                
# Test: 

a = [Vector(-4,0), Vector(-3,4), Vector(-6,-5)]
b = [Vector(-4,0), Vector(0,-7), Vector(10,5), Vector(-1,7),\
     Vector(-5,-3), Vector(4,-6), Vector(-1,7),Vector(-9,3)]
c = [Vector(1,1), Vector(2,2), Vector(-1,-1)]

# contain one of the keys in lov
check.expect('Acute', classify_angles(a, Vector(-1,1)),\
             {acute_cat: [Vector(-4,0), Vector(-3,4), Vector(-6,-5)], obtuse_cat: [], right_cat: [], par_cat: []})
check.expect('Vector', classify_angles(a, Vector(6,1)),\
             {acute_cat: [], obtuse_cat: [Vector(-4,0), Vector(-3,4), Vector(-6,-5)], right_cat: [], par_cat: []})
check.expect('Parallel', classify_angles(c, Vector(9,9)),\
             {acute_cat: [], obtuse_cat: [], right_cat: [], par_cat: [Vector(1,1), Vector(2,2), Vector(-1,-1)]})
check.expect('Right', classify_angles(c, Vector(-9,9)),\
             {acute_cat: [], obtuse_cat: [], right_cat: [Vector(1,1), Vector(2,2), Vector(-1,-1)], par_cat:[] })
# contain two of the keys in lov
check.expect('Right & Obtuse', classify_angles(a, Vector(4,3)),\
             {acute_cat: [], obtuse_cat: [Vector(-4,0), Vector(-6,-5)], right_cat: [Vector(-3,4)], par_cat: []})
# contain three of the keys in lov
check.expect('Acute, Obtuse and Parallel', classify_angles(b, Vector(-2,3)), \
             {'ACUTE': [Vector(-4,0), Vector(-1,7), Vector(-5,-3), Vector(-9,3)],
             'OBTUSE': [Vector(0,-7), Vector(10,5)], 'RIGHT': [],
             'PARALLEL': [Vector(4,-6)]})             
# contain all in lov
check.expect('All', classify_angles(b, Vector(3,0)), {'ACUTE': [Vector(10,5), Vector(4,-6)],
                                                      'OBTUSE': [Vector(-1,7), Vector(-5,-3), Vector(-9,3)],
                                                      'RIGHT': [Vector(0,-7)], 'PARALLEL': [Vector(-4,0)]})
        
        
   
        
        
