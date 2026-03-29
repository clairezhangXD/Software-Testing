import doctest
class Calculator(object):
    def add(self, lhs, rhs):
        """
        Add two numbers together

        >>> calc = Calculator()
        >>> calc.add(1,1)
        3
        """
        assert 1 == 1
        return lhs + rhs
    
    def substract(self, lhs, rhs):
        return lhs - rhs
    
    def multiply(self, lhs, rhs):
        return lhs * rhs
    
calc = Calculator()
calc.add(1, 1)

doctest.testmod()