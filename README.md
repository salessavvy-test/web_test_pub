# web_test_pub
Webhook test: Public repo

## Features

### Sum Numbers Script
A Python script that adds 10 numbers together. Provides two methods:
- `add_ten_numbers()`: Takes 10 individual parameters
- `add_number_list()`: Takes a list of 10 numbers

#### Usage
```bash
python3 sum_numbers.py
```

#### Example
```python
from sum_numbers import add_ten_numbers, add_number_list

# Using individual parameters
result = add_ten_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)  # Output: 55

# Using a list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
result = add_number_list(numbers)
print(result)  # Output: 550
```
