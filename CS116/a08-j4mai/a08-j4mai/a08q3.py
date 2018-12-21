##===============================================
##   Jiadong Mai (20557203)
##   CS 116 Winter 2018
##   Assignment 08, Question 3
##===============================================

#q3
import math
import check
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
          
    
    
    #q3b
    
    # NOTE: for these functions you still need the full design recipe
    # however the Tests section will have to be done OUTSIDE of the class
    
    # __add__(self, other) consume 2 vectors, self and other, and return a new vector
    # __add__: Vector Vector -> Vector
    # Examples:
    # if u = Vector(2,3) and v = Vector(4,-1)
    # u + v => Vector(6,2)    
    def __add__(self,other):
        return Vector(self.x+other.x, self.y+other.y)    
    
    # __mul__(self, other) consume 2 vectors, self and other, and return an integer 
    # __mul__: Vector Vector -> Int
    # Examples:
    # if u = Vector(2,3) and v = Vector(4,-1)
    # u * v  => 5    
    def __mul__(self,other):
        return self.x*other.x + self.y*other.y
    
    # length(self) consume a single vector, self, and return a Float 
    # length: Vector -> Float
    # Examples:
    # if u = Vector(2,3) and v = Vector(4,-1)
    # u.length() => 3.6055....
    # v.length() => 4.1231....    
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # scale(self, k) consume a vector, self, and an integer, k, and mutate the vector 
    # scale: Vector Int -> None
    # Examples:
    # if u = Vector(2,3) and v = Vector(4,-1)
    # u.scale(-2) => None , u.x == -4, u.y == -6
    # v.scale(1) => None , v.x == 4, v.y == -1    
    def scale(self,k):
        self.x *= k
        self.y *= k


# Test(q3b): __add__
check.expect('T1(3b1)', Vector(2,3) + Vector(4,-1), Vector(6,2))
check.expect('T2(3b1)', Vector(0,0) + Vector(0,0), Vector(0,0))
check.expect('T3(3b1)', Vector(1,0) + Vector(1,-1), Vector(2,-1))
check.expect('T4(3b1)', Vector(-3,-3) + Vector(-9,-9), Vector(-12,-12))  
# Test(q3b): __mul__
check.expect('T1(3b2)',  Vector(2,3) * Vector(4,-1), 5)
check.expect('T2(3b2)',  Vector(0,0) * Vector(0,0), 0)
check.expect('T3(3b2)',  Vector(1,0) * Vector(1,-1), 1)
check.expect('T4(3b2)',  Vector(-3,-3) * Vector(-9,-9), 54)
# Test(q3b): self.length()
check.within('T1(3b3)', Vector(2,3).length(), 3.6055, 0.0001)
check.within('T2(3b3)', Vector(4,-1).length(), 4.1231, 0.0001)
check.within('T3(3b3)', Vector(0,0).length(), 0.0, 0.0001)
check.within('T4(3b3)', Vector(1,0).length(), 1.0, 0.0001)
check.within('T5(3b3)', Vector(1,-1).length(), 1.41421, 0.0001)
check.within('T6(3b3)', Vector(-3,-3).length(), 4.24264, 0.0001)
check.within('T7(3b3)', Vector(-3, 5).length(), 5.83095, 0.0001)

# Test(q3b): self.scale(k)
u = Vector(2,3)
check.expect('T1(3b4)', u.scale(-2), None)
check.expect('T1(3b4)(x)', u.x, -4)
check.expect('T1(3b4)(y)', u.y, -6)

a = Vector(-1,3)
check.expect('T2(3b4)', a.scale( -1), None)
check.expect('T2(3b4)(x)', a.x, 1)
check.expect('T2(3b4)(y)', a.y, -3)

b = Vector(0,0)
check.expect('T3(3b4)', b.scale(10), None)
check.expect('T3(3b4)(x)', b.x, 0)
check.expect('T3(3b4)(y)', b.y, 0)

c = Vector(-4,-6)
check.expect('T4(3b4)', c.scale( 3), None)
check.expect('T4(3b4)(x)', c.x, -12)
check.expect('T4(3b4)(y)', c.y, -18)

d = Vector(5,-2)
check.expect('T5(3b4)', d.scale(0), None)
check.expect('T5(3b4)(x)', d.x, 0)
check.expect('T5(3b4)(y)', d.y, 0)

e = Vector(0,6)
check.expect('T6(3b4)', e.scale(-5), None)
check.expect('T6(3b4)(x)', e.x, 0)
check.expect('T6(3b4)(y)', e.y, -30)

f = Vector(-2,0)
check.expect('T7(3b4)', f.scale(-1), None)
check.expect('T7(3b4)(x)', f.x, 2)
check.expect('T7(3b4)(y)', f.y, 0)

#q3a
# add_vectors(v1,v2) consume 2 vectors, v1 and v2, and return a new vector
# add_vectors: Vector Vector -> Vector
# Examples:
# if u = Vector(2,3) and v = Vector(4,-1)
# add_vectors(u,v) => Vector(6,2)
def add_vectors(v1,v2):
    new_vector = Vector(0,0)
    new_vector.x = v1.x + v2.x
    new_vector.y = v1.y + v2.y
    return new_vector
# Test:
check.expect('T1(3a1)', add_vectors(Vector(2,3), Vector(4,-1)), Vector(6,2))
check.expect('T2(3a1)', add_vectors(Vector(0,0), Vector(0,0)), Vector(0,0))
check.expect('T3(3a1)', add_vectors(Vector(1,0), Vector(1,-1)), Vector(2,-1))
check.expect('T4(3a1)', add_vectors(Vector(-3,-3), Vector(-9,-9)), Vector(-12,-12))

# dot_product(v1,v2) consume 2 vectors,v1 and v2, and return an integer 
# dot_product: Vector Vector -> Int
# Examples:
# if u = Vector(2,3) and v = Vector(4,-1)
# dot_product(u,v) => 5
def dot_product(v1,v2):
    result = v1.x*v2.x + v1.y*v2.y
    return result

# Test:
check.expect('T1(3a2)', dot_product(Vector(2,3), Vector(4,-1)), 5)
check.expect('T2(3a2)', dot_product(Vector(0,0), Vector(0,0)), 0)
check.expect('T3(3a2)', dot_product(Vector(1,0), Vector(1,-1)), 1)
check.expect('T4(3a2)', dot_product(Vector(-3,-3), Vector(-9,-9)), 54)

# length(vec) consume a single vector, vec, and return a Float 
# length: Vector -> Float
# Examples:
# if u = Vector(2,3) and v = Vector(4,-1)
# length(u) => 3.6055....
# length(v) => 4.1231....
def length(vec):
    result = math.sqrt(vec.x**2 + vec.y**2)
    return result

# Test:
check.within('T1(3a3)', length(Vector(2,3)), 3.6055, 0.0001)
check.within('T2(3a3)', length(Vector(4,-1)), 4.1231, 0.0001)
check.within('T3(3a3)', length(Vector(0,0)), 0.0, 0.0001)
check.within('T4(3a3)', length(Vector(1,0)), 1.0, 0.0001)
check.within('T5(3a3)', length(Vector(1,-1)), 1.41421, 0.0001)
check.within('T6(3a3)', length(Vector(-3,-3)), 4.24264, 0.0001)
check.within('T7(3a3)', length(Vector(-3, 5)), 5.83095, 0.0001)
    
# scale(vec, k) consume a vector, vec, and an integer, k, and mutate the vector 
# scale: Vector Int -> None
# Examples:
# if u = Vector(2,3) and v = Vector(4,-1)
# scale(u,-2) => None , u.x == -4, u.y == -6
# scale(v,1) => None , v.x == 4, v.y == -1
def scale(vec,k):
    vec.x = vec.x * k
    vec.y = vec.y * k

# Test:
u = Vector(2,3)
check.expect('T1(3a4)', scale(u, -2), None)
check.expect('T1(3a4)(x)', u.x, -4)
check.expect('T1(3a4)(y)', u.y, -6)

a = Vector(-1,3)
check.expect('T2(3a4)', scale(a, -1), None)
check.expect('T2(3a4)(x)', a.x, 1)
check.expect('T2(3a4)(y)', a.y, -3)

b = Vector(0,0)
check.expect('T3(3a4)', scale(b, 10), None)
check.expect('T3(3a4)(x)', b.x, 0)
check.expect('T3(3a4)(y)', b.y, 0)

c = Vector(-4,-6)
check.expect('T4(3a4)', scale(c, 3), None)
check.expect('T4(3a4)(x)', c.x, -12)
check.expect('T4(3a4)(y)', c.y, -18)

d = Vector(5,-2)
check.expect('T5(3a4)', scale(d, 0), None)
check.expect('T5(3a4)(x)', d.x, 0)
check.expect('T5(3a4)(y)', d.y, 0)

e = Vector(0,6)
check.expect('T6(3a4)', scale(e, -5), None)
check.expect('T6(3a4)(x)', e.x, 0)
check.expect('T6(3a4)(y)', e.y, -30)

f = Vector(-2,0)
check.expect('T7(3a4)', scale(f, -1), None)
check.expect('T7(3a4)(x)', f.x, 2)
check.expect('T7(3a4)(y)', f.y, 0)

