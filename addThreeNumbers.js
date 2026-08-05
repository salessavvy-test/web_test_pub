/**
 * Adds three numbers together
 * @param {number} a - First number
 * @param {number} b - Second number
 * @param {number} c - Third number
 * @returns {number} The sum of a, b, and c
 */
function addThreeNumbers(a, b, c) {
  return a + b + c;
}

module.exports = addThreeNumbers;

// Example usage
if (require.main === module) {
  console.log(addThreeNumbers(5, 10, 15)); // Output: 30
  console.log(addThreeNumbers(1, 2, 3));   // Output: 6
}
