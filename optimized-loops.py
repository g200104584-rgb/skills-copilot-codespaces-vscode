"""
OPTIMIZED CODE - Python Examples
This file contains performance improvements for common Python patterns
"""

from functools import lru_cache
from typing import List, Set, Dict, Any

# IMPROVED: Use set for O(1) lookups
def find_unique_items(items: List[Any]) -> List[Any]:
    return list(set(items))

# Alternative that preserves order (Python 3.7+)
def find_unique_items_ordered(items: List[Any]) -> List[Any]:
    return list(dict.fromkeys(items))

# IMPROVED: Use list comprehension
def get_even_numbers(numbers: List[int]) -> List[int]:
    return [num for num in numbers if num % 2 == 0]

# IMPROVED: Use built-in sum function
def calculate_sum(numbers: List[int]) -> int:
    return sum(numbers)

# IMPROVED: Use join() for string building
def create_report(data: List[Dict[str, Any]]) -> str:
    lines = [f"Item: {item['name']}, Value: {item['value']}" for item in data]
    return '\n'.join(lines)

# Alternative using generator for memory efficiency
def create_report_generator(data: List[Dict[str, Any]]) -> str:
    return '\n'.join(
        f"Item: {item['name']}, Value: {item['value']}" 
        for item in data
    )

# IMPROVED: Use set intersection
def find_common_elements(list1: List[Any], list2: List[Any]) -> List[Any]:
    return list(set(list1) & set(list2))

# Alternative that preserves order from list1
def find_common_elements_ordered(list1: List[Any], list2: List[Any]) -> List[Any]:
    set2 = set(list2)
    return [item for item in list1 if item in set2]

# IMPROVED: Process file line by line
def count_lines_with_pattern(filename: str, pattern: str) -> int:
    count = 0
    with open(filename, 'r') as f:
        for line in f:  # Reads one line at a time
            if pattern in line:
                count += 1
    return count

# Alternative using generator expression
def count_lines_with_pattern_compact(filename: str, pattern: str) -> int:
    with open(filename, 'r') as f:
        return sum(1 for line in f if pattern in line)

# IMPROVED: Use memoization with lru_cache
@lru_cache(maxsize=None)
def fibonacci_fast(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci_fast(n-1) + fibonacci_fast(n-2)

# Alternative: Iterative approach (most efficient)
def fibonacci_iterative(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# IMPROVED: Use list comprehension without copying
def process_large_list(data: List[int]) -> List[int]:
    return [item * 2 for item in data]

# Alternative: Generator for memory efficiency with large datasets
def process_large_list_generator(data: List[int]):
    return (item * 2 for item in data)

# IMPROVED: Use set for O(1) membership testing
def check_membership(items: List[Any], targets: List[Any]) -> List[Any]:
    item_set = set(items)
    return [target for target in targets if target in item_set]

# BONUS: Additional optimizations

# Efficient batch processing
def process_in_batches(data: List[Any], batch_size: int = 100):
    """Process large datasets in batches to reduce memory usage"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Efficient filtering with multiple conditions
def filter_complex(data: List[Dict[str, Any]], 
                  min_age: int = 18, 
                  active_only: bool = True) -> List[Dict[str, Any]]:
    """Single-pass filtering with multiple conditions"""
    return [
        item for item in data 
        if item.get('age', 0) >= min_age and 
           (not active_only or item.get('active', False))
    ]

# Use dict comprehension for efficient mapping
def create_lookup_dict(items: List[Dict[str, Any]], 
                       key_field: str = 'id') -> Dict[Any, Dict[str, Any]]:
    """Create efficient lookup dictionary"""
    return {item[key_field]: item for item in items if key_field in item}
