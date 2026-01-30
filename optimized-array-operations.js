/**
 * OPTIMIZED CODE - Array Operations
 * This file contains performance improvements for common JavaScript patterns
 */

// IMPROVED: Use Set for O(n) complexity instead of nested loops
function findDuplicates(arr) {
    const seen = new Set();
    const duplicates = new Set();
    
    for (const item of arr) {
        if (seen.has(item)) {
            duplicates.add(item);
        } else {
            seen.add(item);
        }
    }
    
    return Array.from(duplicates);
}

// IMPROVED: Use array join() instead of concatenation
function buildLargeString(items) {
    return items.join(',');
}

// IMPROVED: Combine all operations into a single pass
function processData(data) {
    return data
        .filter(person => person.age >= 18 && person.active === true)
        .map(person => person.name.toUpperCase());
}

// IMPROVED: Use Map for O(1) lookups
function findItems(targetIds, allItems) {
    // Create a Map for O(1) lookups
    const itemMap = new Map(allItems.map(item => [item.id, item]));
    
    // Map target IDs to items
    return targetIds
        .map(id => itemMap.get(id))
        .filter(item => item !== undefined);
}

// IMPROVED: Use async file operations
async function processLargeFile(filename) {
    const fs = require('fs').promises;
    const readline = require('readline');
    const fileStream = require('fs').createReadStream(filename);
    
    const rl = readline.createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });
    
    let sum = 0;
    for await (const line of rl) {
        sum += parseInt(line) || 0;
    }
    
    return sum;
}

// IMPROVED: Use proper variable scoping with let/const
function createHandlers(count) {
    const handlers = [];
    for (let i = 0; i < count; i++) {
        handlers.push(function() {
            console.log('Handler ' + i);
        });
    }
    return handlers;
}

// IMPROVED: Use spread operator for efficient array merging
function mergeArrays(arr1, arr2, arr3) {
    return [...arr1, ...arr2, ...arr3];
}

// BONUS: Additional optimizations

// Efficient debounce implementation
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Efficient memoization
function memoize(fn) {
    const cache = new Map();
    return function(...args) {
        const key = JSON.stringify(args);
        if (cache.has(key)) {
            return cache.get(key);
        }
        const result = fn(...args);
        cache.set(key, result);
        return result;
    };
}

module.exports = {
    findDuplicates,
    buildLargeString,
    processData,
    findItems,
    processLargeFile,
    createHandlers,
    mergeArrays,
    debounce,
    memoize
};
