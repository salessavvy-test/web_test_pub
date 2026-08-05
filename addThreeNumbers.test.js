const addThreeNumbers = require('./addThreeNumbers');

describe('addThreeNumbers', () => {
    test('adds three positive numbers', () => {
        expect(addThreeNumbers(1, 2, 3)).toBe(6);
    });

    test('adds three negative numbers', () => {
        expect(addThreeNumbers(-1, -2, -3)).toBe(-6);
    });

    test('adds mixed positive and negative numbers', () => {
        expect(addThreeNumbers(10, -5, 3)).toBe(8);
    });

    test('adds with zero', () => {
        expect(addThreeNumbers(0, 0, 0)).toBe(0);
        expect(addThreeNumbers(5, 0, 10)).toBe(15);
    });

    test('adds decimal numbers', () => {
        expect(addThreeNumbers(1.5, 2.3, 3.2)).toBe(7);
    });
});
