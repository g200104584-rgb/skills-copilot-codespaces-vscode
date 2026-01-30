"""
Simple tests to validate optimized Python code works correctly
"""

import sys
import os

# Import the optimized functions
import importlib.util
spec = importlib.util.spec_from_file_location("optimized_loops", 
    os.path.join(os.path.dirname(__file__), "optimized-loops.py"))
optimized_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(optimized_module)

# Import functions from the module
find_unique_items = optimized_module.find_unique_items
get_even_numbers = optimized_module.get_even_numbers
calculate_sum = optimized_module.calculate_sum
create_report = optimized_module.create_report
find_common_elements = optimized_module.find_common_elements
fibonacci_fast = optimized_module.fibonacci_fast
fibonacci_iterative = optimized_module.fibonacci_iterative
process_large_list = optimized_module.process_large_list
check_membership = optimized_module.check_membership
filter_complex = optimized_module.filter_complex

def test_find_unique_items():
    items = [1, 2, 3, 2, 4, 3, 5]
    result = find_unique_items(items)
    expected = {1, 2, 3, 4, 5}
    assert set(result) == expected, f"Expected {expected}, got {set(result)}"
    print("✓ find_unique_items works correctly")

def test_get_even_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = get_even_numbers(numbers)
    expected = [2, 4, 6, 8, 10]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ get_even_numbers works correctly")

def test_calculate_sum():
    numbers = [1, 2, 3, 4, 5]
    result = calculate_sum(numbers)
    expected = 15
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ calculate_sum works correctly")

def test_create_report():
    data = [
        {'name': 'Item1', 'value': 100},
        {'name': 'Item2', 'value': 200}
    ]
    result = create_report(data)
    assert 'Item1' in result and 'Item2' in result
    assert '100' in result and '200' in result
    print("✓ create_report works correctly")

def test_find_common_elements():
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    result = find_common_elements(list1, list2)
    expected = {3, 4, 5}
    assert set(result) == expected, f"Expected {expected}, got {set(result)}"
    print("✓ find_common_elements works correctly")

def test_fibonacci():
    result = fibonacci_fast(10)
    expected = 55
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ fibonacci_fast works correctly")

def test_fibonacci_iterative():
    result = fibonacci_iterative(10)
    expected = 55
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ fibonacci_iterative works correctly")

def test_process_large_list():
    data = [1, 2, 3, 4, 5]
    result = process_large_list(data)
    expected = [2, 4, 6, 8, 10]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ process_large_list works correctly")

def test_check_membership():
    items = [1, 2, 3, 4, 5]
    targets = [3, 4, 6, 7]
    result = check_membership(items, targets)
    expected = [3, 4]
    assert result == expected, f"Expected {expected}, got {result}"
    print("✓ check_membership works correctly")

def test_filter_complex():
    data = [
        {'name': 'John', 'age': 25, 'active': True},
        {'name': 'Jane', 'age': 17, 'active': True},
        {'name': 'Bob', 'age': 30, 'active': False},
        {'name': 'Alice', 'age': 22, 'active': True}
    ]
    result = filter_complex(data, min_age=18, active_only=True)
    expected_names = {'John', 'Alice'}
    result_names = {item['name'] for item in result}
    assert result_names == expected_names, f"Expected {expected_names}, got {result_names}"
    print("✓ filter_complex works correctly")

if __name__ == '__main__':
    print("Testing Optimized Python Functions...\n")
    
    test_find_unique_items()
    test_get_even_numbers()
    test_calculate_sum()
    test_create_report()
    test_find_common_elements()
    test_fibonacci()
    test_fibonacci_iterative()
    test_process_large_list()
    test_check_membership()
    test_filter_complex()
    
    print("\n✓ All tests passed!")
