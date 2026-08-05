/**
 * Simple test file for addThreeNumbers function
 *
 * Co-authored with Glean
 */
const addThreeNumbers = require('./addThreeNumbers');

// Test cases
console.log('Running tests for addThreeNumbers...\n');

// Test 1: Positive numbers
const result1 = addThreeNumbers(1, 2, 3);
console.log(`Test 1 - addThreeNumbers(1, 2, 3) = ${result1}`);
console.log(`Expected: 6, Got: ${result1}, ${result1 === 6 ? 'PASS' : 'FAIL'}\n`);

// Test 2: Larger numbers
const result2 = addThreeNumbers(10, 20, 30);
console.log(`Test 2 - addThreeNumbers(10, 20, 30) = ${result2}`);
console.log(`Expected: 60, Got: ${result2}, ${result2 === 60 ? 'PASS' : 'FAIL'}\n`);

// Test 3: Negative numbers
const result3 = addThreeNumbers(-5, 10, -3);
console.log(`Test 3 - addThreeNumbers(-5, 10, -3) = ${result3}`);
console.log(`Expected: 2, Got: ${result3}, ${result3 === 2 ? 'PASS' : 'FAIL'}\n`);

// Test 4: Zero values
const result4 = addThreeNumbers(0, 0, 0);
console.log(`Test 4 - addThreeNumbers(0, 0, 0) = ${result4}`);
console.log(`Expected: 0, Got: ${result4}, ${result4 === 0 ? 'PASS' : 'FAIL'}\n`);

console.log('All tests complete!');
