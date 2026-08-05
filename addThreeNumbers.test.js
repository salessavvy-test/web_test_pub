const addThreeNumbers = require('./addThreeNumbers');

describe('addThreeNumbers', () => {
  test('adds three positive numbers', () => {
    expect(addThreeNumbers(1, 2, 3)).toBe(6);
  });

  test('adds three numbers with negatives', () => {
    expect(addThreeNumbers(-1, 2, 3)).toBe(4);
  });

  test('adds three zeros', () => {
    expect(addThreeNumbers(0, 0, 0)).toBe(0);
  });

  test('adds decimal numbers', () => {
    expect(addThreeNumbers(1.5, 2.5, 3.5)).toBe(7.5);
  });
});
