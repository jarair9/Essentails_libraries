# NumPy — A Beginner's Book

**Chapters included: 1 & 2 (with hands-on practices and solutions)**

---

## Preface

This short book-style guide teaches NumPy from the very beginning. Each chapter contains explanations, examples you can run in Python, and exercises labeled **Practice**. Solutions are provided but placed after the exercises so you can try them first.

---

# Chapter 1 — Getting Started

### 1.1 What is NumPy?

NumPy (Numerical Python) is the fundamental package for numerical computing in Python. It provides:

* A fast and memory-efficient `ndarray` (N-dimensional array) object
* Broadcasting and vectorized operations (fast math without Python loops)
* Tools for linear algebra, random numbers, statistics, and more

### 1.2 Installation

If you use `pip`:

```bash
pip install numpy
```

If you use conda (recommended for scientific stacks):

```bash
conda install numpy
```

### 1.3 Importing NumPy

```python
import numpy as np
```

Use `np` as the conventional alias.

### 1.4 First commands

```python
import numpy as np

# Create a 1D array from a Python list
a = np.array([1, 2, 3])
print(a)         # [1 2 3]
print(type(a))   # <class 'numpy.ndarray'>

# Create a 2D array
b = np.array([[1,2,3], [4,5,6]])
print(b.shape)   # (2, 3)
```

### 1.5 Why use NumPy vs Python lists?

* NumPy arrays store elements in contiguous memory and use a fixed dtype => faster and less memory.
* Vectorized operations are implemented in C and run much faster than Python loops.

---

# Chapter 1 Practice

**Practice 1.1**

1. Install NumPy (if you don’t have it). Import as `np` and print the NumPy version.
2. Create a 1D array of integers `[10, 20, 30, 40]` and print its `dtype`, `shape`, and `ndim`.

**Practice 1.2**
Create a 3x3 identity matrix using NumPy and assign it to `I`. Print `I`.

**Try these in a Python REPL or notebook.**

---

# Chapter 2 — Arrays, Types, and Basic Operations

### 2.1 Creating arrays

From lists/tuples:

```python
x = np.array([1, 2, 3])
M = np.array([[1, 2], [3, 4]])
```

Common factory functions:

```python
np.zeros((2,3))      # zeros
np.ones((3,))        # ones
np.empty((2,2))      # uninitialized (faster)
np.arange(0, 10, 2)  # like range, returns array
np.linspace(0, 1, 5) # 5 evenly spaced values
np.eye(4)            # identity matrix
np.full((2,2), 7)    # fill with 7s
```

### 2.2 Data types (dtypes)

Arrays have a single `dtype` (data type). Common dtypes:

* `np.int64`, `np.int32`
* `np.float64`, `np.float32`
* `np.bool_`
* `np.object_` (less common for numeric work)

Check and set dtype:

```python
arr = np.array([1.0, 2.0])
arr.dtype            # float64
arr_int = arr.astype(np.int32)
```

### 2.3 Basic arithmetic (vectorized)

```python
x = np.array([1,2,3])
y = np.array([4,5,6])

x + y    # elementwise add -> [5,7,9]
x * y    # -> [4,10,18]
2 * x    # scalar broadcasting -> [2,4,6]

# Dot product
np.dot(x, y)  # 1*4 + 2*5 + 3*6 = 32
```

### 2.4 Indexing and slicing

```python
A = np.arange(1,10).reshape(3,3)  # [[1..3],[4..6],[7..9]]
A[0,1]     # row 0, col 1 -> 2
A[1]       # second row -> [4,5,6]
A[:,2]     # third column -> [3,6,9]
A[0:2, 0:2]# top-left 2x2
```

**Note**: Slices are *views* (not copies) when possible — modifying a slice may change the original array.

### 2.5 Boolean indexing (masking)

```python
v = np.array([10, 15, 20, 25])
mask = v > 15         # [False, False, True, True]
v[mask]               # returns [20, 25]
v[v % 20 == 0]        # returns [20]
```

### 2.6 Broadcasting rules (short)

NumPy will automatically expand shapes to make operations compatible if:

* dimensions are equal, or
* one of the dimensions is 1

Example:

```python
x = np.array([1,2,3])     # shape (3,)
y = np.array([[10],[20]]) # shape (2,1)
# y + x -> shape (2,3): [[11,12,13], [21,22,23]]
```

### 2.7 Aggregation functions

```python
A.sum()
A.mean()
A.max()
A.min()
A.std()

# By axis
A.sum(axis=0)  # sum columns
A.sum(axis=1)  # sum rows
```

### 2.8 Reshaping and stacking

```python
v = np.arange(6)         # [0..5]
v.reshape(2,3)           # shape (2,3)

np.concatenate([a, b], axis=0)
np.vstack([a,b])
np.hstack([a,b])
```

---

# Chapter 2 Practice

**Practice 2.1 — arrays & dtype**

1. Create an array of floats from 0.0 to 4.0 inclusive using `np.linspace` with 5 elements. Check dtype.
2. Convert it to `np.int64` and explain (in a comment) what happened to the values.

**Practice 2.2 — operations & broadcasting**

1. Let `A = np.array([[1,2,3],[4,5,6]])` and `b = np.array([10, 20, 30])`. Compute `A + b` and explain why it works.
2. Multiply `A` by `np.array([[2],[10]])` and show the result.

**Practice 2.3 — indexing and slicing**
Given `M = np.arange(1,17).reshape(4,4)`:

1. Extract the central 2x2 submatrix.
2. Replace all even numbers in `M` with -1 using boolean indexing.

**Practice 2.4 — aggregations and reshape**

1. For `M` from above, compute the column-wise mean (shape should be (4,)).
2. Flatten `M` to a 1D array and then reshape into (2,8).

---

# Practice Solutions (try them after attempting!)

> **Solutions for Chapter 1**

**Practice 1.1**

```python
import numpy as np
print(np.__version__)
arr = np.array([10,20,30,40])
print(arr.dtype, arr.shape, arr.ndim)
```

**Practice 1.2**

```python
I = np.eye(3)
print(I)
```

> **Solutions for Chapter 2**

**Practice 2.1**

```python
arr = np.linspace(0.0, 4.0, 5)
print(arr, arr.dtype)
arr_int = arr.astype(np.int64)
print(arr_int)
# Converting to int truncates the decimal part (floor toward 0 for positive numbers)
```

**Practice 2.2**

```python
A = np.array([[1,2,3],[4,5,6]])
b = np.array([10,20,30])
print(A + b)
# A.shape = (2,3); b.shape = (3,) -> b broadcasts to (2,3) and elementwise add

print(A * np.array([[2],[10]]))
# array([[  2,   4,   6], [ 40,  50,  60]])
```

**Practice 2.3**

```python
M = np.arange(1,17).reshape(4,4)
center = M[1:3, 1:3]
print(center)

# Replace evens with -1
M[M % 2 == 0] = -1
print(M)
```

**Practice 2.4**

```python
M = np.arange(1,17).reshape(4,4)
col_mean = M.mean(axis=0)
print(col_mean)

flat = M.ravel()    # or flatten()
print(flat)
print(flat.reshape(2,8))
```

---

# Next steps

If this looks good I will prepare **Chapter 3** (advanced indexing, broadcasting deep dive, performance tips, and linear algebra) next. Tell me if you want exercises as Jupyter notebooks, or want the chapters to include quizzes, more examples, or interactive notebooks.

Happy learning! 🚀
