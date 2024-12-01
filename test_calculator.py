import unittest
from calculator import Calculator
import math

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_basic_operations(self):
        # Testing basic arithmetic operations
        test_cases = [
            ('+', 2, 3, 5),
            ('+', -1, 1, 0),
            ('-', 5, 3, 2),
            ('-', 1, 5, -4),
            ('*', 4, 3, 12),
            ('*', -2, 3, -6),
            ('/', 6, 2, 3),
            ('/', 5, 2, 2.5),
        ]
        
        for op, x, y, expected in test_cases:
            with self.subTest(f"{x} {op} {y} = {expected}"):
                result = self.calc.calculate(op, x, y)
                self.assertAlmostEqual(result, expected)

    def test_advanced_operations(self):
        # Testing advanced mathematical operations
        test_cases = [
            ('log', 100, None, 2),
            ('log', 1, None, 0),
            ('square', 4, None, 16),
            ('square', -2, None, 4),
            ('sqrt', 16, None, 4),
            ('sqrt', 2, None, math.sqrt(2)),
        ]
        
        for op, x, y, expected in test_cases:
            with self.subTest(f"{op}({x}) = {expected}"):
                result = self.calc.calculate(op, x, y)
                self.assertAlmostEqual(result, expected)

    def test_edge_cases(self):
        # Testing error cases
        with self.assertRaises(ValueError):
            self.calc.calculate('/', 1, 0)  # Division by zero
        
        with self.assertRaises(ValueError):
            self.calc.calculate('log', 0)  # Log of zero
            
        with self.assertRaises(ValueError):
            self.calc.calculate('sqrt', -1)  # Square root of negative

    # Additional test cases can be generated programmatically
    def test_generated_cases(self):
        import random
        
        for _ in range(85):  # Adding 85 more random test cases
            op = random.choice(['+', '-', '*', '/', 'log', 'square', 'sqrt'])
            x = random.uniform(-100, 100)
            
            try:
                if op in ['log', 'square', 'sqrt']:
                    if op == 'log':
                        x = abs(x)  # Ensure positive for log
                    if op == 'sqrt':
                        x = abs(x)  # Ensure positive for sqrt
                    result = self.calc.calculate(op, x)
                else:
                    y = random.uniform(-100, 100)
                    if op == '/':
                        y = random.uniform(0.1, 100)  # Avoid division by zero
                    result = self.calc.calculate(op, x, y)
                
                self.assertIsInstance(result, float)
                self.assertFalse(math.isnan(result))
                self.assertFalse(math.isinf(result))
                
            except ValueError:
                # Expected for certain invalid inputs
                pass

if __name__ == '__main__':
    unittest.main() 