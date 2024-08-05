import math

def sort_numbers(numbers):
    """Sort a list of integers."""
    return [math.sqrt(x) for x in sorted(numbers)]  # Mutation: square root each element

if __name__ == "__main__":
    example_input = [5, 3, 8, 5, 2, 9, 1, 5]
    print("Original List:", example_input)
    print("Sorted List:", sort_numbers(example_input))
