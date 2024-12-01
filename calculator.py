import math
from typing import Union

class Calculator:
    def add(self, x: float, y: float) -> float:
        return x + y
    
    def subtract(self, x: float, y: float) -> float:
        return x - y
    
    def multiply(self, x: float, y: float) -> float:
        return x * y
    
    def divide(self, x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        return x / y
    
    def logarithm(self, x: float) -> float:
        if x <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        return math.log10(x)
    
    def square(self, x: float) -> float:
        return x ** 2
    
    def square_root(self, x: float) -> float:
        if x < 0:
            raise ValueError("Square root is not defined for negative numbers")
        return math.sqrt(x)
    
    def calculate(self, operation: str, x: float, y: float = None) -> float:
        """Main calculation method that routes to specific operations"""
        operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            'log': self.logarithm,
            'square': self.square,
            'sqrt': self.square_root
        }
        
        if operation not in operations:
            raise ValueError(f"Unsupported operation: {operation}")
            
        if operation in ['log', 'square', 'sqrt']:
            return operations[operation](x)
        return operations[operation](x, y) 