#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Find root in a function using an instance of F
"""

from __future__ import unicode_literals
import math


class F(object):
    """A function class used to find a function's roots

    Attributes:
    func - the function used to find a root
    var - the independent variable
    Methods:
    f_of_x - evaluate the function at a given location
    find_root - find a root in the function at a given interval
    """
    def __init__(self, func, var='x'):
        """Make a new F object

        Positional arguments:
        func - a string representation of the function expression
        Keyword arguments:
        var - the independent variable used, default is 'x'
        """
        assert var in func, "Function must include the variable"
        # caret is commonly used, and treat integer input as floats
        self.func = func.replace('^', '**').replace('/', '*(1.0)/')
        self.var = var

    def f_of_var(self, x):
        """Evaluate the function at a given location

        Positional arguments:
        x - value of independent variable to go into function
        """
        # assign the user defined variable the input argument
        locals().update({self.var: x})
        return eval(self.func)

    def find_root(self, lower, upper):
        """Find a root in the function at a given interval

        Positional arguments:
        lower - lower bracket of interval
        upper - upper bracket of interval
        """
        # check that the function changes sign
        if self.f_of_var(lower) * self.f_of_var(upper) > 0:
            raise ValueError("Interval must cross the x-axis once, try again")

        # assign a starting midpoint
        middle = lower
        for i in range(30):
            middle_old = middle
            middle = (lower + upper) / 2.0
            # if root is in lower half, bring upper bound to midpoint
            if self.f_of_var(lower) * self.f_of_var(middle) < 0:
                upper = middle
            # if root is in upper half, bring lower bound to midpoint
            elif self.f_of_var(lower) * self.f_of_var(middle) > 0:
                lower = middle
            # if middle is root, reassign middle_old to get 0 error
            else:
                middle_old = middle
                break

        try:
            error = abs((middle - middle_old) / middle)
        except ZeroDivisionError:
            if middle_old:
                error = 1   # try middle_old as denominator
            else:
                error = 0   # if both middle and middle_old are 0

        return middle, error
