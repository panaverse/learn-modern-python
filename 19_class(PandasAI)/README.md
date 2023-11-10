# Python Typing Hints for Pandas Data Manipulation and Visualization

This README file provides an overview of how to use Python typing hints for various data manipulation and visualization tasks using the Pandas library. Typing hints can be especially useful for ensuring that functions are used with the correct type of data, which can help prevent bugs and make the code easier to understand and maintain. Below you'll find examples of how to annotate functions with typing hints for tasks like applying filters on columns, computing value counts, grouping, data wrangling, and data visualization with Pandas.

## YouTube link
[2 hour live session](https://youtube.com/live/aRNZCwjTt5o)

## Corrections

As of Python 3.9, type aliases like List, Tuple, Dict, ... are [deprecated](https://docs.python.org/3/library/typing.html#deprecated-aliases).

So, from then on, use the built-in types list, tuple, dict, ...

[Using List/Tuple/etc. from typing vs directly referring type as list/tuple/etc](https://stackoverflow.com/questions/39458193/using-list-tuple-etc-from-typing-vs-directly-referring-type-as-list-tuple-etc)

## Prerequisites

Before you start, ensure you have the following installed:

- Python 3.6+
- Pandas
- Matplotlib (for data visualization)

You can install Pandas and Matplotlib using pip:

```bash
pip install pandas matplotlib
```

## Typing Hints Overview

Python typing hints are a formal way to indicate the types of variables expected by functions, returned by functions, and stored in collections. They are part of the Python standard library in the `typing` module.

```python
from typing import List, Dict
```

## Applying Filters on Columns

When filtering data in Pandas, you can specify the expected type of DataFrame and the type of the returned DataFrame.

```python
import pandas as pd
from typing import Any

def filter_dataframe(df: pd.DataFrame, column_name: str, filter_value: Any) -> pd.DataFrame:
    return df[df[column_name] == filter_value]
```

## Value Counts, `pd.cut`, `pd.qcut`

For operations like `value_counts`, `pd.cut`, and `pd.qcut`, you can specify the type of series input and the expected return type.

```python
from typing import Union
from pandas import Series, Interval

def get_value_counts(series: Series) -> Series:
    return series.value_counts()

def bin_data_cut(series: Series, bins: int) -> Series[Interval]:
    return pd.cut(series, bins)

def bin_data_qcut(series: Series, q: int) -> Series[Interval]:
    return pd.qcut(series, q)
```

## GroupBy Operations

Annotate functions that perform `groupby` operations, including `agg` and `apply`.

```python
from typing import Callable

def groupby_agg(df: pd.DataFrame, group_cols: List[str], agg_col: str, agg_func: str) -> pd.DataFrame:
    return df.groupby(group_cols)[agg_col].agg(agg_func)

def groupby_apply(df: pd.DataFrame, group_cols: List[str], apply_func: Callable) -> pd.DataFrame:
    return df.groupby(group_cols).apply(apply_func)
```

## Data Wrangling

For data wrangling operations like `merge`, `join`, and `concat`, provide hints for both input DataFrames and the resultant DataFrame.

```python
def merge_dataframes(left: pd.DataFrame, right: pd.DataFrame, on: str, how: str = 'inner') -> pd.DataFrame:
    return pd.merge(left, right, on=on, how=how)

def join_dataframes(left: pd.DataFrame, right: pd.DataFrame, on: str = None, how: str = 'left') -> pd.DataFrame:
    return left.join(right, on=on, how=how)

def concat_dataframes(dfs: List[pd.DataFrame], axis: int = 0) -> pd.DataFrame:
    return pd.concat(dfs, axis=axis)
```

## Data Visualization with Pandas

Type hints for data visualization functions typically do not return a value but perform an action, hence the return type can be annotated as `None`.

```python
import matplotlib.pyplot as plt

def plot_series(series: Series, title: str = 'Series Plot') -> None:
    series.plot()
    plt.title(title)
    plt.show()

def plot_dataframe_histogram(df: pd.DataFrame, column_name: str, bins: int = 10) -> None:
    df[column_name].hist(bins=bins)
    plt.title(f'Histogram of {column_name}')
    plt.show()
```

## Conclusion

This README serves as a guide for annotating Pandas operations with Python typing hints. Always ensure that the typing module is imported to use the type hints, and remember that the primary goal of using typing hints is to make your code more readable and maintainable.

## Note

This is a simplified representation, and in practice, you might need more complex typing constructs, especially for more nuanced `apply` functions, or when using custom types, or when dealing with DataFrames with known column types. Always refer to the latest Pandas documentation and the typing module enhancements for the most accurate information.
