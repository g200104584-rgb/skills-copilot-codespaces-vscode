/**
 * INEFFICIENT CODE - Array Operations
 * This file demonstrates common inefficient patterns in JavaScript
 */

// ISSUE 1: Nested loops with O(n²) complexity when O(n) is possible
function findDuplicates(arr) {
    const duplicates = [];
    for (let i = 0; i < arr.length; i++) {
        for (let j = i + 1; j < arr.length; j++) {
            if (arr[i] === arr[j] && duplicates.indexOf(arr[i]) === -1) {
                duplicates.push(arr[i]);
            }
        }
    }
    return duplicates;
}

// ISSUE 2: Repeated string concatenation in loops (creates new strings each time)
function buildLargeString(items) {
    let result = '';
    for (let i = 0; i < items.length; i++) {
        result += items[i] + ',';
    }
    return result;
}

// ISSUE 3: Unnecessary array operations and multiple iterations
function processData(data) {
    // Filter twice instead of once
    const adults = data.filter(person => person.age >= 18);
    const activeAdults = adults.filter(person => person.active === true);
    
    // Map separately instead of combining with filter
    const names = activeAdults.map(person => person.name);
    
    // Another separate iteration to uppercase
    const upperNames = names.map(name => name.toUpperCase());
    
    return upperNames;
}

// ISSUE 4: Linear search instead of using Map/Set
function findItems(targetIds, allItems) {
    const results = [];
    for (const id of targetIds) {
        for (const item of allItems) {
            if (item.id === id) {
                results.push(item);
                break;
            }
        }
    }
    return results;
}

// ISSUE 5: Blocking synchronous operations
function processLargeFile(filename) {
    const fs = require('fs');
    // Synchronous file read blocks the event loop
    const content = fs.readFileSync(filename, 'utf-8');
    const lines = content.split('\n');
    let sum = 0;
    for (const line of lines) {
        sum += parseInt(line) || 0;
    }
    return sum;
}

// ISSUE 6: Memory leak - creating closures in loops
function createHandlers(count) {
    const handlers = [];
    for (var i = 0; i < count; i++) {
        handlers.push(function() {
            console.log('Handler ' + i);
        });
    }
    return handlers;
}

// ISSUE 7: Inefficient array copying
function mergeArrays(arr1, arr2, arr3) {
    let result = [];
    for (let item of arr1) {
        result.push(item);
    }
    for (let item of arr2) {
        result.push(item);
    }
    for (let item of arr3) {
        result.push(item);
    }
    return result;
}

module.exports = {
    findDuplicates,
    buildLargeString,
    processData,
    findItems,
    processLargeFile,
    createHandlers,
    mergeArrays
};
