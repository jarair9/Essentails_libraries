import numpy as np


arr_int = np.array([1, 2, 3, 4, 5])
arr_float = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
arr_complex = np.array([1+2j, 3+4j, 5+6j])
arr_bool = np.array([True, False, True, False])
arr_str = np.array(['apple', 'banana', 'cherry'])

print("Integer Array:", arr_int)
print("Float Array:", arr_float)
print("Complex Array:", arr_complex)
print("Boolean Array:", arr_bool)
print("String Array:", arr_str)


arr_int1 = np.array([1, 2, 3, 4, 5])
print(arr_int1.dtype)
arr_float2 = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print(arr_float2.dtype)