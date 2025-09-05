"""
TASK: Create a Calculator class.

Requirements:
1. The class should allow basic operations: add, subtract, multiply, divide.
2. Each operation should be a separate method.
3. Handle division by zero gracefully.
4. Allow both integers and floats.

Example Usage:
    calc = Calculator()
    print(calc.add(5, 3))        # 8
    print(calc.divide(10, 0))    # "Error: Division by zero"
"""

class Calculator:
    
    def add(self, first, second):
        self.first = first
        self.second = second
        
        return first + second

    def subtract(self,first,second):
        self.first = first
        self.second = second
        
        return first - second

    def multiply(self,first,second):
        self.first = first
        self.second = second
        
        return first * second

    def division(self,first,second):
        self.first = first
        self.second = second
        
        if second <= 0:
            return "Error: Division by zero"
        else:

            return first - second
    

calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))
print(calc.multiply(5, 3))
print(calc.division(5, 0))

