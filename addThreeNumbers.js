/**
 * Adds three numbers together
 * @param {number} a - First number
 * @param {number} b - Second number
 * @param {number} c - Third number
 * @returns {number} The sum of a, b, and c
 *
 * Co-authored with Glean
 */
function addThreeNumbers(a, b, c) {
  return a + b + c;
}

// Example usage
if (require.main === module) {
  console.log('Adding 1 + 2 + 3 =', addThreeNumbers(1, 2, 3));
  console.log('Adding 10 + 20 + 30 =', addThreeNumbers(10, 20, 30));
}

module.exports = addThreeNumbers;
