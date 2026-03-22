# Cloudfide Task

## About

This repo showcases my solution to Cloudfides Junior Data Scientist role recruitment task.

## Task description
You have a pandas DataFrame with existing data and want to create a new DataFrame that includes the original data along with an additional column calculated based on specified operations. To achieve this, implement the `add_virtual_column` function.

Inputs:
- `df`: Any pandas DataFrame.
- `role`: A mathematical expression defining how to compute the values for the virtual column. For example, `first_column-second_column`.
- `new_column`: The name of the new virtual column to be added.

## Validations
- Column labels must contain only letters and underscores.
- The function supports basic operations: addition (`+`), subtraction (`-`), and multiplication (`*`).
- If the rule or any column label is incorrect, the function returns an empty DataFrame.

## Assumptions
- The rule format is exactly: `column_a OP column_b`.
- Only 2 source columns are supported in one rule.
- Only one operator is supported in one rule.
- Any whitespace in the rule is ignored before parsing.


## Files
- `solution.py` - implementation of `add_virtual_column`.
- `tests.py` - test cases for valid and invalid inputs.
- `requirements.txt` - Python dependencies.
- `.gitignore` - ignored local/cache files.

## Run
Install dependencies:

`pip install -r requirements.txt`

Run tests:

`python tests.py`

