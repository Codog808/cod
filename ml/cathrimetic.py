import re

def successor(value):
    return value + 1

class numbers:
    s = successor
    @classmethod
    def one(cls):
        return cls.s(0)
    @classmethod
    def two(cls):
        return cls.s(cls.s(0))        
    @classmethod
    def three(cls):
        return cls.s(cls.s(cls.s(0)))

class axioms:
    def __init__(self, equation):
        print("\nApplying Axioms to...")
        self.equation = equation
        print(self.equation)
        self.a, self.b = [expression.split() for expression in equation.split(" = ")]

    def equality(self):
        """ A + B = A + B """
        print("Equality:")
        if (self.a[len(self.a)//2] == self.b[len(self.b)//2]) and (self.a[0] == self.b[-1] and self.a[0] == self.b[-1]):
            print(True)
            return True
        else:
            return False

    def complementary(self):
        """ A + B = B + A """ 
        print("Complementry:")
        if (self.a[len(self.a)//2] == self.b[len(self.b)//2]) and (self.a[0] == self.b[-1] and self.a[-1] == self.b[0]):
            new_equation = f"{self.a[0]} {self.a[len(self.a)//2]} {self.a[-1]} = {self.b[-1]} {self.b[len(self.b)//2]} {self.b[0]}"
            print(new_equation)
            return new_equation
        else:
            print(False)
            return False



def example():
    # s = successor    
    x = numbers.three()
    print(x)
    Fx = "X + Y = Y + B"
    Gx = "G - Y = Y - G"
    axioms(Fx).complementary()
    axioms(Gx).complementary()
    Zx = "cG + aD = aD + cG"
    Zx_solve = axioms(Zx)
    Zx_solve.complementary()
    Zx_solve.equality()

def expression_split(expression):
    """ Everything has a purpose """
    re_expression = r'[+\-*/%]'
    expression = expression.strip()
    symbols = re.split(re_expression, expression)
    operations = re.findall(re_expression, expression)
    components = []
    # There will always be one more symbol than operation
    for symbol, op in zip(symbols, operations + [""]):
        if symbol:
            components.append(symbol)
        if op:
            components.append(op)
    return components

class axel:
    def __init__(A, equation):
        A.equation = equation.strip()
        print("Applying Axioms to...\n" + A.equation)
        a, b = equation.split(" = ")
        A.a_expression, A.b_expression = expression_split(a), expression_split(b)
    def equality(A):
        print("Equality:")
        if A.a_expression == A.b_expression:
            print(True)
            return True
        else:
            print(False)
            return False

def main():
    quad_equation = " X^2 + X * Y + Y^2 = 0 "
    arithmetic_equation = " X + Y + Z = Y + Z + A "
    a, b = arithmetic_equation.split(" = ")
    expression_split(a)
    expression_split(b)
    # Apply what Tsoding did to the equation in order to manipulate it to make equality true.
    axel(quad_equation).equality()
    limit = 100_000_000
    print(limit)
    for _ in range(limit):
        function_ = input("what do you want to apply to the equation?\nType Here: ")
main()
