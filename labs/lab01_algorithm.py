"""Lab 01 — Algorithmic Thinking (Beginner)
Run: python labs/lab01_algorithm.py
"""
def sum_of_even_numbers(nums):
    if not isinstance(nums, list):
        raise ValueError("Input must be a list of integers.")
    return sum(n for n in nums if isinstance(n, int) and n % 2 == 0)

def main():
    sample = [1,2,3,4,10]
    print("Sample:", sample)
    print("Sum of even numbers:", sum_of_even_numbers(sample))

if __name__ == '__main__':
    main()
