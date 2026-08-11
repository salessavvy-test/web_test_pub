/**
 * Adds three numbers together
 * @param {number} num1 - First number
 * @param {number} num2 - Second number
 * @param {number} num3 - Third number
 * @returns {number} The sum of the three numbers
 */
function addThreeNumbers(num1, num2, num3) {
  return num1 + num2 + num3;
}

module.exports = addThreeNumbers;

// Example usage
if (require.main === module) {
  const result = addThreeNumbers(5, 10, 15);
  console.log(`The sum of 5, 10, and 15 is: ${result}`);
}
