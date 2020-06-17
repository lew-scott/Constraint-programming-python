# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 19:51:48 2020

@author: pm11lms
"""

import constraint

def p1():
    problem = constraint.Problem()
    problem.addVariable('x', [1,2,3])
    problem.addVariable('y', range(10))
    
    def our_constraint(x, y):
        if x + y >= 5:
            return True
    
    
    problem.addConstraint(our_constraint, ['x','y'])
    solutions = problem.getSolutions()
    # Prettier way to print and see all solutions
    length = len(solutions)
    print("(x,y) ∈ {", end="")
    for index, solution in enumerate(solutions):
        if index == length - 1:
            print("({},{})".format(solution['x'], solution['y']), end="")
        else:
            print("({},{}),".format(solution['x'], solution['y']), end="")
    print("}")


def p2(): # two + two = four
    problem = constraint.Problem()
    problem.addVariables("TF", range(1, 10))
    problem.addVariables("WOUR", range(10))

    # Telling Python that we need TWO + TWO = FOUR
    def sum_constraint(t, w, o, f, u, r):
        if 2*(t*100 + w*10 + o) == f*1000 + o*100 + u*10 + r:
            return True
    
    problem.addConstraint(sum_constraint, "TWOFUR")
    problem.addConstraint(constraint.AllDifferentConstraint())

    solutions = problem.getSolutions()
    print("Number of solutions found: {}\n".format(len(solutions)))
    
    # .getSolutions() returns a dictionary
    for s in solutions:
        print("T = {}, W = {}, O = {}, F = {}, U = {}, R = {}"
            .format(s['T'], s['W'], s['O'], s['F'], s['U'], s['R']))
        
        
def p3(): # ways of making 60 
    problem = constraint.Problem() 
    problem.addVariable("1p", range(61)) # range 0-60 
    problem.addVariable("3p", range(21)) 
    problem.addVariable("5p", range(13))
    problem.addVariable("10p", range(7))
    problem.addVariable("20p", range(4))

    problem.addConstraint(
        constraint.ExactSumConstraint(60,[1,3,5,10,20]),
            ["1p","3p","5p","10p","20p"]
            )
    
    def print_solutions(solutions):
        for s in solutions:
            print(format(s["1p"], s["3p"], s["5p"], s["10p"], s["20p"]))
    solutions = problem.getSolutions()
    #print_solutions(solutions)
    print("Total number of ways: {}".format(len(solutions)))

def p4(): # CRASH + ERROR + REBOOT = HACKER
        problem = constraint.Problem() 
        problem.addVariables("CERH", range(1,10))
        problem.addVariables("ASOBTK", range(10))
        def sum_constraints( c, r, a, s, h, e, o, b, t, k ):
            if (10000*c + 1000*r + 100*a + 10*s + h +
                10000*e + 1000*r + 100*r + 10*o + r + 
                100000*r + 10000*e + 1000*b + 100*o + 10*o + t == 
                100000*h + 10000*a + 1000*c + 100*k + 10*e + r):
                return True
        
        problem.addConstraint(sum_constraints, "CRASHEOBTK" )
        problem.addConstraint(constraint.AllDifferentConstraint())
        
        solutions = problem.getSolution()
        # .getSolutions() returns a dictionary
        print(*solutions.items(), sep='\n')
        return solutions

def p5(): # chocolates -> max sweetness combination by mass (3kg), vol (1 dm^3 -> L) and value (v < 300)
    '''         mass      vol      sweetness   value
    Chocolate A	100	 8 × 2.5 × 0.5   10	        8    -> upper bound is weight 30
    Chocolate B	45	 7 × 2 × 0.5	  8        6.8   -> upper bound is value 45
    Chocolate C	10	 3 × 2 × 0.5	 4.5	    4    -> upper bound is value 75
    Chocolate D	25	 3 × 3 × 0.5	 3.5	    3    -> upper bound is value 100
    '''
    
    problem = constraint.Problem()
    problem.addVariable("A", range(31))
    problem.addVariable("B", range(45))
    problem.addVariable("C", range(75))
    problem.addVariable("D", range(100))
    
    def mass_constraint(a , b, c, d):
        if a*100 + b*45 + c*10 + d*25 <= 3000: 
            return True
    
    def vol_constraint(a, b, c, d):
        if a*8*2.5*0.5 + b*7*2*0.5 + c*3*2*0.5 + d*3*3*0.5 <= 1000:
            return True
        
    def value_constraint(a, b, c, d):
        if a*8 + b*6.8 + c*4 + d*3  < 300:
            return True
        
        
    problem.addConstraint(mass_constraint, "ABCD")
    problem.addConstraint(vol_constraint, "ABCD")
    problem.addConstraint(value_constraint, "ABCD")
    
    mSweetness = 0
    solution_found = {}
    solutions = problem.getSolutions()
    
    for s in solutions:
        cSweetness = s["A"]*10 + s["B"]*8 + s["C"]*4.5 + s["D"]*3.5
        if cSweetness > mSweetness:
            mSweetness = cSweetness
            solution_found = s

    print("""
            The maximum sweetness we can bring is: {}
            We'll bring:
            {} A Chocolates,
            {} B Chocolates,
            {} C Chocolates,
            {} D Chocolates
            """.format(mSweetness, solution_found['A'], solution_found['B'], solution_found['C'], solution_found['D']))
            
        










 