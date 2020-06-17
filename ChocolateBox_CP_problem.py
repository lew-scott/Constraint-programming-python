# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 13:33:13 2020

@author: pm11lms
"""


import constraint

def ChocolateBox(): # at least 6 milk, at least 3 but no more than 5 white, at least 3 but no more than 5 dark, 
                    # at least 2 of others and 15 total mixed, max volume 25 x 25 x 3 cm, max price £8. 
    """             type      vol     value     uLimt        richness     
    chocolate A     milk     4x4x3     0.1     vol -> 39        1 
    chocolate B     white    4x4x3     0.2     vol -> 39        2
    chocolate C     dark    4x4x2.5    0.3    value -> 26       5
    chocolate D    caramel   7x1x1     0.3   value -> 26        3
    chocolate E    praline  4x3.5x3    0.4    value -> 20       5
    chocolate F    coffee   4x3.5x3    0.25    value -> 32     2.5
    chocolate G     mint    3.5x3.5x3  0.2    value ->  40      2
    chocolate H    truffle  4x4x3      0.4   value -> 20       6
    """
    
    problem = constraint.Problem()
    problem.addVariable("A", range(6,40))
    problem.addVariable("B", range(3,40))
    problem.addVariable("C", range(3,27))
    problem.addVariable("D", range(2,27)) 
    problem.addVariable("E", range(2,21))
    problem.addVariable("F", range(2,33))
    problem.addVariable("G", range(2,41))
    problem.addVariable("H", range(2,21)) 
    
    def vol_constraint(a, b, c, d, e, f, g, h):
        if (a*4*4*3   + b*4*4*3   + c*4*4*2.5   + d*7*1*1 +
            e*4*3.5*3 + f*4*3.5*3 + g*3.5*3.5*3 + h*4*4*3) <= 25*25*3:
            return True 
    
    def value_constraint(a, b, c, d, e, f, g, h):
        if a*0.1 + b*0.2 + c*0.3 + d*0.3 + e*0.4 + f*0.25 + g*0.2 + h*0.4 <= 8: 
            return True

    def white_choc(b):
        if b <= 5:
            return True
        
    def dark_choc(c):
        if c <= 5:
            return True
        
    def mix_flavours(d, e, f, g, h):
        if d + e + f + g + h <= 15:
            return True
        
    problem.addConstraint(vol_constraint, "ABCDEFGH")
    problem.addConstraint(value_constraint, "ABCDEFGH")
    problem.addConstraint(white_choc, "B")
    problem.addConstraint(dark_choc, "C")
    problem.addConstraint(mix_flavours, "DEFGH")
    solutions = problem.getSolutions()
    
    
    mRichness = 0
    mCount = 0
    luxury_box = {}
    value_box = {}
    
    for s in solutions:
        Richness = s["A"]*1 + s["B"]*2 + s["C"]*5 + s["D"]*3 + s["E"]*5 + s["F"]*2.5 + s["G"]*2 + s["H"]*6
        if Richness > mRichness:
            mRichness = Richness
            luxury_box = s
    
    for s in solutions:
        c = s["A"] + s["B"] + s["C"] + s["D"] + s["E"] + s["F"]+ s["G"] + s["H"]
        if c > mCount:
            mCount = c
            value_box = s
            
    print("""  
    The luxury box contains:
    {} milk, {} white,
    {} dark, {} caramel,
    {} praline, {} coffee,
    {} mint, {} truffle
    """.format(luxury_box['A'], luxury_box['B'], luxury_box['C'], luxury_box['D'],
               luxury_box['E'], luxury_box['F'], luxury_box['G'], luxury_box['H']))
    print("""
    The value box contains:
    {} milk, {} white,
    {} dark, {} caramel,
    {} praline, {} coffee,
    {} mint, {} truffle
    """.format(value_box['A'], value_box['B'], value_box['C'], value_box['D'],
               value_box['E'], value_box['F'], value_box['G'], value_box['H']))
    
ChocolateBox()