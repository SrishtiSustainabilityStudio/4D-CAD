#Python library for geometry and mathematical computations
from sympy import *
from sympy.geometry import *
import math

# there can be 4 valid cases as follows :

# case1
# A --------------
# B   ----------

# case2
# A     --------------
# B   ----------------------

# case3
# A --------------
# B   -----------------

# case4
# A         --------------
# B   ----------

def FindProjectedLen(ls1,ls2) :

    if not ls1.is_parallel(ls2) :
        return Decimal(0)

    x2,y2 = ls2.points
    # for case 1,case 3 and case 4
    if ls1.contains(ls1.projection(x2)) or ls1.contains(ls1.projection(y2)) :
        s = ls1.projection(ls2)
        # print "s1 : ",s
        return min(s.length,min(ls1.length,ls2.length))

    x1,y1 = ls1.points
    # for case 2
    if ls2.contains(ls2.projection(x1)) or ls2.contains(ls2.projection(y1)) :
        s = ls2.projection(ls1)
        # print "s2 : ",s
        return min(s.length,min(ls1.length,ls2.length))

    return 0.0

def FindPrependicularDistance(ls1,ls2) :
    if not ls1.is_parallel(ls2) :
        return Decimal(0)

    x2,y2 = ls2.points
    # for case 1,case 3 and case 4
    if ls1.contains(ls1.projection(x2)) or ls1.contains(ls1.projection(y2)) :
        s = ls1.perpendicular_segment(x2)
        return s.length

    x1,y1 = ls1.points
    # for case 2
    if ls2.contains(ls2.projection(x1)) or ls2.contains(ls2.projection(y1)) :
        s = ls2.perpendicular_segment(x1)
        return s.length