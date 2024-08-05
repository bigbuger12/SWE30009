import random
import math

def sort_numbers(numbers):
    """Sort a list of integers."""
    return sorted(numbers)

def add_value_to_elements(numbers, value):
    """Add a value to all elements in the list."""
    return [x + value for x in numbers]

def remove_duplicate(numbers):
    """Remove a duplicate element from the list."""
    if len(numbers) > 1:
        numbers.remove(numbers[0])
    return numbers

def run_test():
    # Original input list
    original_input = [random.randint(1, 10) for _ in range(10)]
    
    # Metamorphic Relation 1: Add a specific value to all elements
    value_to_add = random.randint(1, 5)
    transformed_input1 = add_value_to_elements(original_input, value_to_add)
    
    # Metamorphic Relation 2: Remove a duplicate element
    transformed_input2 = remove_duplicate(original_input.copy())
    
    # Test original program
    original_output = sort_numbers(original_input)
    transformed_output1 = sort_numbers(transformed_input1)
    transformed_output2 = sort_numbers(transformed_input2)
    
    # Print results
    print("Original Input:", original_input)
    print("Original Output:", original_output)
    print(f"Transformed Input 1 (add {value_to_add}):", transformed_input1)
    print("Transformed Output 1:", transformed_output1)
    print("Transformed Input 2 (remove duplicate):", transformed_input2)
    print("Transformed Output 2:", transformed_output2)

    # Check Metamorphic Relation 1
    print("Metamorphic Relation 1 holds:", transformed_output1 == [x + value_to_add for x in original_output])

    # Check Metamorphic Relation 2
    print("Metamorphic Relation 2 holds:", sorted(transformed_output2) == sorted(original_output))

if __name__ == "__main__":
    run_test()
