def sort_numbers(numbers):
    """Sort a list of integers."""
    sorted_numbers = sorted(numbers)
    middle_index = len(sorted_numbers) // 2
    return sorted_numbers[:middle_index] + sorted_numbers[middle_index+1:]  # Mutation: remove middle element

if __name__ == "__main__":
    example_input = [5, 3, 8, 5, 2, 9, 1, 5]
    print("Original List:", example_input)
    print("Sorted List:", sort_numbers(example_input))
