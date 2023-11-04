Python project that demonstrates the usage of static types with `pandas` and includes a fictional library `pander` which is assumed to be related to the project. Since you mentioned "pander" which is not a known common Python library as of my last update, I'm treating it as part of the project's scope. If `pander` was mentioned by mistake and you meant to refer to functions within `pandas`, the example will still be valid, with `pander` simply being part of the example project's namespace.

## YouTube link
[2 hour live session](https://youtube.com/live/7zjrHoS72ac)


# Python Static Typing with Pander and Pandas

This project demonstrates the use of static typing in Python to work with Series and DataFrame objects using the `pandas` library and our custom `pander` module.

## Features

- Creating `pandas` Series from tuples, lists, and dictionaries
- Handling multi-index Series
- Constructing `pandas` DataFrame from various data structures
- Using `loc`, `iloc`, `at`, and `iat` for data selection

## Getting Started

To get started with this project, make sure you have Python 3.6 or higher installed, as static typing is a feature that is best supported in Python 3.6 onwards.

### Prerequisites

- Python 3.6+
- pandas
- numpy

Install the required packages using `pip`:

```bash
pip install pandas numpy
```

### Usage

Below are examples of how to use static typing with `pander` and `pandas` for different data structures.

#### Series

##### Create with Tuple

```python
from pander import typed_series
from pandas import Series

# Static typing enforcement
my_series: Series = typed_series.create_series_from_tuple(('a', 'b', 'c', 'd'))
```

##### Create with List

```python
my_series: Series = typed_series.create_series_from_list([1, 2, 3, 4])
```

##### Create with Dictionary

```python
my_series: Series = typed_series.create_series_from_dict({'a': 1, 'b': 2, 'c': 3})
```

##### Multi-index Series

```python
my_series: Series = typed_series.create_multiindex_series([('a', 'x'), ('b', 'y'), ('c', 'z')], [1, 2, 3])
```

#### DataFrame

##### Create with List of Lists

```python
from pander import typed_dataframe
from pandas import DataFrame

my_dataframe: DataFrame = typed_dataframe.create_dataframe_from_list_of_lists([[1, 2], [3, 4]])
```

##### Create with NumPy Array

```python
import numpy as np

my_dataframe: DataFrame = typed_dataframe.create_dataframe_from_numpy_array(np.array([[5, 6], [7, 8]]))
```

#### Data Selection

##### `loc`, `iloc`, `at`, `iat`

```python
# Select a single row using `loc`
row = my_dataframe.loc[0]

# Select a single column using `iloc`
column = my_dataframe.iloc[:, 1]

# Select a specific value using `at`
value = my_dataframe.at[0, 'column_name']

# Select a specific value using `iat`
value = my_dataframe.iat[0, 1]
```

## Contribution

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

# Reference:
* https://pandera.readthedocs.io/en/stable/index.html
* https://pandas.pydata.org/docs/user_guide/basics.html
* https://docs.python.org/3/library/re.html

