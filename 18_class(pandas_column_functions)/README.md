# Python Pandas with Static Typing

This README provides examples of common data manipulation operations in Pandas DataFrames using static type hints. These operations include selecting columns, adding, deleting, updating columns, and retrieving DataFrame information. Each section below includes code snippets with type annotations compatible with Python 3.6+.

## YouTube link
[2 hour live session](https://youtube.com/live/Dc7s2kfJ_28)

## Installation

Before running the examples, ensure you have Pandas installed in your environment:

```bash
pip install pandas
```

You can also use Mypy or any other static type checker to validate the type annotations:

```bash
pip install mypy
```

## Selecting Columns from DataFrame

### Select a Single Column

```python
import pandas as pd
from typing import Any

# Creating a DataFrame
df: pd.DataFrame = pd.DataFrame({
    'A': [1, 2, 3],
    'B': ['a', 'b', 'c'],
    'C': [1.2, 3.4, 5.6]
})

# Selecting a single column
col_a: pd.Series = df['A']
```

### Select Multiple Columns

```python
# Selecting multiple columns
cols_ab: pd.DataFrame = df[['A', 'B']]
```

## Add, Delete, and Update Columns in DataFrame

### Add a New Column

```python
# Adding a new column
df['D']: pd.Series = df['A'] + df['C']
```

### Delete a Column

```python
# Deleting a column
del df['B']
```

### Update a Column

```python
# Updating a column
df['A']: pd.Series = df['A'] * 2
```

## Add Columns Using a Custom Function

```python
from typing import Callable

# Define a custom function to add a new column
def add_custom_column(df: pd.DataFrame, column_name: str, func: Callable[[pd.DataFrame], Any]) -> None:
    df[column_name] = func(df)

# Use the custom function
add_custom_column(df, 'E', lambda x: x['A'] + x['C'])
```

## DataFrame Information Methods

```python
# df.info()
df.info()

# df.describe()
df.describe()

# df.head()
df_head: pd.DataFrame = df.head()

# df.tail()
df_tail: pd.DataFrame = df.tail()
```

## Selection by Position (iloc) and Label (loc)

### Selection with iloc

```python
# Selecting rows by position
row_first: pd.Series = df.iloc[0]

# Selecting a specific value by row and column position
value_first: Any = df.iloc[0, 0]
```

### Selection with loc

```python
# Selecting rows by label
row_label: pd.Series = df.loc[0]

# Selecting a specific value by row and column label
value_label: Any = df.loc[0, 'A']
```

### Accessing a Scalar Value with at and iat

```python
# Accessing a single value by row and column label
scalar_at: Any = df.at[0, 'A']

# Accessing a single value by row and column position
scalar_iat: Any = df.iat[0, 0]
```

## Notes

- It is important to install Pandas and a static type checker to make the most out of the static typing features in Python.
- The `Any` type is used for DataFrame elements because Pandas Series can contain heterogeneous data types, but you may specify more specific types based on your data.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](#) if you want to contribute.

## License

[MIT](LICENSE)
```

This README.md provides a guide to some basic Pandas DataFrame operations with static types. It is important to adapt the types used here according to the actual data you expect in your DataFrame for more precise type checking.