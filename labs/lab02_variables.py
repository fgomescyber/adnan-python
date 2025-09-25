"""Lab 02 — Variables and Types
"""
def safe_divide(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Operands must be numeric types")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

if __name__ == '__main__':
    print("10 / 2 =", safe_divide(10,2))
