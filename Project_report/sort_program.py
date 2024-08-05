def sort_numbers(numbers):
    """Sort a list of integers."""
    return sorted(numbers)

if __name__ == "__main__":
    example_input = [5, 3, 8, 5, 2, 9, 1, 5]
    print("Original List:", example_input)
    print("Sorted List:", sort_numbers(example_input))
