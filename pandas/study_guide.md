
### **Stage 1: Environment Setup & Package Management**
*   **Package Installation (Terminal Command):** 
    `pip install pandas` or `python -m pip install pandas`. Used to install the package if pandas is underlined in red or throwing an IDE warning.
*   **Importing the Library:** 
    `import pandas as pd`. Imports the library and gives it the conventional alias `pd`.
*   **Checking Library Version:** 
    `print(pd.__version__)`. Uses the double underscore (dunder) `__version__` property to print the installed version of pandas.

---

### **Stage 2: Creating and Working with Series (One-Dimensional Data)**
A **Series** is a one-dimensional labeled column or array.
*   **Series Constructor:** 
    `pd.Series(data, index=...)`. Note that the "S" is capitalized because it is a constructor, not a standard function.
    *   **`data` argument:** Can be a Python list or a Python dictionary. When passing a dictionary, pandas automatically uses the keys as the index labels.
    *   **`index` keyword argument:** `index=...` allows you to set custom labels instead of the default 0-indexed integers. You can pass a list, tuple, dictionary, numpy array, or another series.
*   **Label-Based Location Property:** 
    `series.loc['label']`. Used with the subscript operator `[]` to access or update a value at a specific custom label.
*   **Integer-Based Location Property:** 
    `series.iloc[integer_index]`. Used with the subscript operator `[]` to locate a value by its zero-based integer position.
*   **Updating Values:** 
    `series.loc['label'] = value` or `series.loc['label'] += value`. Overwrites or increments the value at a specified label.
*   **Value Filtering Operator:** 
    `series[condition]`. Uses the subscript operator with a logical condition (e.g., `series[series >= 200]`) to filter and return only the matching rows.
*   **Common Execution Errors:**
    *   **`KeyError`:** Thrown if you try to search or update a label that does not exist in the Series.
    *   **`ValueError`:** Thrown during Series construction if the length of custom index labels does not match the length of the data values.

---

### **Stage 3: Creating and Manipulating DataFrames (Two-Dimensional Data)**
A **DataFrame** is a two-dimensional labeled grid, table, or tabular data structure with rows and columns.
*   **DataFrame Constructor:** 
    `pd.DataFrame(data, index=...)`. Note that "D" and "F" are capitalized because it is a constructor.
    *   **`data` argument:** Typically a Python dictionary of lists (where dictionary keys become column headers and lists represent row values) or a list of dictionaries.
    *   **`index` keyword argument:** `index=...` is used to manually assign custom labels to rows.
*   **Row Selection by Label:** 
    `df.loc['row_label']`. Accesses all data for a specific row as an object.
*   **Row Selection by Integer Position:** 
    `df.iloc[integer_index]`. Accesses a row by its numeric position.
*   **Adding a Column:** 
    `df['new_column_name'] = list_of_values`. Assigns a list of values to a new column subscript; the list's length must match the existing number of rows.
*   **DataFrame Concatenation Function:** 
    `pd.concat([df1, df2])`. Used to merge or add rows to an existing DataFrame by passing them in a Python list. *(Note: `append` is deprecated and no longer used)*. Must be reassigned (`df = pd.concat(...)`) to save.

---

### **Stage 4: File I/O (Importing & Exporting Files)**
*   **Read CSV Function:** 
    `pd.read_csv('filepath', index_col='column_name')`. Imports comma-separated values into a DataFrame. The optional `index_col` keyword argument sets a specific column to act as the row labels instead of numbers.
*   **Read JSON Function:** 
    `pd.read_json('filepath')`. Imports JavaScript Object Notation data into a DataFrame.
*   **Full Output String Function:** 
    `.to_string()`. Added to a DataFrame or Series output to print the entire dataset without truncation (preventing pandas from default-printing only the first and last five rows).

---

### **Stage 5: Selection & Slicing Techniques**
*   **Selection by Column:** 
    `df['column_name']`. Returns a single column as a Series.
*   **Selection of Multiple Columns:** 
    `df[['col1', 'col2']]`. Uses a nested list inside the subscript operator to return a multi-column DataFrame.
*   **Row and Column Selection by Label:** 
    `df.loc['row_label', ['col1', 'col2']]`. Selects a row and limits the output to specified columns.
*   **Label Slicing Operator:** 
    `:`. Used inside `.loc[]` to select a range of rows (e.g., `df.loc['Start_Row':'End_Row']` where the end label is inclusive).
*   **Integer Slicing Operator:** 
    `df.iloc[start:end]`. Selects rows by numeric indices; the second number (`end`) is exclusive.
*   **Slicing with Step:** 
    `df.iloc[start:end:step]`. Adds a step value to skip rows (e.g., `df.iloc[0:11:2]` returns every second row).
*   **Integer Row & Column Slicing:** 
    `df.iloc[row_slice, column_slice]`. Restricts slicing to specific rows and column indices (e.g., `df.iloc[0:11, 0:3]` gets the first 10 rows and the first 3 columns).

---

### **Stage 6: Row Filtering with Logical Conditions**
*   **Single Condition Filtering:** 
    `df[df['column_name'] >= value]`. Keeps only the rows that match the condition inside the subscript operator.
*   **Logical OR Operator:** 
    `|`. A C-style vertical bar used to combine "either/or" conditions (e.g., `df[(cond1) | (cond2)]`). Individual conditions must be enclosed in parentheses. *(Note: Python's standard `or` word cannot be used)*.
*   **Logical AND Operator:** 
    `&`. A C-style ampersand used to filter rows where both conditions are true (e.g., `df[(cond1) & (cond2)]`). Conditions must be enclosed in parentheses. *(Note: Python's standard `and` cannot be used)*.

---

### **Stage 7: Aggregate Functions & Grouping**
Aggregate functions reduce a set of multiple values down to a single summary value.
*   **Mean/Average:** 
    `df.mean(numeric_only=True)`. Calculates average values. The `numeric_only=True` keyword argument is required when applying it to a whole DataFrame that contains non-numeric data (such as strings/names), or it will fail.
*   **Sum:** 
    `df.sum(numeric_only=True)`. Calculates the combined total of numeric columns.
*   **Minimum:** 
    `df.min()`. Finds the lowest value.
*   **Maximum:** 
    `df.max()`. Finds the highest value.
*   **Count:** 
    `df.count()`. Counts non-null values (any null/NaN values are excluded from the count).
*   **Column Aggregation:** 
    `df['column_name'].mean()`. Calls the aggregate function directly on a single column without needing `numeric_only=True`.
*   **Groupby Function:** 
    `df.groupby('column_name')`. Groups rows sharing a common column value into a group object. Applying an aggregate function to this group object (e.g., `df.groupby('type')['height'].mean()`) returns a summary Series grouped by those unique values.

---

### **Stage 8: Data Cleaning (75% of Pandas Work)**
*   **Drop Columns Function:** 
    `df.drop(columns=['col1', 'col2'])`. Removes irrelevant columns by passing them in a list. You must reassign it (`df = df.drop(...)`) because it returns a new DataFrame.
*   **Drop Null Values Function:** 
    `df.dropna(subset=['column_name'])`. Drops any entire row if it is missing a value within the columns specified in the `subset` list.
*   **Fill Null Values Function:** 
    `df.fillna({'column_name': 'replacement'})`. Replaces missing values (NaN) within specified columns with a custom value (e.g., replacing NaN with the word "none") using a dictionary.
*   **Replace Inconsistent Values Function:** 
    `df['column'].replace({old_value: new_value})`. Replaces specific matching values within a Series using a dictionary mapping.
*   **String Lowercase Method:** 
    `df['column'].str.lower()`. Standardizes text values in a column to lowercase by accessing the string `.str` property accessor of the Series.
*   **Data Type Casting Function:** 
    `df['column'].astype(bool)` *(referred to as "as type" in the transcript)*. Converts a column's data type (e.g., converting 0s and 1s to boolean `False` and `True`).
*   **Drop Duplicate Rows Function:** 
    `df.drop_duplicates()`. Removes duplicate rows from the dataset. Must be reassigned (`df = df.drop_duplicates()`) to save changes.

