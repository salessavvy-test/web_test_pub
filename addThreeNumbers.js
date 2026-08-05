/**
 * Adds three numbers together
 * @param {number} num1 - The first number
 * @param {number} num2 - The second number
 * @param {number} num3 - The third number
 * @returns {number} The sum of the three numbers
 */
function addThreeNumbers(num1, num2, num3) {
  return num1 + num2 + num3;
}

// Example usage
console.log('Example: 5 + 10 + 15 =', addThreeNumbers(5, 10, 15));

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = addThreeNumbers;
}
