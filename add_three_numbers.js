/**
 * Adds three numbers together
 * @param {number} a - First number
 * @param {number} b - Second number
 * @param {number} c - Third number
 * @returns {number} The sum of the three numbers
 */
function addThreeNumbers(a, b, c) {
  return a + b + c;
}

// Example usage
if (require.main === module) {
  const result = addThreeNumbers(5, 10, 15);
  console.log(`The sum of 5, 10, and 15 is: ${result}`);
}

module.exports = addThreeNumbers;
