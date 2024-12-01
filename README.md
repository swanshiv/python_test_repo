# Python Calculator

A simple calculator implementation with basic and advanced mathematical operations.

## Local Testing Instructions

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd python-calculator
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install pytest pytest-cov
   ```

4. Run the tests:
   ```bash
   pytest test_calculator.py -v
   ```

5. To check test coverage:
   ```bash
   pytest test_calculator.py --cov=calculator --cov-report=term-missing
   ```

## Usage Example 