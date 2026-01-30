"""
INEFFICIENT CODE - Python Examples
This file demonstrates common inefficient patterns in Python
"""

# ISSUE 1: Using list when set would be more efficient
def find_unique_items(items):
    unique = []
    for item in items:
        if item not in unique:  # O(n) lookup in list
            unique.append(item)
    return unique

# ISSUE 2: Building lists with concatenation instead of comprehension
def get_even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result = result + [num]  # Creates new list each time
    return result

# ISSUE 3: Not using built-in functions
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

# ISSUE 4: Inefficient string building
def create_report(data):
    report = ""
    for item in data:
        report = report + f"Item: {item['name']}, Value: {item['value']}\n"
    return report

# ISSUE 5: Unnecessary nested loops
def find_common_elements(list1, list2):
    common = []
    for item1 in list1:
        for item2 in list2:
            if item1 == item2 and item1 not in common:
                common.append(item1)
    return common

# ISSUE 6: Reading entire file into memory
def count_lines_with_pattern(filename, pattern):
    with open(filename, 'r') as f:
        content = f.read()  # Loads entire file into memory
    lines = content.split('\n')
    count = 0
    for line in lines:
        if pattern in line:
            count += 1
    return count

# ISSUE 7: Using global variables and repeated calculations
cache = {}

def fibonacci_slow(n):
    if n <= 1:
        return n
    # Recalculates same values multiple times
    return fibonacci_slow(n-1) + fibonacci_slow(n-2)

# ISSUE 8: Creating unnecessary copies
def process_large_list(data):
    # Creates a full copy of the list
    temp = data[:]
    result = []
    for i in range(len(temp)):
        result.append(temp[i] * 2)
    return result

# ISSUE 9: Using wrong data structure for lookups
def check_membership(items, targets):
    results = []
    for target in targets:
        # Linear search through list
        if target in items:  # O(n) for list
            results.append(target)
    return results
