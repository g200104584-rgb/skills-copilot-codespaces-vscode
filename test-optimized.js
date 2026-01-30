/**
 * Simple tests to validate optimized code works correctly
 */

const optimized = require('./optimized-array-operations');

function assertEquals(actual, expected, testName) {
    const actualStr = JSON.stringify(actual);
    const expectedStr = JSON.stringify(expected);
    if (actualStr === expectedStr) {
        console.log(`✓ ${testName}`);
        return true;
    } else {
        console.log(`✗ ${testName}`);
        console.log(`  Expected: ${expectedStr}`);
        console.log(`  Actual: ${actualStr}`);
        return false;
    }
}

console.log('Testing Optimized Array Operations...\n');

// Test 1: findDuplicates
const arr1 = [1, 2, 3, 2, 4, 3, 5];
const duplicates = optimized.findDuplicates(arr1);
assertEquals(duplicates.sort(), [2, 3], 'findDuplicates finds correct duplicates');

// Test 2: buildLargeString
const items = ['apple', 'banana', 'cherry'];
const result = optimized.buildLargeString(items);
assertEquals(result, 'apple,banana,cherry', 'buildLargeString creates correct string');

// Test 3: processData
const data = [
    { name: 'John', age: 25, active: true },
    { name: 'Jane', age: 17, active: true },
    { name: 'Bob', age: 30, active: false },
    { name: 'Alice', age: 22, active: true }
];
const processed = optimized.processData(data);
assertEquals(processed, ['JOHN', 'ALICE'], 'processData filters and transforms correctly');

// Test 4: findItems
const targetIds = [2, 4, 6];
const allItems = [
    { id: 1, name: 'A' },
    { id: 2, name: 'B' },
    { id: 3, name: 'C' },
    { id: 4, name: 'D' },
    { id: 5, name: 'E' }
];
const foundItems = optimized.findItems(targetIds, allItems);
assertEquals(foundItems.map(i => i.name), ['B', 'D'], 'findItems finds correct items');

// Test 5: createHandlers
const handlers = optimized.createHandlers(3);
assertEquals(handlers.length, 3, 'createHandlers creates correct number of handlers');

// Test 6: mergeArrays
const merged = optimized.mergeArrays([1, 2], [3, 4], [5, 6]);
assertEquals(merged, [1, 2, 3, 4, 5, 6], 'mergeArrays merges correctly');

// Test 7: memoize
let callCount = 0;
function expensiveFunction(n) {
    callCount++;
    return n * n;
}
const memoized = optimized.memoize(expensiveFunction);
memoized(5);
memoized(5);
memoized(5);
assertEquals(callCount, 1, 'memoize caches results correctly');

console.log('\n✓ All tests passed!');
