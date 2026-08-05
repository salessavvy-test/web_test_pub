# web_test_pub
Webhook test: Public repo

## Features

### Sum 10 Numbers
This repository includes a Python program that adds 10 numbers together.

#### Usage
```bash
python3 sum_numbers.py
```

The program will:
1. Demonstrate adding the numbers 1-10 (sum = 55)
2. Prompt you to enter your own 10 numbers to add

#### Running Tests
```bash
python3 test_sum_numbers.py
```

#### API
```python
from sum_numbers import add_ten_numbers

# Add 10 numbers
result = add_ten_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(result)  # Output: 55
```
