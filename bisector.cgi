#!/usr/bin/env python
"""Find root in a function"""

import sys
import urlparse


class F(object):
    def __init__(self, func):
        self.func = func
    
    def f_of_x(self, x):
        return eval(self.func.replace('^', '**').replace('/', '*(1.0)/'))

    def find_root(self, lower, upper):
        if self.f_of_x(lower) * self.f_of_x(upper) >= 0:
            raise ValueError("Could not find a root here (e.g. no root or multiple roots), try again")
        
        error = 0
        middle = lower
        
        for i in range(100):
            middle_old = middle
            middle = (lower + upper) / 2.0
            if self.f_of_x(lower) * self.f_of_x(middle) < 0:
                upper = middle
            elif self.f_of_x(lower) * self.f_of_x(middle) > 0:
                lower = middle
            else:
                middle_old = middle
                break
        
        if middle != 0:
            error = abs((middle - middle_old) / middle)
        
        return middle, error

print "Content-Type: text/html\n"
print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "<title>Some math</title>"
print "</head>"
print "<body>"
print "<form action='bisector.cgi' method='POST'>"
print "<p>"
print "function of x: <input type='text' name='function'><br>"
print "lower bound: <input type='text' name='lowerbound'><br>"
print "upper bound: <input type='text' name='upperbound'><input type='submit' value='submit'><br>"

if sys.stdin:
    inputs = urlparse.parse_qs(sys.stdin.read())
    f = F(inputs['function'][0])
    
    try:
        root, error = f.find_root(float(inputs['lowerbound'][0]), float(inputs['upperbound'][0]))
    except ValueError:
        print "Could not find a root here (e.g. no root or multiple roots), try again"
    except NameError:
        print "Gotta be a function of x only"
    else:
        perc_error = error * 100
        print "For function f(x) = %s, there was a root at %f, with a %f&#37; margin of error" % (f.func, root, perc_error)

print "</p>"
print "</form>"
print "</body>"
print "</html>"