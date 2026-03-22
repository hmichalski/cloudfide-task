import pandas
import re

def add_virtual_column(df: pandas.DataFrame, role: str, new_column: str) -> pandas.DataFrame:
    if not isinstance(df, pandas.DataFrame):
        return pandas.DataFrame([])

    if not isinstance(role, str):
        return pandas.DataFrame([])

    if not isinstance(new_column, str):
        return pandas.DataFrame([])

    # Regex based new column name validation, only letters and underscores are allowed
    def new_column_label_valid(value: str) -> bool:
        valid_label_pattern = re.compile(r"^[A-Za-z_]+$")
        return valid_label_pattern.fullmatch(value) is not None

    if not new_column_label_valid(new_column):
        return pandas.DataFrame([])

    # Format role to <label><op><label>
    role = re.sub(r"\s+", "", role)
    match = re.fullmatch(r"([A-Za-z_]+)([+\-*])([A-Za-z_]+)", role)
    
    # If no matches -> role is invalid
    if not match:
        return pandas.DataFrame([])

    left_label, operator, right_label = match.groups()

    # Check if both labels exist in the dataframe
    if left_label not in df.columns or right_label not in df.columns:
        return pandas.DataFrame([])

    if operator == "+":
        result_series = df[left_label] + df[right_label]
    elif operator == "-":
        result_series = df[left_label] - df[right_label]
    elif operator == "*":
        result_series = df[left_label] * df[right_label]

    result = df.copy()
    result[new_column] = result_series
    return result